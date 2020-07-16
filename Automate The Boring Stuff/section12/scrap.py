import requests,bs4

def getScrap(productURL):
    res = requests.get(productURL)
    res.raise_for_status() 

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(".calibre2")
    chapter=[]
    for elem in elems:
        chapter.append(elem.text.strip())
    #print(chapter)
    return chapter

url = "https://automatetheboringstuff.com/2e/chapter12/"
scrap_dict = getScrap(url)
#print(scrap_dict)
for scrap in scrap_dict:
    print(f"Chapter : {scrap}")


