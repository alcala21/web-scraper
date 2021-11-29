import requests


class QuoteError(Exception):
    ...


url = input("Input the URL:\n")

r = requests.get(url)

try:
    if r:
        body = r.json()
        if 'content' in body:
            print(body['content'])
        else:
            raise QuoteError
    else:
        raise QuoteError
except QuoteError:
    print("Invalid quote resource!")
