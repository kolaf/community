app: windows_explorer
app: windows_file_browser
-
# Select the audio file(s) of a meeting in Explorer (or a folder with its parts), then say this. Handy transcribes them
# with a local speech model, writes the minutes with the post-processing model, saves them in the meeting_notes folder and
# opens them. Progress is on Handy's Meetings page. The language defaults to the one set on that page.
transcribe meeting: user.kolaf_handy_transcribe_selected("")
transcribe meeting norwegian: user.kolaf_handy_transcribe_selected("no")
transcribe meeting english: user.kolaf_handy_transcribe_selected("en")
