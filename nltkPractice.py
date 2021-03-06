
from bs4 import BeautifulSoup
# print(soup.prettify())
import pandas as pd
import nltk

from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer, word_tokenize

# Whoa wordnet is awesome!
from nltk.corpus import wordnet
from nltk.corpus import stopwords

from textblob import TextBlob

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')


# Note: cannot name file "nltk.py"

syns = wordnet.synsets('program')

# print(syns)
#
# print(syns[0].name())
# print(syns[0].lemmas()[0].name())
# print(syns[0].definition())
# print(syns[0].examples())

synonyms = []
antonyms = []

# for syn in wordnet.synsets('good'):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
#
# print(set(synonyms))
# print(set(antonyms))

allCsvs = [
'AllsWellThatEndsWell',
'AntonyandCleopatra',
'AsYouLikeIt',
'ComedyofErrors',
'Coriolanus',
'Cymbeline',
'Hamlet',
'HenryIV,part1',
'HenryIV,part2',
'HenryV',
'HenryVI,part1',
'HenryVI,part2',
'HenryVIII',
'JuliusCaesar',
'KingJohn',
'KingLear',
'LovesLaboursLost',
'Macbeth',
'MeasureforMeasure',
'MerchantofVenice',
'MerryWivesofWindsor',
'MidsummerNightsDream',
'MuchAdoAboutNothing',
'Othello',
'Pericles',
'RichardII',
'RichardIII',
'RomeoandJuliet',
'TamingoftheShrew',
'TheTempest',
'TimonofAthens',
'TitusAndronicus',
'TroilesandCressida',
'TwelfthNight',
'TwoGentlemenofVerona',
'WintersTale'
]

dataframes = []
# main_df = pd.read_csv('csvs/AllsWellThatEndsWell.csv', index_col=0)
# main_df.set_index("LineNos", inplace=True)

blob = ''
blobs = []
filteredBlobs = []
taggedWords = []
moreBlobs = []
sentiments = []
allData = []

# Unfortunate that we had to resort to textblob, couldn't get nltk sentiment working.
for i, csv in enumerate(allCsvs):
    filename = 'csvs/' + csv + '.csv'
    df = pd.read_csv(filename, index_col=0)

    # df.set_index("LineNos", inplace=True)

    # print(df.head(5))
    dataframes.append(df)
    # main_df.join(df, lsuffix="_left", rsuffix="_right")
    # print(df["Lines"][2:22])
    # print("\n")

    # Gonna go through ALL of each play!
    for line in df["Lines"][2:]:
        blob += line
        blob += ' '

    blobs.append(blob)

    realBlob = TextBlob(blob)
    sentiments.append(realBlob.sentiment.polarity)
    data = { 'sentiment': 0, 'play': ''}
    data['sentiment'] = realBlob.sentiment.polarity
    data['play'] = allCsvs[i]
    allData.append(data)

    moreBlobs.append(realBlob)
    blob = ''

# print(blobs)
# print(moreBlobs)
# print(sentiments)
# print(allData)



fig, ax1 = plt.subplots(1,1)
fig.subplots_adjust(bottom=0.2)

y_pos = np.arange(len(allCsvs))

ax = plt.bar(y_pos, sentiments, align='center', alpha=0.5)
plt.xticks(y_pos, allCsvs, rotation='vertical')
plt.ylabel('Sentiment')
plt.title('Sentiment of All of each Play')

ax1.set_xticklabels(allCsvs, {'rotation':80, 'fontsize':8})


plt.show()


# stop_words = set(stopwords.words('english'))
#
# for blob in blobs:
#     word_tokens = word_tokenize(blob)
#     tagged = nltk.pos_tag(word_tokens)
#     filtered_blob = [w for w in word_tokens if not w in stop_words]
#     filteredBlobs.append(filtered_blob)
#     taggedWords.append(tagged)

# print(filteredBlobs)
# Adds part of speech tag:
# print(taggedWords)










# chillin
