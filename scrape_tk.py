from bs4 import BeautifulSoup
import requests


grey_jeans_example_url = "https://tkaninykaroliny.pl/pl/p/JEANS-WODOODPORNY-Szary-364/331"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

req = requests.get(grey_jeans_example_url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

# id=box_productrelated


matching = soup.find("box_productrelated")

# with open("pasujace.html", "w") as f:
#     f.write(str(matching))

# print(matching)

matching_elems = []

for d in soup.select('a.details'):
    print(d['href'])
    print(d['title'])
    for i in d.select('img'):
        print(i['src'])
        matching_elems.append({"href":d['href'], "title":d['title'], "img":i['src']})


print(matching_elems)
"""
Main material:
- description: what use it for
- colour data
- pattern


We're looking for related materials:
data-product-id
data-category
download img
"""