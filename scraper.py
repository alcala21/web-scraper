import requests
import re
from bs4 import BeautifulSoup
import os


def get_content(_url):
    r = requests.get(_url)
    return BeautifulSoup(r.content, 'html.parser') if r else None


pages, art_type = int(input()), input()
root = "https://www.nature.com"
suf = "/nature/articles?sort=PubDate&year=2020"

for page in range(pages):
    dir_name = f"Page_{page + 1}"
    os.mkdir(dir_name)
    _url = root + suf + f"&page={page + 1}"
    soup = get_content(_url)

    if soup:
        articles = soup.find_all("article")
        for article in articles:
            if article.find("span", {"class": "c-meta__type"}).text == art_type:
                info = article.find("a", {"itemprop": "url"})
                title = re.sub(r"[^\w\s]", "", info.text)
                savename = dir_name + "/" + re.sub(r"\s", "_", title) + ".txt"
                content = get_content(root + info.get("href"))
                body = content.find("div", {"class": "c-article-body"})
                with open(savename, "w", encoding="utf-8") as f:
                    f.write(body.text)

print("Saved all articles.")

