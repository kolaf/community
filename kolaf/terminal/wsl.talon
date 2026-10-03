app: windows_terminal
title: /ubuntu|wsl|@/i
-
# This Windows Terminal tab is a WSL (Ubuntu) shell: use the Linux flavour of the community terminal commands
# (lisa all = ls -a, clear screen = Ctrl-L, ...) instead of the PowerShell flavour that windows_terminal.talon enables.
tag(): user.wsl

# The community "go <system path>" and "path <system path>" use Windows folders (Desktop, Documents ...), which mean
# nothing in a Linux shell. Here the same words use the folders zoxide knows instead: "go airsports" jumps there,
# "path airsports" types its full path, quoted.
go <user.system_path>: skip()
path <user.system_path>: skip()
go <user.kolaf_jump>: user.kolaf_terminal_jump(kolaf_jump)
path <user.kolaf_jump>: user.kolaf_terminal_path(kolaf_jump)
