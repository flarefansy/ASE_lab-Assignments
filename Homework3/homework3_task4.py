# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:11:23 2017

@author: Spencersun
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag
import re, collections

#Read the file
input_tokenizer = nltk.data.load('input.txt')
sentences = sent_tokenize(input_tokenizer)
words = word_tokenize(input_tokenizer)

#Lemmatization on the remaining words
lemmatizer = WordNetLemmatizer()
Lemmatization_words = []
for i in range(len(words)):
    output_lemmatizer = lemmatizer.lemmatize(words[i])
    Lemmatization_words.append(output_lemmatizer)
print (Lemmatization_words)

#Remove all the verbs
word_tags = {}
word_tags.update(pos_tag(words))
delete_words = []
for key in word_tags:
    if (word_tags[key] == 'VBD') or (word_tags[key] == 'VBZ') or (word_tags[key] == 'VBG'):
        delete_words.append(key) 
for i in range(len(delete_words)):
    word_tags.pop(delete_words[i])
print (word_tags)
words = list(word_tags.keys())
print (words)

#Calculate the word frequency of the remaining words
while '.' in words:
    words.remove('.')
while ',' in words:
    words.remove(',')
word_count = collections.Counter(words)
print (word_count)

#Choose top five words that has been repeated
repeated_word = word_count.most_common(5)
print (repeated_word)

#Find all the sentences with those most repeated words
repeat_sen = []
for i in range(len(repeated_word)):
    for j in range(len(sentences)):
        if repeated_word[i][0] in sentences[j]:
            repeat_sen.append(sentences[j])
print (set(repeat_sen))
            