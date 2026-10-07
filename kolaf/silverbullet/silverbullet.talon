tag: browser
-
# SilverBullet in the browser. Every command starts with "silver": the commands are active in all browser tabs, because SilverBullet's tab titles
# are only page names. The keys are SilverBullet's defaults (Mod = Ctrl); see README.md for the list. Commands without a default key go through the
# command palette ("silver run <command name>").

# ---- finding and moving around
silver page$: key(ctrl-k)
silver open <user.text>$: user.kolaf_silverbullet_open_page(text)
silver meta picker$: key(ctrl-shift-k)
silver tag picker$: key(ctrl-alt-t)
silver tree$: key(ctrl-o)
silver graph$: key(ctrl-shift-g)
silver commands$: key(ctrl-/)
silver run <user.text>$: user.kolaf_silverbullet_run(text)
silver find$: key(ctrl-f)
# "Ctrl-g h" is in the documentation but did not work in a test (CodeMirror uses Ctrl-g for search), so the command goes through the palette
silver home$: user.kolaf_silverbullet_run("Navigate: Home")
silver back$: key(alt-left)
silver forward$: key(alt-right)
silver follow link$: key(ctrl-enter)
silver create page$: key(ctrl-shift-enter)
silver settings$: key(ctrl-,)
silver tab$: user.kolaf_silverbullet_focus()

# ---- journal and quick notes
silver journal today$: key(ctrl-q j)
silver journal previous$: key(ctrl-q p)
silver journal next$: key(ctrl-q n)
silver quick note$: key(ctrl-q q)
silver from template$: key(ctrl-q t)

# ---- writing
silver bold$: key(ctrl-b)
silver italic$: key(ctrl-i)
silver strike through$: key(ctrl-shift-s)
silver quote$: key(ctrl-shift-.)
silver make list$: key(ctrl-shift-8)
silver marker$: key(ctrl-alt-m)
silver comment$: key(ctrl-alt-c)
silver delete line$: key(ctrl-d)
silver indent$: key(tab)
silver outdent$: key(shift-tab)
silver center cursor$: key(ctrl-alt-l)

# ---- tasks and outline
silver task$: key(ctrl-. t)
silver move up$: key(alt-up)
silver move down$: key(alt-down)
silver move left$: key(ctrl-. h)
silver move right$: key(ctrl-. l)
silver fold$: key(ctrl-. ctrl-.)

# ---- pages (no default key: through the command palette)
silver rename page$: user.kolaf_silverbullet_run("Page: Rename")
silver delete page$: user.kolaf_silverbullet_run("Page: Delete")
silver copy page$: user.kolaf_silverbullet_run("Page: Copy")

# ---- system
silver export$: key(ctrl-e)
silver reload$: key(ctrl-alt-r)
