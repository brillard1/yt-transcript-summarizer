# yt-transcript-summarizer

People are watching YouTube videos daily which can be educational, documentary or of any genre with longer length; think about how much time can be saved by creating summarized content. In this project, you will be a creating a Chrome Extension which will make a request to backend REST API where it will perform NLP and respond with a summarized version of a YouTube transcript.


Plan:
make a minimaslistic website that has a text field with the message (Enter youtube URL and hit enter) along with a short description of what it does below the text field
when the user presses enter shrink the text field vertically first then horizontally and add a processing symbol (probably await in JS? idk)
now idk how to implement actual backend but we have to first use a library/api to get transcript for that video then feed it to summarizer and get the summary
then show the title of video, channel name, views, likes, dislikes along with the summary.
except the title, and summary keep everything in a side content box (less distractive)
