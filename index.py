
# Next steps: put into DB, and run some NLTK analyses

import urllib.request, urllib.error
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
# print(soup.prettify())
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')

# Holds urls:
allPlays = []
# Holds all strings:
allStrings = []
allSpeakers = []
allText = []
allDictionaries = []

# For our chart of number of lines per speaker:
speakers = []
counts = []

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



# Master dictionary:
# Example items will be {"speaker": "King Lear", }
masterList = []

# Whoops, dataframe wants object of arrays, not vice versa:
masterDict = dict()
masterDict['Speakers'] = []
masterDict['Lines'] = []
masterDict['LineNos'] = []

speakerCounts = []
currentSpeaker = ''
currentCount = 0

speakersDict = dict()

shakespeare = 'http://shakespeare.mit.edu/'
page = urllib.request.urlopen(shakespeare)
soup = BeautifulSoup(page, "html5lib")

all_links = (soup.find_all('a'))

def generateLinks():
    for pos, link in enumerate(all_links):
        # print(link.get("href"))
        href = link.get("href")
        ind = href.find("/")
        if pos > 1 and pos < len(all_links) - 7:
            if not ind == -1:
                # print(link.get("href")[0 : ind])
                url = 'http://shakespeare.mit.edu/' + href[0 : ind] + '/full.html'
                allPlays.append(url)


generateLinks()

def getPlay(x):
    # Clear everything out in case we're getting multiple plays:
    speakersDict = dict()
    allStrings = []

    # Need to get rid of this in order to not clear it out before we can print it:
    # allText = []

    global currentCount
    currentCount = 0
    global currentSpeaker
    currentSpeaker = ''
    global allDictionaries

    # There must be a cleaner way to do this:
    for ind, play in enumerate(allPlays):
        if ind == x:
            page = urllib.request.urlopen(play)
            soup2 = BeautifulSoup(page, "html5lib")
            allStrings = soup2.findAll('a')

    # Prints out all the strings (list of lines or speakers):
    # for s in allStrings:
    #     print(s)
    #     print('\n')

    for s in allStrings:
        # We have a new speaker:
        if (str(s)[9] == 's'):
            ind = str(s).find('b>') + 2
            end = str(s).find('</')
            allSpeakers.append(str(s)[ind : end])

            # Switch to new speaker:
            oldSpeaker = currentSpeaker

            # Do we already have this speaker?
            if oldSpeaker in speakersDict:
                speakersDict[oldSpeaker] += currentCount
            else:
                speakersDict[oldSpeaker] = currentCount

            currentSpeaker = str(s)[ind : end]
            currentCount = 0

        # We have a line:
        else:
            ind = str(s).find('">') + 2
            end = str(s).find('</')

            ind2 = str(s).find('="')
            data = {}
            # Odd we couldn't use dot notation here:
            data['line'] = str(s)[ind:end]
            data['lineNo'] = str(s)[ind2 + 2:ind - 2]
            allText.append(data)

            # Add to master list for dataframe:
            # dataObj = dict()
            # dataObj["speaker"] = currentSpeaker
            # dataObj["line"] = str(s)[ind: end]
            # dataObj["lineNo"] = str(s)[ind2 + 2: ind - 2]
            #
            # masterList.append(dataObj)

            # Whoops, pandas wants an object of arrays, not an array of objects:
            masterDict['Speakers'].append(currentSpeaker)
            masterDict['Lines'].append(str(s)[ind: end])
            masterDict['LineNos'].append(str(s)[ind2 + 2: ind - 2])


            # Increment current speaker's count:
            currentCount = currentCount + 1
    # AHA!  We had this inside the for loop!!!!
    allDictionaries.append(speakersDict)

# getPlay(32)
#
# # clear it out:
# masterDict = dict()
# masterDict['Speakers'] = []
# masterDict['Lines'] = []
# masterDict['LineNos'] = []
# getPlay(31)
#
# # print(masterList)
# # print(allText)
#
# # print(masterDict)
#
# df = pd.DataFrame(masterDict)
#
# print(df.head(2))
#
# print(df['Lines'][1])




# Awesome, this generates all our csvs:
# for i in range(0, 37):
#     masterDict = dict()
#     masterDict['Speakers'] = []
#     masterDict['Lines'] = []
#     masterDict['LineNos'] = []
#
#     getPlay(i)
#
#     df = pd.DataFrame(masterDict)
#     # print(df['Lines'][1])
#
#     name = ''
#     for c in df['Lines'][1]:
#         if c != ' ' and c != "'":
#             name += c
#     print(name)
#
#     name += '.csv'
#
#     df.to_csv(name)


# df = pd.read_csv('csvs/KingLear.csv', index_col=0)
# print(df.head(10))


# df.to_csv('macbeth.csv')



# df = pd.read_csv('macbeth.csv', index_col=0)
#
# print(df.head(10))


for csv in allCsvs:
    filename = 'csvs/' + csv + '.csv'
    df = pd.read_csv(filename, index_col=0)
    print(df.head(5))



# for x in range(38):
#     getPlay(x)

# print(len(allText))
# print(allText)
# print(allDictionaries)

# for d in allDictionaries:
#     print(d)
#     print('\n')


# print(allDictionaries[0]['LEAR'])


# Preparing our chart:
# for key in allDictionaries[0]:
#     speakers.append(key)
#     counts.append(allDictionaries[0][key])
#
# # print(speakers)
# # print(counts)
#
# fig, ax1 = plt.subplots(1,1)
#
# y_pos = np.arange(len(speakers))
#
# ax = plt.bar(y_pos, counts, align='center', alpha=0.5)
# plt.xticks(y_pos, speakers, rotation='vertical')
# plt.ylabel('Lines')
# plt.title('Lines per Speaker in King Lear')
#
# ax1.set_xticklabels(speakers, {'rotation':80, 'fontsize':8})





# plt.show()
