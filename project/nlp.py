import re
import nltk
from nltk.stem import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def remove_tags(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    return clean_text

def stemmer(texts: list):
    """Функция принимающая список текстов и возвращающая его после стемминга
    texts - исходный текст
    stem_texts - список лемматизированных текстов
    """
    porter_stemmer = PorterStemmer()
    stem_texts = []
    stop_words = set(stopwords.words('english') + ['•', 's', "n't", "'s", '.', ',', "''", '--', '-', "``", '“', '”', '(', ')', ':', ';', '!', '?', '/', '%', '&', '@', '#', '…', '...', '’', '....']) 
    for text in texts:
        text = text.lower()
        cleaned_text = remove_tags(text)
        nltk_tokens = word_tokenize(cleaned_text)
        filtered_tokens = [word for word in nltk_tokens if word not in stop_words]
        line = ''
        for word in filtered_tokens:
            line += ' ' + porter_stemmer.stem(word)
        stem_texts.append(line)
    return stem_texts