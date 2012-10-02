#from bs4 import BeautifulSoup
from bs4 import *
import urllib2
from decimal import *
from datetime import datetime
from bs4 import NavigableString
import collections

def convert(data):
    if isinstance(data, unicode):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
 

doc = BeautifulSoup(urllib2.urlopen("http://www.oregonpremierleague.com/standingsandschedules/Fall2012/index_E.html","html5lib"));


t = doc.find("table").select(".MainContent")
doc2 = BeautifulSoup(str(t[0]),"html5lib")

print "*********************************************************"
scheds = doc2.table.table.find_all("div","tg")
for sched in scheds:
	print sched.text
	print sched.a.get('href')
###print (link.get('href'))




"""
if 'RowHeader' in t.tr.td['class']:
	print t.tr.td.text.strip()

for sib in t.tr.next_siblings:
	if not isinstance(sib, NavigableString):
		if(sib.select(".RowHeader")):
			print "****** Game Day: *****",sib.td.text.strip()
		t1 = convert(sib.attrs)
		if t1.has_key('class'):
			print t1['class']
"""



