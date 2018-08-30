import requests
r = requests.get("https://www.baidu.com/")
print(r)
print(r.text)
r.encoding = 'utf-9'
print(r.text)