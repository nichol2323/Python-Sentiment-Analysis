from textblob import TextBlob
from newspaper import Article
import nltk
# nltk.download('punkt')


with open('text.txt', 'r') as f:
    text = f.read()


# url = 'https://en.wikipedia.org/wiki/World_War_II'
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()
# text = article.summary


blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(blob, '\n', sentiment)