

################### SENTIMENT ANALYSIS using VADER ######
"""
VADER
VADER (Valence Aware Dictionary and Sentiment Reasoner) functions beyond word-level. Instead, it analyzes sentiment on the sentence-level/content-level. Moreover, it provides both polarity (positive/negative) and intensity of emotions. In Python vaderSentiment library, it returns 4 scores— positive, negative, neutral, and compound.
"""

# -*- coding: utf-8 -*-
import pandas as pd

train_df = pd.read_csv(r'preprocessed.csv')
train_df.head()

import nltk
nltk.download('punkt')

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer() 
pos=neg=neu=compound=0
sentences =[nltk.sent_tokenize(text.lower()) for text in train_df['stemmed_Tokens']]

for sentence in sentences:
    print(sentences)
    vs = analyzer.polarity_scores(sentence)
    pos += vs["pos"]/len(sentences)
    neg += vs["neg"]/len(sentences)
    neu += vs["neu"]/len(sentences)
    compound += vs["compound"]/len(sentences)
    

