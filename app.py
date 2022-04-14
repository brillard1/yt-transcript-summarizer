
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# Flask imports
from flask import Flask, request, render_template

# Summarizer
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# YouTube Transcript API
from youtube_transcript_api import YouTubeTranscriptApi

# Flask local environment
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Landing Page
@app.route('/', methods=['GET','POST'])
def send_form():
    return render_template('main.html', data="No video chosen!")

# Summary Page
@app.route('/summary', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form

    return render_template('main.html', data = getSummary(form_data))

# Function to generate summary of transcript
def getSummary(form_data):

    # Handling both types of URL inputs

    url1 = form_data['URL'].replace("https://www.youtube.com/watch?v=", "")
    url2 = form_data['URL'].replace("https://youtu.be/", "")

    # Trying to get transcript using first type of URL
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(url1)
    except:
        # If the above fails, we use the second type of URL
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(url2)
        except:
            # If both types of URL fail, we return an error message
            return "Error! Video not found!"

    # Extracting English transcript from the list of transcripts

    transcript = transcript_list.find_transcript(['en']).fetch()
    t = ""
    for i,T in enumerate(transcript):
        t += T['text'] + " ";

    LANGUAGE = "english"
    SENTENCES_COUNT = form_data['num_sentences']

    # Generating summary

    parser = PlaintextParser.from_string(t, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = ""

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        summary+=str(sentence)+" "

    return summary
