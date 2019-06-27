import requests
# grab text
res = requests.get('http://www.dwt-inc.com/custom-filtration-products.html')
import bs4
soup = bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))
titleTagList = soup.select('title')
textStrongList = soup.select('strong')
for x in titleTagList:
    print(x.text)
for y in textStrongList:
    print(y.text)
# grab img
imgInfo = soup.select('img')
for z in range(len(imgInfo)-1):
    imgLink = 'http://www.dwt-inc.com/' + imgInfo[z]['src']
    print(imgLink)
    img = requests.get(imgLink, 'lxml')
    with open('1.jpg','wb') as f:
        f.write(img.content)