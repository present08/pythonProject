import requests

from bs4 import BeautifulSoup
url ="https://novel.naver.com/webnovel/weekday"

res =requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

webtoon = soup.find("div", attrs={"id":"integrationRaking"})
print(webtoon)

titles = webtoon.find_all("span", attrs={"class","title"})

for title in titles: # forEach 같은 친구
    if title: print(title.get_text())
    else: print("제목없음")