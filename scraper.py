import requests
import re
from bs4 import BeautifulSoup


def get_content(_url):
    r = requests.get(_url)
    return BeautifulSoup(r.content, 'html.parser') if r else None


root = "https://www.nature.com"
suf = "/nature/articles?sort=PubDate&year=2020&page=3"

soup = get_content(root + suf)

if soup:
    articles = soup.find_all("article")
    for article in articles:
        if article.find("span", {"class": "c-meta__type"}).text == "News":
            info = article.find("a", {"itemprop": "url"})
            title = re.sub(r"[^\w\s]", "", info.text)
            savename = re.sub(r"\s", "_", title) + ".txt"
            content = get_content(root + info.get("href"))
            body = content.find("div", {"class": "c-article-body"})
            with open(savename, "w", encoding="utf-8") as f:
                f.write(body.text)
            print("Content saved.")

