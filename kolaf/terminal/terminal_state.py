"""Voice navigation for a shell, driven by a small state file the shell writes after every prompt.

The shell hook (dotfiles: talon-terminal.bash) writes %USERPROFILE%\\.cache\\hv\\terminal-state.txt:
    v1 / cwd / sig / d <subfolder> / f <file> / z <folder zoxide knows>
so no window-title parsing and no wsl.exe calls are needed. This module turns it into three lists
(sub-folders, files, zoxide folders) that are active in Windows Terminal, plus the actions the commands use.
The most recently used shell wins when several terminals are open.
"""
import os
import shlex
from pathlib import Path

from talon import Context, Module, actions, cron, imgui

mod = Module()
ctx = Context()
ctx.matches = r"""
app: windows_terminal
"""

# Beats the community WSL actions (apps/wsl/wsl.py) in the same tab.
ctx_wsl = Context()
ctx_wsl.matches = r"""
app: windows_terminal
title: /ubuntu|wsl|@/i
tag: user.wsl
tag: terminal
"""

mod.tag("kolaf_yazi", desc="The yazi file manager is running in the terminal (set by the shell wrapper 'y')")
mod.list("kolaf_dir", desc="Sub-folders of the folder the shell is in")
mod.list("kolaf_file", desc="Files in the folder the shell is in")
mod.list("kolaf_jump", desc="Folders zoxide knows, by their last name")

STATE_FILE = Path.home() / ".cache" / "hv" / "terminal-state.txt"
MODE_FILE = STATE_FILE.with_name("terminal-mode.txt")
WORDS_TO_EXCLUDE = ["and", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "dot", "exe"]
PAGE = 20

_mtime = None
_cwd = ""
_dirs: list = []
_files: list = []
_jump: list = []
_mode = ""


def parse_state(text: str):
    """Returns (cwd, dirs, files, jump_paths) from the state file text; unknown or damaged input gives empty results."""
    lines = text.splitlines()
    if not lines or lines[0] != "v1":
        return "", [], [], []
    cwd, dirs, files, jump = "", [], [], []
    for line in lines[1:]:
        kind, _, value = line.partition("\t")
        if not value:
            continue
        if kind == "cwd":
            cwd = value
        elif kind == "d":
            dirs.append(value)
        elif kind == "f":
            files.append(value)
        elif kind == "z":
            jump.append(value)
    return cwd, dirs, files, jump


def last_names(paths):
    """Unique last path components of the folders zoxide knows, in the order given."""
    seen, names = set(), []
    for path in paths:
        name = path.rstrip("/").rsplit("/", 1)[-1]
        if name and name not in seen:
            seen.add(name)
            names.append(name)
    return names


def spoken(names):
    if not names:
        return {}
    return actions.user.create_spoken_forms_from_list(names, words_to_exclude=WORDS_TO_EXCLUDE)


def read_mode() -> str:
    try:
        return MODE_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def refresh_mode():
    """The shell wrapper writes 'yazi' while the file manager runs; any prompt clears it."""
    global _mode
    mode = read_mode()
    if mode != _mode:
        _mode = mode
        ctx.tags = ["user.kolaf_yazi"] if mode == "yazi" else []


def refresh():
    """Cheap: one stat per call; the file is only read and the lists rebuilt when it changed."""
    global _mtime, _cwd, _dirs, _files, _jump
    refresh_mode()
    try:
        mtime = STATE_FILE.stat().st_mtime_ns
    except OSError:
        return
    if mtime == _mtime:
        return
    try:
        text = STATE_FILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    _mtime = mtime
    _cwd, _dirs, _files, jump_paths = parse_state(text)
    _jump = last_names(jump_paths)
    ctx.lists["user.kolaf_dir"] = spoken(_dirs)
    ctx.lists["user.kolaf_file"] = spoken(_files)
    ctx.lists["user.kolaf_jump"] = spoken(_jump)
    if folders_gui.showing:
        folders_gui.show()


def quote(name: str) -> str:
    return shlex.quote(name)


@ctx_wsl.action_class("user")
class WslActions:
    def terminal_kill_all():
        # The community version also types "y" and Enter (for Windows' "Terminate batch job?"). In bash that would run
        # the command "y", which is the yazi wrapper here.
        actions.key("ctrl-c")


HELP_FILE = Path(__file__).with_name("README.md")


@imgui.open(y=10, x=900)
def folders_gui(gui: imgui.GUI):
    gui.text(f"Folders in {_cwd}")
    gui.line()
    for index, name in enumerate(_dirs[:PAGE], start=1):
        gui.text(f"{index}: {name}")
    if len(_dirs) > PAGE:
        gui.text(f"... and {len(_dirs) - PAGE} more")
    gui.spacer()
    if gui.button("Folders hide"):
        folders_gui.hide()


@mod.action_class
class Actions:
    def kolaf_terminal_cd(name: str):
        """Change into a sub-folder of the shell's current folder"""
        actions.insert(f"cd -- {quote(name)}")
        actions.key("enter")

    def kolaf_terminal_up(levels: int):
        """Go up one or more folders (the opposite of 'into')"""
        levels = max(1, min(levels, 20))
        actions.insert("cd " + "/".join([".."] * levels))
        actions.key("enter")

    def kolaf_terminal_cd_number(number: int):
        """Change into the numbered sub-folder shown by 'folders'"""
        if 1 <= number <= len(_dirs):
            actions.user.kolaf_terminal_cd(_dirs[number - 1])

    def kolaf_terminal_pick(name: str):
        """Type a file or folder name, quoted, at the cursor"""
        actions.insert(quote(name) + " ")

    def kolaf_terminal_jump(query: str):
        """Jump with zoxide to the best match for the words"""
        actions.insert(f"z {quote(query)}")
        actions.key("enter")

    def kolaf_terminal_press(keys: str, count: int = 1):
        """Press a key (or key sequence) several times"""
        for _ in range(max(1, min(count, 50))):
            actions.key(keys)

    def kolaf_terminal_type_after(keys: str, text: str, submit: bool = False):
        """Press a key that opens a prompt, type the words, optionally press enter"""
        actions.key(keys)
        actions.sleep("150ms")
        actions.insert(text)
        if submit:
            actions.key("enter")

    def kolaf_terminal_browse(name: str):
        """Open the yazi file manager in a sub-folder"""
        actions.insert(f"y -- {quote(name)}")
        actions.key("enter")

    def kolaf_terminal_help():
        """Open the summary of the terminal voice commands"""
        os.startfile(str(HELP_FILE))

    def kolaf_terminal_folders_toggle():
        """Show or hide the numbered list of sub-folders"""
        if folders_gui.showing:
            folders_gui.hide()
        else:
            refresh()
            folders_gui.show()


cron.interval("700ms", refresh)
refresh()
