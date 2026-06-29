import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize



try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet", quiet=True)



lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))



def preprocess_text(text):

   
    text = text.lower()

    
    text = text.translate(str.maketrans("", "", string.punctuation))

    
    text = re.sub(r"\d+", "", text)

    
    words = word_tokenize(text)

    
    processed_words = []

    for word in words:
        if word not in stop_words and len(word) > 2:
            processed_words.append(lemmatizer.lemmatize(word))

    return " ".join(processed_words)

if __name__ == "__main__":

    sentence = "What is Artificial Intelligence?"

    print("Original :", sentence)
    print("Processed:", preprocess_text(sentence))