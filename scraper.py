import requests
from bs4 import BeautifulSoup


class MovieError(Exception):
    ...


url = input("Input the URL:\n")
r = requests.get(url)
sc = r.status_code
if sc == 200:
    with open("source.html", "wb") as f:
        f.write(r.content)
    print("Content saved.")
else:
    print(f"The URL returned {sc}!")
