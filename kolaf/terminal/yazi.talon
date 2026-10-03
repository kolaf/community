tag: user.kolaf_yazi
app: windows_terminal
-
# Commands for the yazi file manager (started with "file browser" or "browse <folder>"). They are only active while
# yazi runs, which the shell wrapper tells Talon. Keys are yazi's default keymap; press F1 inside yazi to see them.

# moving
up [<number_small>]: user.kolaf_terminal_press("k", number_small or 1)
down [<number_small>]: user.kolaf_terminal_press("j", number_small or 1)
parent: key(h)
open it: key(l)
history back: key(shift-h)
history forward: key(shift-l)
top: key(g g)
bottom: key(shift-g)
page down: key(ctrl-d)
page up: key(ctrl-u)

# selecting and file operations
select: key(space)
select all: key(ctrl-a)
visual mode: key(v)
copy it: key(y)
cut it: key(x)
paste it: key(p)
paste over: key(shift-p)
trash it: key(d)
rename it: key(r)
create [<user.text>]: user.kolaf_terminal_type_after("a", text or "")
toggle hidden: key(.)
copy path: key(c c)
copy name: key(c f)

# finding and jumping
find <user.text>: user.kolaf_terminal_type_after("/", text, true)
search name <user.text>: user.kolaf_terminal_type_after("s", text, true)
search content <user.text>: user.kolaf_terminal_type_after("S", text, true)
next match: key(n)
previous match: key(shift-n)
fuzzy jump: key(z)
zoxide jump: key(shift-z)

# tabs, help, leaving
new tab: key(t)
tab next: key(])
tab last: key([)
yazi help: key(f1)
quit yazi: key(q)
quit here: key(shift-q)
cancel: key(escape)
