import re
import string

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


factory_stopword = StopWordRemoverFactory()
stopword_remover = factory_stopword.create_stop_word_remover()

factory_stemmer = StemmerFactory()
stemmer = factory_stemmer.create_stemmer()

CUSTOM_STOPWORDS = [
    "sangat",
    "banget",
    "bgt",
    "lumayan",
    "mantap",
    "tempat",
    "wisata",
    "rekomendasi",
    "recommended",
    "recommend",
    "bagus",
    "baik",
    "cukup",
    "sekali",
    "benar",
    "keren",
    "oke",
    "ok",
    "mantul",
    "sip"
]

def preprocess_text(text):
    """
    Lowercase
    Remove punctuation
    Remove angka
    Stopword removal
    Stemming
    """

    text = str(text).lower()

    text = re.sub(r'\d+', '', text)

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    text = stopword_remover.remove(text)
    for word in CUSTOM_STOPWORDS:
        text = text.replace(word, " ")

    text = stemmer.stem(text)

    text = re.sub(r'\s+', ' ', text).strip()

    return text