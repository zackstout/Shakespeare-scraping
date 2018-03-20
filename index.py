
# Following along with https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/:
import urllib.request, urllib.error
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
# soup = BeautifulSoup(page, "html5lib")
# print(soup.prettify())
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')

# right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
#
# A=[]
# B=[]
# C=[]
# D=[]
# E=[]
# F=[]
# G=[]
# for row in right_table.findAll("tr"):
#     cells = row.findAll('td')
#     states=row.findAll('th') #To store second column data
#     if len(cells)==6: #Only extract table body not heading
#         A.append(cells[0].find(text=True))
#         B.append(states[0].find(text=True))
#         C.append(cells[1].find(text=True))
#         D.append(cells[2].find(text=True))
#         E.append(cells[3].find(text=True))
#         F.append(cells[4].find(text=True))
#         G.append(cells[5].find(text=True))

# print(C)



# Shakespeare plays:
# Holds urls:
allPlays = []
# Holds all strings:
allStrings = []
allSpeakers = []
allText = []
allDictionaries = []

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
    speakersDict = dict()

    allStrings = []
    allText = []
    global currentCount
    currentCount = 0
    global currentSpeaker
    currentSpeaker = ''
    global allDictionaries

    for ind, play in enumerate(allPlays):
        if ind == x:
            page = urllib.request.urlopen(play)
            soup2 = BeautifulSoup(page, "html5lib")
            allStrings = soup2.findAll('a')

    # print(allStrings)
    # for s in allStrings:
    #     print(s)
    #     print('\n')

    for s in allStrings:
        if (str(s)[9] == 's'):
            ind = str(s).find('b>') + 2
            end = str(s).find('</')
            allSpeakers.append(str(s)[ind : end])

            # Switch to new speaker:
            oldSpeaker = currentSpeaker

            if oldSpeaker in speakersDict:
                speakersDict[oldSpeaker] += currentCount
            else:
                speakersDict[oldSpeaker] = currentCount

            currentSpeaker = str(s)[ind : end]
            currentCount = 0

        else:
            ind = str(s).find('">') + 2
            end = str(s).find('</')

            ind2 = str(s).find('="')
            data = {}
            # Odd we couldn't use dot notation here:
            data['line'] = str(s)[ind:end]
            data['lineNo'] = str(s)[ind2 + 2:ind - 2]
            allText.append(data)

            # Increment current speaker's count:
            currentCount = currentCount + 1
    # AHA!  We had this inside the for loop!!!!
    allDictionaries.append(speakersDict)

getPlay(26)


# for x in range(38):
#     getPlay(x)
# getPlay(1)
# getPlay(2)

# print(len(allText))
# print(allText)
# print(allDictionaries)

# for d in allDictionaries:
#     print(d)
#     print('\n')

speakers = []
counts = []

# print(allDictionaries[0]['LEAR'])

for key in allDictionaries[0]:
    speakers.append(key)
    counts.append(allDictionaries[0][key])

print(speakers)
print(counts)

fig, ax1 = plt.subplots(1,1)

y_pos = np.arange(len(speakers))

ax = plt.bar(y_pos, counts, align='center', alpha=0.5)
plt.xticks(y_pos, speakers, rotation='vertical')
plt.ylabel('Lines')
plt.title('Lines per Speaker in King Lear')

ax1.set_xticklabels(speakers, {'rotation':80, 'fontsize':8})

# print(ax.get_xticks())
# axes.tick_params( axis='x', width=10, length=10)
# print(plt)
plt.show()
