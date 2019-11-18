import urllib.request as ur
from bs4 import *

current_repeat_count = 0
#url = input('Enter URL: ')
url = 'http://py4e-data.dr-chuck.net/known_by_Chala.html'
repeat_count = 7 # int(input('Enter count: '))
position = 18 # int(input('Enter position: '))


def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print('Retrieving: ', url)
    print (current_repeat_count)
    tags = parse_html(url)
    print (tags)
    for index, item in enumerate(tags):
    #     if index == position - 1:
    #         url = item.get('href', None)
    #         name = item.contents[0]
    #         break
    #     else:
    #         continue
    current_repeat_count += 1
print('Last Url: ', url)
