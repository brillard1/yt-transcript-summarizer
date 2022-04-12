from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals



from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from youtube_transcript_api import YouTubeTranscriptApi


url = input("Enter the url of the video:").replace("https://www.youtube.com/watch?v=","")
transcript_list = YouTubeTranscriptApi.list_transcripts(url)
transcript = transcript_list.find_transcript(['en']).fetch()
t = ""
for i,T in enumerate(transcript):
    t += T['text'] + " ";

LANGUAGE = "english"
SENTENCES_COUNT = int(input("Enter number of sentences:"))

if __name__ == "__main__":
    parser = PlaintextParser.from_string(t, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)

