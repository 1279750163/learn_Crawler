import requests

url = "http://www.crazyant.net"
url2 = "http://www.baidu.com"
url3 = "http://www.httpcn.com"
r = requests.get(url2)
print(r.status_code)
print(r.headers)
print(r.encoding)
r.encoding = "utf-8"
print(r.encoding)
# print(r.text)
print(r.cookies)