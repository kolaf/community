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
- `terminal/`: **all terminal commands are summarized in `terminal/README.md`** (say "terminal help" to open it). Voice navigation for the shell in Windows Terminal (WSL). The shell hook `talon-terminal.bash`
  (installed by the dotfiles Ansible playbook, sourced from `.bashrc`) writes the current folder, its sub-folders and files
  and zoxide's folders to `%USERPROFILE%\.cache\hv\terminal-state.txt` after every prompt; `terminal_state.py` turns that into
  spoken lists. Commands: `into <folder>` / `into numb <n>`, `pick <folder>` / `pick file <file>` (types the quoted name),
  `folders` (numbered list), `jump <name>` / `jump list` / `jump back` (zoxide), `fuzzy file|folder|history [text]` (fzf).
  Also `out of [n]` (go up), `history [words]` (atuin), `history list <words>`, `jump show`, picker keys (`choose it`,
  `edit it`, `result next|back`, `cancel search`), and the yazi file manager: `file browser` / `browse <folder>` run the shell
  function `y`; while it runs, `yazi.talon` (up, down, parent, open it, select, copy it, cut it, paste it, trash it, find,
  search name, fuzzy jump, zoxide jump, quit yazi ...) is active. No title parsing and no wsl.exe calls. The most recently
  used shell wins when several are open.
- `handy/`: Talon <-> Handy. Voice transforms ("make that formal|informal|shorter|fuller|clearer", "fix that up", "translate
  that to norwegian|english", "bullet that", "summarize that") on the selection or the last dictation; "transcribe latest meeting" (newest OBS recording and its parts; add "with speakers" for speaker labels), "language model local|cloud" (switch the post-processing language model), "transcribe meeting" (in Explorer: minutes from the selected audio files), "model parakeet|norwegian|picker" (switch the speech model), "scratch that" (made context-aware: Talon's own phrase or Handy's dictation, whichever is newer), "scratch dictation", "redo as email|message|note|formal|...", "edit this" (free-form
  change by voice, replaces the selection) and "reply to this"
  (copies the selected message and dictates the reply with the reply prompt; stop with your Handy key); and Talon switches its
  speech off while Handy records (`user.kolaf_mute_during_handy`) so dictation is not taken for commands. Handy path:
  `user.kolaf_handy_path` (default `D:/Handy/handy.exe`).
- Linux: `terminal/terminal_linux.talon`, `terminal/yazi_linux.talon` and `handy/explorer_linux.talon` repeat the commands for Linux terminals and file managers. Untested (no Linux machine with Talon).
- `silverbullet/`: voice commands for SilverBullet in the browser, all starting with "silver" (page picker, command palette, journal, formatting, outline, tasks); see `silverbullet/README.md`.
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
