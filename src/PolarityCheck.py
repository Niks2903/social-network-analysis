import nltk as nltk
import json
import textblob
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords


class PolarityCheck:

    def clean_data(self):
        tweets = []
        for line in open("tweets.txt", "r"):
            tweets.append(json.loads(line))
        return tweets

    def check_polarity(self, tweets):
        a = 0.0
        for tweet in tweets:
            tokens = word_tokenize(tweet["text"])
            tokens = [w.lower() for w in tokens]
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in tokens]
            words = [word for word in stripped if word.isalpha()]
            stop_words = set(stopwords.words('english'))
            stop_words.add("rt")
            stop_words.add("https")
            words = [w for w in words if not w in stop_words]
            sentence = ''.join(str(e)+" " for e in words)
            text = textblob.TextBlob(sentence)
            text_full_sentence = textblob.TextBlob(tweet["text"])
            polarity = text.sentiment.polarity
            polarity_full_sentence = text_full_sentence.sentiment.polarity
            print("", sentence, polarity)
            print(tweet["text"], polarity_full_sentence)
            a = a + abs(polarity-polarity_full_sentence)
        print("Polarity Differencee", a)


if __name__ == "__main__":
    polarity_check = PolarityCheck()
    tweets = polarity_check.clean_data()
    polarity_check.check_polarity(tweets)
