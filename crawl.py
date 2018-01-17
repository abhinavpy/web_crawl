import time
import urllib

import bs4
import requests

url_lis = ['https://en.wikipedia.org/wiki/Special:Random']
print(url_lis[-1])
for ele in url_lis:
    response = requests.get(ele)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    li =''
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            li = element.find("a", recursive=False).get('href')
            break
    if len(li)==0:
        print("We've arrived at an article with no links, aborting search!")
        break
    li = urllib.parse.urljoin('https://en.wikipedia.org/', li)

    if li not in url_lis and li!="https://en.wikipedia.org/wiki/Philosophy" :
        url_lis.append(li)
    print(url_lis[-1])
