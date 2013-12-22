#!python3.2.3
import sys
import json
import urllib.request
from bs4 import BeautifulSoup


req = urllib.request.Request('http://book.douban.com/tag/?view=type')
response = urllib.request.urlopen(req)

soup = BeautifulSoup(response.read().decode('utf8'))
list_cnt = soup.select('.article div')[1]

data = {}
for li in list_cnt.select('div'):
    group = BeautifulSoup(str(li.select('a[name]'))).a.get('name')
    td = BeautifulSoup(str(li.select('table td')))
    tag = BeautifulSoup(str(td.select('a')))
    num = BeautifulSoup(str(td.select('b')))

    item = {}
    for (t,n) in zip(tag,num):
        if t.string.strip() not in ('[',']',','):
            item[t.string] = n.string.lstrip('(').rstrip(')')

    data[group] = item


print(data)
open('douban.json','w').write(json.dumps(data))

