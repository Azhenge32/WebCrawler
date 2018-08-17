import requests
from lxml import etree
url = "https://book.douban.com/subject/1084336/comments"
r = requests.get(url).text
#print(r)
s = etree.HTML(r)
# 浏览器--方便
# print(s.xpath('//*[@id="comments"]/ul/li[1]/div[2]/p/span/text()'))
# print(s.xpath('//*[@class="comment-content"]/span/text()'))
print(s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()'))

# 手写--适用于简单结构化数据
# print(s.xpath('//p[@class="comment-content"]/span/text()'))
# print(s.xpath('//p[@class="comment-content"]/span/text()')[0])