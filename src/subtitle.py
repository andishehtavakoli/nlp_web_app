import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import json
import pysrt
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from utils import read_json


class Subtitle():
    def __init__(self, subtitle_path):
        self.word_difficulty = read_json('word_difficulty.json')
        subtitle = pysrt.open(subtitle_path, encoding='cp1252')
        self.subtitle_text = ' '.join([i.text for i in subtitle])

    def __clean_text(self, text):

        text = text.lower()
        word_list = [item for item in word_tokenize(text) \
                     if item not in stopwords.words('english') \
                     and (item not in string.punctuation) \
                     and (len(item) > 3) \
                     and item.isalpha()]

        return word_list


    def get_difficult_words(self, score):

        clean_sub = self.__clean_text(self.subtitle_text)
        difficult_words = []
        for word in clean_sub:
            if word in self.word_difficulty.keys():

                if self.word_difficulty[word] > score:
                    difficult_words.append(word)
        return set(difficult_words)
