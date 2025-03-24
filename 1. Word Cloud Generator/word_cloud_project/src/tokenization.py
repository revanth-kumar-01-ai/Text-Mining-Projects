from nltk.tokenize import word_tokenize 
from nltk.util import ngrams
from collections import Counter

def uniTokenization(textData):
    joined_text = " ".join(textData)
    tokenize = word_tokenize(joined_text)
    return tokenize

def biGramTokenization(textData):
    bigrams = list(ngrams(textData, 2))
    bigram_phrases = [" ".join(bigram) for bigram in bigrams]
    bigram_freq = Counter(bigram_phrases)
    return bigram_freq