
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from flask import Flask, request, render_template

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from youtube_transcript_api import YouTubeTranscriptApi

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def send_form():
    return render_template('main.html', data="No video chosen!")

@app.route('/summary', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form

    return render_template('main.html', data = getSummary(form_data))

def getSummary(form_data):
    url = form_data['URL'].replace("https://www.youtube.com/watch?v=", "")
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(url)
    except:
        return "Error! Video not found!"
    transcript = transcript_list.find_transcript(['en']).fetch()
    t = ""
    for i,T in enumerate(transcript):
        t += T['text'] + " ";

    LANGUAGE = "english"
    SENTENCES_COUNT = form_data['num_sentences']

    parser = PlaintextParser.from_string(t, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = ""

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        summary+=str(sentence)+" "

    return summary
