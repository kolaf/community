-
# Voice transforms: they work on the selected text, or, when nothing is selected, on the last dictation Handy pasted
# (same window, at most 5 minutes old; it is taken back with Backspace presses like "scratch that"). The result replaces it.
make that formal: user.kolaf_handy_transform("t_formal")
make that informal: user.kolaf_handy_transform("t_informal")
make that shorter: user.kolaf_handy_transform("t_shorter")
make that fuller: user.kolaf_handy_transform("t_longer")
make that clearer: user.kolaf_handy_transform("t_clear")
fix that up: user.kolaf_handy_transform("t_fix")
translate that to norwegian: user.kolaf_handy_transform("t_to_no")
translate that to english: user.kolaf_handy_transform("t_to_en")
bullet that: user.kolaf_handy_transform("t_bullets")
summarize that: user.kolaf_handy_transform("t_summary")

# Undo and redo the last dictation. Like the community "scratch that" this presses Backspace once per character, but only
# when Handy pasted it in the window that has focus, at most 5 minutes ago; it works in terminals too. Use it right after
# dictating: Handy cannot see whether you moved the cursor. "redo as" processes the original recording again.
scratch dictation: user.kolaf_handy_scratch()
redo as <user.kolaf_handy_prompt>: user.kolaf_handy_redo(kolaf_handy_prompt)

# Select a message, say this, then dictate the reply. Talon switches itself off while Handy records; stop with your
# Handy key, and the reply (shaped by the reply prompt, with the message as context) is pasted.
reply to this: user.kolaf_handy_dictate_with("reply")

# Select text, say this, then speak what to change ("shorter and friendlier, mention Thursday"). Stop with your Handy
# key; the result replaces the selection. For free-form changes; the fixed "make that ..." commands above are faster.
edit this: user.kolaf_handy_dictate_with("edit")
