from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

req = Request("https://lols.gg/pt/name/lists/br/Recently%20Available%20Names/All/", headers={
    'User-Agent': 'Mozilla/5.0'
})

nick, available = [], []

html = urlopen(req)
bs = BeautifulSoup(html, 'html.parser')

lines = bs.find_all('tr')

for i in lines:
    children = i.findChildren("td")
    nick.append(children[0].text)
    available.append(children[1].text)

df = pd.DataFrame({
    'Nick': nick,
    'Available': available
})

df.head()

print(df)

df.to_excel('nicks_lol.xlsx')
