import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python"
r = requests.get(url=url)
soup = BeautifulSoup(r.content, 'html5lib')
allH3 = soup.find_all("h3", class_="s-post-summary--content-title")
for i in allH3:
    aContent = i.a.contents[0]
    print(aContent)
