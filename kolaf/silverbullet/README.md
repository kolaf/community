# Voice control of SilverBullet (kolaf/silverbullet)

Talon commands for [SilverBullet](https://silverbullet.md) in the web browser. SilverBullet's tabs cannot be told apart from other tabs (the tab
title is only the page name), so the commands are active in every browser and **all start with "silver"**. They send SilverBullet's own default
keyboard shortcuts (Windows and Linux: `Mod` = Ctrl; macOS uses Cmd and is not covered). Commands for actions without a default key go through the
command palette. If you changed a shortcut in SilverBullet (Configuration Manager), change it in `silverbullet.talon` too.

Optional settings (in your `settings.talon`): `user.kolaf_silverbullet_url = "http://host:3000/notes"` for "silver tab" (needs Rango).

**Checked** means the key was sent to a real SilverBullet 2.12.0 in a headless Chrome and did what the command says; the others come from SilverBullet's
source code and documentation and have not been tried.

| Say | Key (or palette command) | Does | |
|---|---|---|---|
| `silver page` | Ctrl-k | page picker | checked |
| `silver open <text>` | Ctrl-k, text, Enter | open (or create) that page | |
| `silver meta picker` | Ctrl-Shift-k | picker for meta pages | checked |
| `silver tag picker` | Ctrl-Alt-t | picker for tags | checked |
| `silver commands` | Ctrl-/ | command palette | checked |
| `silver run <text>` | Ctrl-/, text, Enter | run a command by name | |
| `silver home` | palette "Navigate: Home" | the index page | checked |
| `silver back` / `silver forward` | Alt-Left / Alt-Right | history | |
| `silver find` | Ctrl-f | find in page | |
| `silver tree` | Ctrl-o | page tree | |
| `silver graph` | Ctrl-Shift-g | graph explorer | |
| `silver follow link` | Ctrl-Enter | go to the page under the cursor | |
| `silver create page` | Ctrl-Shift-Enter | create the page under the cursor | |
| `silver settings` | Ctrl-, | Configuration Manager | |
| `silver tab` | (Rango) | switch to the SilverBullet tab / open it | |
| `silver journal today` | Ctrl-q j | today's journal page | checked |
| `silver journal previous` | Ctrl-q p | previous journal page | checked |
| `silver journal next` | Ctrl-q n | next journal page | |
| `silver quick note` | Ctrl-q q | new quick note | checked |
| `silver from template` | Ctrl-q t | page from template | |
| `silver bold` / `italic` | Ctrl-b / Ctrl-i | formatting of the selection | checked |
| `silver strike through` | Ctrl-Shift-s | strikethrough | checked |
| `silver quote` | Ctrl-Shift-. | quote the selection | not working in the test |
| `silver make list` | Ctrl-Shift-8 | turn the selection into a list | partly (the key was received) |
| `silver marker` | Ctrl-Alt-m | marker | |
| `silver comment` | Ctrl-Alt-c | add a comment | |
| `silver delete line` | Ctrl-d | delete the line | checked |
| `silver indent` / `silver outdent` | Tab / Shift-Tab | indent | indent checked |
| `silver center cursor` | Ctrl-Alt-l | scroll the cursor to the middle | |
| `silver task` | Ctrl-. t | cycle the state of the task under the cursor | did not change the task in the test |
| `silver move up` / `down` | Alt-Up / Alt-Down | move the outline item | |
| `silver move left` / `right` | Ctrl-. h / Ctrl-. l | outdent / indent the outline item | |
| `silver fold` | Ctrl-. Ctrl-. | fold or unfold | |
| `silver rename page` / `delete page` / `copy page` | palette "Page: Rename" ... | no default key | |
| `silver export` | Ctrl-e | export page or selection | |
| `silver reload` | Ctrl-Alt-r | System: Reload (after changing templates or scripts) | |

Handy's own commands work in SilverBullet as everywhere: "update journal" dictates into today's journal, "edit this" rewrites the selection.
Not included: Ctrl-n (a new browser window is the browser's), Ctrl-p (print), and the cursor and selection keys, which the community commands already
send in any editor.
