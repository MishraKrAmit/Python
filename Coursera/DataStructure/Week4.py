

import urllib.request as Imp
from bs4 import *
URL = Imp.urlopen('http://py4e-data.dr-chuck.net/comments_291644.html').read()
soup = BeautifulSoup(URL, 'html.parser')
Cout = 0
tot = 0
spans = soup('span')
for span in spans:
    tot += int(span.contents[0])
    Cout += 1
print('Count ', Cout)
print('Sum ', tot)
