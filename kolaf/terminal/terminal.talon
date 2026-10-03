app: windows_terminal
-
# The folder the shell is in, its sub-folders and files, and zoxide's folders, are known through the state file
# (terminal_state.py). Say "folders" to see the numbered list.

folders: user.kolaf_terminal_folders_toggle()
folders hide: user.kolaf_terminal_folders_toggle()

into <user.kolaf_dir>: user.kolaf_terminal_cd(kolaf_dir)
into numb <number_small>: user.kolaf_terminal_cd_number(number_small)
pick <user.kolaf_dir>: user.kolaf_terminal_pick(kolaf_dir)
pick file <user.kolaf_file>: user.kolaf_terminal_pick(kolaf_file)

# zoxide: "jump dotfiles" goes to the best match; "jump list" opens its interactive picker (fzf)
jump list: insert("zi\n")
jump back: insert("z -\n")
jump <user.kolaf_jump>: user.kolaf_terminal_jump(kolaf_jump)
jump <user.text>: user.kolaf_terminal_jump(text)

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
