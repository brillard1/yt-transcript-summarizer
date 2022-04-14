# SummarYT
People are watching YouTube videos daily which can be educational, documentary or of any genre with longer length; think about how much time can be saved by creating summarized content. In this project, we performed NLP and generate summarized version of YouTube transcript using Python libraries. We deployed a web applciation for the same.<br><br>
The URL is taken as input from the user. If the input URL is invalid or the transcript of the video does not exists then an error message will be displayed. The transcript is extracted from the given video using a Python library then feed it to summarizer to get the summary. The lengths of the summary can me tuned with the sliding bar from which the number of sentences can be varied from 1 to 51. The website is deployed on heroku platform using the flask framework.<br><br>
For development purposes, follow the given steps:
<ul>
<li>Clone the repository using <code>git clone https://github.com/sawmill811/yt-transcript-summarizer.git</code></li>
  <li>Create a file named <code>.env</code> with the content:
<ul>
<li><code>
FLASK_APP=app.py
FLASK_ENV=development
  </code>
</li>
</ul>
</li>
  <li>Now to run the command <code>flask run</code> to run the app in development mode.</li>
</ul>
