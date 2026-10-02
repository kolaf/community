# kolaf: personal Talon setup (lives inside this community fork)

Everything here is loaded by Talon automatically because it sits under `user/community/`. It is in one folder so that
merging upstream community never conflicts. Clone this fork into `user/` on any machine and you get it all.

## Contents

- `personal/`: the wake key (`Ctrl+PageUp` toggles speech), spoken wake commands disabled, `drowse`, the `shock` key, and
  `sleep.py` (Talon starts asleep: it calls `speech.disable()` when Talon is ready; note that reloading it puts Talon to sleep).
  The wake overrides use community's context plus the tag `user.disable_voice_wake`, so they win. To get voice wake
  back, delete the `tag()` line in `wake_key_and_tag.talon`.
- `hv/`: the voice shell front end (`hermes <request>`, `hermes go`, `grab files`). It types `hv ...` into a terminal, so
  it needs the `hv` script on that machine (`fork/voice-shell/hv` in the `kolaf/Handy` repo, symlinked to `~/.local/bin/hv`).
- `handy-bridge/`: Talon commands for Handy (one key that starts or stops a dictation and mutes Talon, language and
  prompt commands). **Disabled** (`*.disabled`) because it is untested and mutes Talon if Handy cannot be started.
  To enable: rename both files (drop `.disabled`) and set the Handy path, e.g. in a `.talon` file:
  `settings(): user.handy_path = "D:/Handy/handy.exe"` (Windows) or leave the default `handy` (Linux).

All of this was written without a Talon test session for the voice behaviour. What was checked: Talon loads the files without
errors and its registry contains the commands. Not checked: the spoken behaviour itself.

## Setting this up on another machine

1. Install Talon, then in its user folder (`%APPDATA%\talon\user` on Windows, `~/.talon/user` on Linux):
   `git clone https://github.com/kolaf/community.git`, then `cd community`, then
   `git remote add upstream https://github.com/talonhub/community.git`.
2. The other packages (separate repos; versions as found on 2 October 2026, both old):
   - `cursorless-talon` https://github.com/cursorless-dev/cursorless-talon.git (last commit 2024-02-21)
   - `rango-talon` https://github.com/david-tejada/rango-talon.git (2024-03-06)
   - `cursorless-settings`: not a git repo; copy the folder.
   Check that the Cursorless Talon side matches the VS Code extension's version before relying on it.
   `talon-ai-tools` is deliberately **not** used any more: its main job (rewrite the selected text from a spoken
   instruction) is done by Handy's `edit` prompt, so the GPT key now lives in one place only (Handy's settings).
3. Machine-level file that is **not** in git: `user/settings.talon` (speech timeout). Keep API keys out of this repo.

## Updating community from upstream

`git fetch upstream && git merge upstream/main` (merge, do not reset: that would delete `kolaf/`). Our files are in a folder
upstream does not have, so the merge should not conflict. Then check `talon.log` for errors.
