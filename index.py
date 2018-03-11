
# Following along with https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/:
import urllib.request, urllib.error
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
# soup = BeautifulSoup(page, "html5lib")
# print(soup.prettify())

# title = soup.title.string
#
# all_links = soup.find_all("a")
# # for link in all_links:
#     # print(link.get("href"))
#
# all_tables = soup.find_all('table')
#
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
allPlays = []

shakespeare = 'http://shakespeare.mit.edu/'
page = urllib.request.urlopen(shakespeare)
soup = BeautifulSoup(page, "html5lib")

all_links = (soup.find_all('a'))

for pos, link in enumerate(all_links):
    # print(link.get("href"))
    href = link.get("href")
    ind = href.find("/")
    if pos > 1 and pos < len(all_links) - 7:
        if not ind == -1:
            # print(link.get("href")[0 : ind])
            url = 'http://shakespeare.mit.edu/' + href[0 : ind] + '/full.html'
            allPlays.append(url)
    # print([pos for pos, char in enumerate(link) if char == '/'])
# print(allPlays)

for play in allPlays:
    page = urllib.request.urlopen(play)
    soup2 = BeautifulSoup(page, "html5lib")
    print(soup2)
