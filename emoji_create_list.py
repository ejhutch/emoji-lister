from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

data = urlopen('https://www.webpagefx.com/tools/emoji-cheat-sheet').read()
soup = bs(data)

emoji_list = []

for span in soup.findAll('span', class_="name"):
    emoji_list.append(":" + span.text + ":\n")
    
emoji_list.sort()

with open("emoji-list.txt", "w") as f:
    for x in emoji_list: 
        f.write(x)


