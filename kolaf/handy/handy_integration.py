"""Talon <-> Handy: voice transforms, "reply to this", and staying quiet while Handy records.

Handy is driven through its command line (a running Handy receives the flags) and tells Talon whether it is recording
through %USERPROFILE%\\.cache\\hv\\handy-state.txt ("recording" or "idle", then a Unix time, rewritten every few seconds
while recording). While Handy records, Talon switches its speech off so the dictation is not taken for commands, and
switches it on again afterwards (only if it was Talon that switched it off).
"""
import os
import subprocess
import time
from pathlib import Path

from talon import Module, actions, app, cron, settings

from user.community.kolaf.hv.hv import _clipboard_paths

mod = Module()

mod.list("kolaf_handy_model", desc="Spoken names of speech models; the value is part of the model's name or id")
mod.list("kolaf_handy_prompt", desc="Spoken names of the Handy prompts that \"redo as ...\" can use")

mod.setting(
    "kolaf_handy_path",
    type=str,
    default="D:/Handy/handy.exe",
    desc="The Handy program to send commands to",
)
mod.setting(
    "kolaf_mute_during_handy",
    type=bool,
    default=True,
    desc="Switch Talon's speech off while Handy records, and back on afterwards",
)

STATE_FILE = Path.home() / ".cache" / "hv" / "handy-state.txt"
STALE_AFTER_SECONDS = 12  # a "recording" older than this is a leftover from a crash

_muted_by_us = False


def parse_state(text: str, now: float):
    """Returns True if the state file says Handy is recording right now."""
    lines = text.split()
    if len(lines) < 2 or lines[0] != "recording":
        return False
    try:
        written = float(lines[1])
    except ValueError:
        return False
    return now - written <= STALE_AFTER_SECONDS


def handy_is_recording() -> bool:
    try:
        return parse_state(STATE_FILE.read_text(encoding="utf-8"), time.time())
    except OSError:
        return False


def poll():
    """Runs a few times a second: mute Talon while Handy records, unmute afterwards."""
    global _muted_by_us
    if not settings.get("user.kolaf_mute_during_handy"):
        _muted_by_us = False
        return
    recording = handy_is_recording()
    if recording and not _muted_by_us and actions.speech.enabled():
        _muted_by_us = True
        actions.speech.disable()
    elif not recording and _muted_by_us:
        _muted_by_us = False
        if not actions.speech.enabled():
            actions.speech.enable()


def run_handy(args):
    path = settings.get("user.kolaf_handy_path")
    if not os.path.exists(path):
        path = "handy"
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    subprocess.Popen([path, *args], creationflags=flags, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@mod.action_class
class Actions:
    def kolaf_handy_run(args: list[str]):
        """Send command line flags to the running Handy"""
        run_handy(args)

    def kolaf_handy_transform(prompt_id: str):
        """Run the selection (or, with nothing selected, the last dictation) through a Handy transform prompt"""
        run_handy(["--transform", prompt_id])

    def kolaf_handy_dictate_with(prompt_id: str):
        """Copy the selection, then dictate with a Handy prompt for this one dictation (stop with your Handy key)"""
        actions.edit.copy()
        actions.sleep("200ms")
        run_handy(["--use-prompt-once", prompt_id, "--toggle-post-process"])

    def kolaf_handy_dictate_as(prompt_id: str):
        """Start a dictation that uses a given Handy prompt for this one dictation (stop with your Handy key)"""
        run_handy(["--use-prompt-once", prompt_id, "--toggle-post-process"])

    def kolaf_handy_transcribe_selected(language: str = "", speakers: bool = False, project: str = ""):
        """Write meeting minutes from the audio files (or folder) selected in the file manager"""
        actions.edit.copy()
        actions.sleep("300ms")
        paths = _clipboard_paths()
        if not paths:
            app.notify("Handy: no files selected")
            return
        args = ["--meeting-minutes", ";".join(paths)]
        if language:
            args += ["--meeting-language", language]
        if speakers:
            args.append("--meeting-speakers")
        if project:
            args += ["--meeting-project", project]
        run_handy(args)
        app.notify(f"Handy: transcribing {len(paths)} item(s)")

    def kolaf_handy_transcribe_latest(single: bool = False, speakers: bool = False, project: str = ""):
        """Write meeting minutes from the latest recording in the recorder's folder (set on Handy's Meetings page)"""
        args = ["--meeting-latest"]
        if single:
            args.append("--meeting-single")
        if speakers:
            args.append("--meeting-speakers")
        if project:
            args += ["--meeting-project", project]
        run_handy(args)

    def kolaf_handy_set_model(name: str):
        """Switch Handy's speech model; name is part of the model's name or id"""
        run_handy(["--set-model", name])

    def kolaf_handy_set_llm(name: str):
        """Switch Handy's post-processing language model: local (a llama-server on this computer) or cloud (the hosted gateway)"""
        run_handy(["--set-llm", name])

    def kolaf_handy_model_picker():
        """Open Handy's numbered list of downloaded speech models"""
        run_handy(["--model-picker"])

    def kolaf_handy_redo(prompt_id: str):
        """Replace the last dictation by the same recording processed again with another prompt"""
        run_handy(["--redo-with", prompt_id])

    def kolaf_handy_scratch():
        """Delete the last dictation, if it is really the text before the cursor"""
        run_handy(["--scratch-last"])

    def kolaf_handy_mute_now():
        """Is Handy recording right now (for debugging)"""
        return handy_is_recording()


cron.interval("300ms", poll)
