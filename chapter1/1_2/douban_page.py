import requests
from bs4 import BeautifulSoup

urlFormat = "https://book.douban.com/subject/1084336/comments/hot?p="
pageNo = 1
url = urlFormat + str(pageNo)
r = requests.get(url)
while r.status_code == 200:
    print(url)
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    pattern = soup.find_all('span', 'short')
    for item in pattern:
     print(item.string)
    pageNo=pageNo+1
    url = urlFormat + str(pageNo)
    r = requests.get(url)



#comments = []
#for item in pattern:
#    comments.append(item.string)
#df = pandas.DataFrame(comments)
#df.to_csv('comments.csv')
