# Terminal voice commands (Windows Terminal, Ubuntu/WSL)

Say **"terminal help"** in a terminal to open this file. Words in `<angle brackets>` are what you say; `[square]` is optional.
The commands marked **kolaf** are in this folder; the others come from the community setup (`tags/terminal`, `apps/git`,
`core/windows_and_tabs`, ...). Nothing here has been verified by voice yet: the files load without errors and the lists
build, but the spoken behaviour is untested. Report what does not work.

## Setup that this depends on

- The shell hook `talon-terminal.bash` (dotfiles Ansible role, sourced from `.bashrc`). Open a **new** terminal, or run
  `source ~/.bashrc`, after it was installed. It writes the current folder, its contents and zoxide's folders to
  `%USERPROFILE%\.cache\hv\terminal-state.txt` after each prompt. With several terminals open, the last one you used wins.
- `zoxide`, `fzf`, `atuin` and `yazi` installed (the dotfiles playbook does it). `y` is a shell function from the hook.

## Moving around

| Say | Does |
|---|---|
| `into <folder>` | `cd` into a sub-folder of the current folder (kolaf) |
| `into numb <n>` | `cd` into folder number *n* of the `folders` list (kolaf) |
| `out of` / `out of <n>` | go up one / *n* folders (kolaf) |
| `folders` / `folders hide` | numbered list of the sub-folders on screen (kolaf) |
| `jump <name>` | zoxide: `z <name>`, the best match for a folder it knows (kolaf) |
| `jump <any words>` | the same with free words, e.g. "jump air sports" (kolaf) |
| `jump list` | zoxide's interactive picker, `zi` (kolaf) |
| `jump back` | `z -`, the previous folder (kolaf) |
| `jump show [<words>]` | list the folders zoxide knows, with scores (kolaf) |
| `katie [dir] [<text>]` | `cd <text>` (community) |
| `katie up` / `katie back` | `cd ..` (community) |
| `katie root` | `cd /` (community) |
| `lisa [dir] [<text>]` | `ls <text>` (community) |
| `lisa all` | `ls -a` (community; uses the Linux flavour thanks to `wsl.talon`) |
| `go <name>` | jump to the folder zoxide knows by that name, like `jump <name>` (kolaf; replaces the community *go <system path>*, which used Windows folders) |
| `path <name>` | type the full path, quoted, of the best-ranked zoxide folder with that name (kolaf; replaces the community *path <system path>*) |

## Community folder pickers (work in WSL through the state file)

The community file-manager commands are active in this terminal. They read the folder from the shell hook, so there is no
`wsl.exe` call and no window-title parsing.

| Say | Does |
|---|---|
| `manager show` / `manager close` / `manager refresh` | show / hide / refresh the numbered folder and file lists |
| `follow <folder>` / `follow numb <n>` | `cd` into that folder (community; `into` is the lighter kolaf version) |
| `go parent` / `daddy` | up one folder |
| `folder next` / `folder last`, `file next` / `file last` | page through long lists |

The community `open <file>`, `select file ...` and `select folder ...` have no terminal implementation and do nothing here;
use `pick file <file>` and then type what you want to do with it.

## Files and names

| Say | Does |
|---|---|
| `pick <folder>` | type the folder's name, quoted, at the cursor (kolaf) |
| `pick file <file>` | type a file's name, quoted, at the cursor (kolaf) |
| `copy paste` | copy the selection and paste it (community) |

Spoken forms are made from the real names: `.cargo` can be said "cargo" or "dot cargo", `handy_app` as "handy app".

## Searching: fzf, atuin, zoxide

| Say | Does |
|---|---|
| `fuzzy file [<words>]` | fzf file search (Ctrl-T), then the words (kolaf) |
| `fuzzy folder [<words>]` | fzf folder search (Alt-C) (kolaf) |
| `history [<words>]` | atuin interactive history search (Ctrl-R), types the words (kolaf) |
| `history list <words>` | print the 15 best atuin matches (kolaf) |
| `history last` | print the last 10 commands from atuin (kolaf) |
| `fuzzy history [<words>]` | same key as `history` (atuin owns Ctrl-R) (kolaf) |
| `rerun [<text>]` / `rerun search` | Ctrl-R with the text (community) |
| `run last` | Up, Enter: repeat the last command (community) |

**Choosing in a picker** (fzf, atuin, zoxide's `jump list`), all kolaf:
`result next` / `result back` / `result page` move, `choose it` = Enter (atuin runs the command), `edit it` = Tab
(atuin puts the command on the prompt without running it; fzf toggles a multi-selection), `cancel search` = Escape.

## yazi, the file manager

`file browser` starts it here, `browse <folder>` starts it in a sub-folder (both run the shell function `y`).
Quit with `quit yazi` to **take the shell with you** to the folder you ended in, or `quit here` to stay where you were.
The commands below are only active while yazi runs (the `y` function tells Talon). Keys are yazi's defaults; `yazi help`
shows them.

| Say | Does | Say | Does |
|---|---|---|---|
| `up [<n>]` / `down [<n>]` | move | `select` / `select all` | mark / mark all |
| `parent` | go to the parent folder | `visual mode` | select a range |
| `open it` | enter folder / open file | `copy it` / `cut it` | yank / cut |
| `history back` / `history forward` | previous / next folder visited | `paste it` / `paste over` | paste / overwrite |
| `top` / `bottom` | first / last entry | `trash it` | move to trash |
| `page down` / `page up` | half page | `rename it` | rename |
| `create [<name>]` | new file (end with `/` for a folder) | `toggle hidden` | show dot files |
| `copy path` / `copy name` | copy to the clipboard | `find <words>` | find in this folder |
| `search name <words>` | search file names | `search content <words>` | search inside files |
| `next match` / `previous match` | next / previous find result | `fuzzy jump` | fzf jump (z) |
| `zoxide jump` | zoxide jump (Z) | `new tab` / `tab next` / `tab last` | yazi tabs |
| `cancel` | Escape | `yazi help` | F1 |

## Git (community, `apps/git`)

| Say | Does |
|---|---|
| `git <command> [<arguments>]` | types `git <command>` and its arguments. Commands include: add, branch, checkout, cherry pick, clone, commit, diff, diff tool, fetch, grep, init, log, merge, move, pull, push, rebase, ref log, remote ..., reset, restore, revert, remove, show, stash ..., status, submodule ... |
| `git status` / `git diff` / `git diff cached` | run immediately |
| `git add patch` / `git show head` | run immediately |
| `git commit [<args>] message [<prose>]` | `git commit --message "..."` with the words inside the quotes |
| `git stash [push] [<args>] message [<prose>]` | stash with a message |
| `git add highlighted` / `git add clipboard` | add the selected / copied path |
| `git diff highlighted` / `git diff clipboard` | diff the selected / copied path |
| `git commit highlighted` | add the selected path and commit |
| `git clone clipboard` | clone the copied URL |

Also `anaconda ...` (conda commands: `anaconda environment list`, `anaconda activate`, ...) from the community setup.

## Windows Terminal

| Say | Does |
|---|---|
| `tab open` / `tab new` | new tab |
| `tab next` / `tab last` / `tab previous` | switch tab |
| `tab close` / `tab reopen` / `tab duplicate` | close / reopen / duplicate |
| `go tab <number>` / `go tab final` | jump to a tab |
| `split right|left|down|up` | split the pane |
| `split vertically` / `split horizontally` | split the pane (by orientation) |
| `split next` / `split last` / `go split <number>` | move between panes |
| `split max` / `split reset` / `split flip` / `split clear` | pane layout |
| `focus left|right|up|down` | move focus between panes |
| `settings open` / `term menu` | Terminal settings / menu |
| `find it [<phrase>]` | search in the terminal output |
| `clear screen` | clear the screen (Ctrl-L) |
| `kill all` | Ctrl-C (kolaf: the community version also typed `y` Enter, which would start yazi here) |

## Handy (kolaf/handy)

| Say | Does |
|---|---|
| `make that formal` / `informal` / `shorter` / `fuller` / `clearer` | rewrite the selected text, or the last dictation, and replace it |
| `fix that up` | spelling and grammar only |
| `translate that to norwegian` / `english` | translate and replace |
| `bullet that` / `summarize that` | bullet list / short summary |
| `edit this` | select text, say it, then speak the change you want ("shorter and friendlier, mention Thursday"); stop with your Handy key and the result replaces the selection |
| `model <name>` | switch Handy's speech model, e.g. `model parakeet`, `model norwegian`, `model whisper small` (edit `handy/models.talon-list`; the model must be downloaded) |
| `model picker` | numbered list of the downloaded models; say or press a number |
| `scratch that` / `nope that` | **context-aware** (kolaf/handy/scratch_that.py): takes back whichever put text on the screen last, Talon's own phrase or Handy's dictation, by comparing their times; repeat it to go further back |
| `scratch dictation` | delete the last dictation with Backspace presses (same window, at most 5 minutes old; works in terminals); use it right after dictating |
| `redo as email` / `message` / `note` / `meeting` / `document` / `formal` / `informal` / `simple` | process the last recording again with that prompt and replace the text |
| `reply to this` | copy the selected message, then dictate the reply (stop with your Handy key); Talon is quiet while Handy records |
| `learn this repo` | (in the terminal) add the project's names and terms to Handy's custom words |

## Hermes, the voice shell (kolaf/hv)

| Say | Does |
|---|---|
| `hermes <request>` | types `hv "<request>"`: Hermes plans the file/shell task and, for requests that change something, ends with "Go ahead?" |
| `hermes go` (also yes, go ahead, do it) | execute the plan |
| `hermes again <text>` | correct the plan |
| `hermes ask <text>` | read-only question |
| `hermes cancel` | cancel |
| `grab files` (in a file manager) | remember the selected files for the next `hermes ...` |

## General (kolaf/personal)

`drowse` puts Talon to sleep. `Ctrl+PageUp` toggles speech (the spoken wake words are switched off on purpose).

## Available in the community setup but switched off

- `core {unix_utility}` (type common Unix commands like grep, find, sed): tag `user.unix_utilities`.
- kubectl commands: tag `user.kubectl` in `windows_terminal.talon`.

## How it hangs together

- `terminal_state.py` reads the state file and builds the lists `kolaf_dir`, `kolaf_file`, `kolaf_jump`; it also switches
  on the yazi tag when the shell function `y` marks yazi as running.
- `terminal.talon`, `yazi.talon` hold the commands; `wsl.talon` makes this tab use the Linux flavour of the community
  terminal commands.
- To change a spoken word, edit the `.talon` file; Talon reloads it by itself.
