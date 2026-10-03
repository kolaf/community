app: windows_terminal
-
# The folder the shell is in, its sub-folders and files, and zoxide's folders, are known through the state file
# (terminal_state.py). Say "folders" to see the numbered list.

terminal help: user.kolaf_terminal_help()
folders: user.kolaf_terminal_folders_toggle()
folders hide: user.kolaf_terminal_folders_toggle()

into <user.kolaf_dir>: user.kolaf_terminal_cd(kolaf_dir)
into numb <number_small>: user.kolaf_terminal_cd_number(number_small)
out of: user.kolaf_terminal_up(1)
out of <number_small>: user.kolaf_terminal_up(number_small)
pick <user.kolaf_dir>: user.kolaf_terminal_pick(kolaf_dir)
pick file <user.kolaf_file>: user.kolaf_terminal_pick(kolaf_file)

# zoxide: "jump dotfiles" goes to the best match; "jump list" opens its interactive picker (fzf)
jump list: insert("zi\n")
jump back: insert("z -\n")
jump <user.kolaf_jump>: user.kolaf_terminal_jump(kolaf_jump)
jump <user.text>: user.kolaf_terminal_jump(text)

# atuin: searchable shell history (Ctrl-R). Say the words to look for, then choose.
history [<user.text>]: user.kolaf_terminal_type_after("ctrl-r", text or "")
history list <user.text>: insert("atuin search --limit 15 {text}\n")
history last: insert("atuin search --limit 10\n")

# zoxide: what does it know?
jump show <user.text>: insert("zoxide query --list --score {text}\n")
jump show: insert("zoxide query --list --score | head -20\n")

# Choosing in fzf, atuin and other pickers that are open
choose it: key(enter)
edit it: key(tab)
result next: key(down)
result back: key(up)
result page: key(pagedown)
cancel search: key(escape)

# yazi, the file manager (the shell function y; follows you when you quit with q)
file browser: insert("y\n")
browse <user.kolaf_dir>: user.kolaf_terminal_browse(kolaf_dir)

# fzf key bindings (installed by the dotfiles playbook): fuzzy file, folder and history search
fuzzy file [<user.text>]:
    key(ctrl-t)
    sleep(150ms)
    insert(text or "")
fuzzy folder [<user.text>]:
    key(alt-c)
    sleep(150ms)
    insert(text or "")
fuzzy history [<user.text>]:
    key(ctrl-r)
    sleep(150ms)
    insert(text or "")
