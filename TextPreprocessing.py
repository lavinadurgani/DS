import pandas as pd

import nltk

## Tokenizer class
from nltk.tokenize import RegexpTokenizer
regTokenizer = RegexpTokenizer(r"[a-zA-Z]+")

# Remove Contractions
import contractions

## Stopwords Class
#nltk.download('stopwords')
#from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')
extended = ["bad"]
stopwords.extend(extended)

## Stemming Class
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

## Lemmartizer Class and POS Tag
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
from nltk import pos_tag
from nltk.corpus import wordnet

def getWordnetPOS(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    if treebank_tag.startswith('V'):
        return wordnet.VERB
    if treebank_tag.startswith('N'):
        return wordnet.NOUN
    if treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
  

train_df = pd.read_csv(r'C:\Users\lavin\Documents\Practising Python\Kaggle_PCM_Subj_Textdata\train.csv')
train_df.head()

print(train_df.head())


#comments = train_df['Comment']
ContractionsRemoved = []
Tokens_NoStopWords = []
stemmed_Tokens = []
#tempPOSbasedLemmaList = []

for i in  train_df['Comment']:
    string = i.strip()
    #print(i)
    tempList = contractions.fix(string)
    ContractionsRemoved.append(tempList)
    
    tempList = regTokenizer.tokenize(i)
    #print(tempList)
    """ Tokenize just with space delimiter, no regex
    tempList = i.split()
    print(tempList)
    """

    tempList = [s.lower() for s in tempList]
    tempList = [s for s in tempList if s not in set(stopwords)]
    Tokens_NoStopWords.append(tempList)
    
    tempStemmedList = [ps.stem(s) for s in tempList]
    stemmed_Tokens.append(tempStemmedList)
    
    """
    tempPOSbasedLemmaList = [wnl.lemmatize(s[0] , pos = getWordnetPOS(s[1])) for s in pos_tag(tempList)]
    tempPOSbasedLemmaList.append(tempPOSbasedLemmaList)
    """
train_df['ContractionsRemoved'] = ContractionsRemoved
train_df['Tokens_NoStopWords'] = Tokens_NoStopWords
train_df['stemmed_Tokens'] = stemmed_Tokens
#train_df['tempPOSbasedLemmaList'] = tempPOSbasedLemmaList

train_df.head()

train_df.to_csv(r'preprocessed.csv')
