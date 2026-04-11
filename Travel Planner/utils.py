import re
import string

stopwords = {
    "is", "the", "a", "an", "and", "or", "in", "on", "at",
    "to", "for", "of", "with", "by", "what", "how", "why"
}

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = re.findall(r'\b\w+\b', text)
    tokens = [word for word in tokens if word not in stopwords]
    return tokens
