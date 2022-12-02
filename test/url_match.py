import re

url1 = "http://www.crazyant.net/1234.html"
url2 = "http://www.crazyant.net/1234.html#comments"
url3 = "http://www.baidu.com"

pattern = r'^http://www.crazyant.net/\d+.html$'

print(re.match(pattern, url1))