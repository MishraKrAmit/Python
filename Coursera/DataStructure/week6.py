
import urllib.request as ur
import json

url = 'http://py4e-data.dr-chuck.net/comments_291647.json'
data = ur.urlopen(url).read().decode('utf-8')
json = json.loads(data)

sum = 0
Count = 0

for each in json["comments"]:
    sum = sum+ int(each["count"])
    Count = Count+ 1
print('Count:', Count)
print('Sum:', sum)
