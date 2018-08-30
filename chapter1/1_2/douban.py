import requests
import pandas
from bs4 import BeautifulSoup

r = requests.get('https://book.douban.com/subject/1084336/comments').text

soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('span', 'short')
for item in pattern:
    print(item.string)

comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')