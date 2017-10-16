# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:09:12 2017

@author: Spencersun
"""

import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.util import ngrams
from nltk import ne_chunk

synsets = wn.synsets('car')
print (synsets)

#input_tokenizer = nltk.data.load('input.txt')
input_tokenizer = "hello world, Tim"
sentences = sent_tokenize(input_tokenizer)
print (sentences)

#words = [word_tokenize(t) for t in sentences]
words = word_tokenize(input_tokenizer)
print (words)

stemmer = SnowballStemmer('english')
output_stemmer = stemmer.stem('eating')
print (output_stemmer)

output_POStags = []
for tokens in words:
    output_POStags.append(nltk.pos_tag(tokens))
print (output_POStags)

lemmatizer = WordNetLemmatizer()
output_lemmatizer = lemmatizer.lemmatize('walked', pos='v')
print (output_lemmatizer)

trigrams = list(ngrams(words,2))
print (trigrams)

NER = ne_chunk(pos_tag(wordpunct_tokenize(input_tokenizer)))
print (NER)
