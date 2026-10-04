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

# "scratch that" itself is context-aware (scratch_that.py): it takes back whichever came last, a Talon phrase or a Handy
# dictation. "scratch dictation" below always means Handy's.
# Speech model: "model parakeet", "model norwegian" ... (edit models.talon-list; the value only has to be part of the model's
# name or id, and the model must be downloaded). "model picker" shows a numbered list.
model <user.kolaf_handy_model>: user.kolaf_handy_set_model(kolaf_handy_model)
model picker: user.kolaf_handy_model_picker()

# Meeting minutes from the latest recording in the recorder's folder (OBS Studio...; set the folder on Handy's Meetings page).
# "meeting" takes the files that belong together (OBS splits long recordings), "recording" only the newest file. Works
# anywhere, on Windows and Linux. Refuses while the newest file is still being written.
transcribe latest meeting: user.kolaf_handy_transcribe_latest(false)
transcribe latest recording: user.kolaf_handy_transcribe_latest(true)

# Start a dictation in a given mode: "dictate as email", "dictate as message", "dictate as note" ... (the names are in
# prompts.talon-list). Talon is quiet while Handy records; stop with your Handy key. No text is copied first (for that,
# "reply to this" and "edit this" copy the selection).
dictate as <user.kolaf_handy_prompt>: user.kolaf_handy_dictate_as(kolaf_handy_prompt)

# Undo and redo the last dictation. Like the community "scratch that" this presses Backspace once per character, but only
# when Handy pasted it in the window that has focus, at most 5 minutes ago; it works in terminals too. Use it right after
# dictating: Handy cannot see whether you moved the cursor. "redo as" processes the original recording again.
scratch dictation: user.kolaf_handy_scratch()
redo as <user.kolaf_handy_prompt>: user.kolaf_handy_redo(kolaf_handy_prompt)
redo raw: user.kolaf_handy_redo("raw")

# Select a message, say this, then dictate the reply. Talon switches itself off while Handy records; stop with your
# Handy key, and the reply (shaped by the reply prompt, with the message as context) is pasted.
reply to this: user.kolaf_handy_dictate_with("reply")

# Select text, say this, then speak what to change ("shorter and friendlier, mention Thursday"). Stop with your Handy
# key; the result replaces the selection. For free-form changes; the fixed "make that ..." commands above are faster.
edit this: user.kolaf_handy_dictate_with("edit")
