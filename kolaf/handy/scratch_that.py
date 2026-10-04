"""Context-aware "scratch that": Talon's own, or Handy's, whichever put text on the screen last.

The community "scratch that" (and "nope that") deletes the last phrase that Talon typed, character by character. Text that
Handy pasted is not in Talon's phrase list, so after a Handy dictation it would delete the wrong amount. Here:
- Talon's phrase list gets a time stamp for every phrase (this file wraps `user.add_phrase_to_history`);
- Handy writes the time of its last undoable paste to %USERPROFILE%\\.cache\\hv\\handy-paste.txt ("<unix ms>\\n<chars>", or
  "none" once it was taken back);
- "scratch that" asks Handy to take its paste back if that is newer than Talon's last phrase (and not older than five
  minutes, which is as far back as Handy goes), otherwise it does what it always did. Repeating it works down the list.
"""
import time
from pathlib import Path

from talon import Context, actions

import user.community.core.text.phrase_history as phrase_history_module

ctx = Context()

PASTE_FILE = Path.home() / ".cache" / "hv" / "handy-paste.txt"
HANDY_MAX_AGE_MS = 5 * 60 * 1000  # Handy does not take back anything older

# Time (ms) at which each phrase in Talon's phrase list was typed, newest first, kept the same length as that list.
_phrase_times: list = []


def now_ms() -> int:
    return int(time.time() * 1000)


def parse_paste_ms(text: str) -> int:
    """The time of Handy's last undoable paste in ms, or 0 if there is none."""
    first = text.split()[0] if text.split() else ""
    return int(first) if first.isdigit() else 0


def handy_paste_ms() -> int:
    try:
        return parse_paste_ms(PASTE_FILE.read_text(encoding="utf-8"))
    except OSError:
        return 0


def choose(handy_ms: int, talon_ms: int, now: int) -> str:
    """Which "scratch that" to run: 'handy' only for a paste that is newer than Talon's last phrase and recent enough."""
    if handy_ms > talon_ms and now - handy_ms <= HANDY_MAX_AGE_MS:
        return "handy"
    return "talon"


def _align():
    """Entries removed from the front of the phrase list (scratched) leave the front of the times too."""
    size = len(phrase_history_module.phrase_history)
    while len(_phrase_times) > size:
        _phrase_times.pop(0)
    while len(_phrase_times) < size:
        _phrase_times.append(0)  # older than this file's tracking


@ctx.action_class("user")
class UserActions:
    def add_phrase_to_history(text: str):
        _align()
        actions.next(text)
        _phrase_times.insert(0, now_ms())
        del _phrase_times[len(phrase_history_module.phrase_history) :]

    def clear_last_phrase():
        _align()
        talon_ms = _phrase_times[0] if _phrase_times else 0
        if choose(handy_paste_ms(), talon_ms, now_ms()) == "handy":
            actions.user.kolaf_handy_scratch()
        else:
            actions.next()
            _align()
