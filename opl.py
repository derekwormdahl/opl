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
 

doc = BeautifulSoup(urllib2.urlopen("http://www.oregonpremierleague.com/schedules/Fall2012/47896539.html","html5lib"));

"""
print(doc.find("table").find(id="tblListGames2").find("tbody").find("tr").find("td").prettify())

game_date = doc.find("table").find(id="tblListGames2").find("tbody").find("tr").find("td").text.strip()

game_date = "Sat, September 10, 2012"

print game_date

t = game_date.split()

print t

if Decimal(t[2].strip(',')) < 10: 
	day = ''.join(['0',t[2]])
	game_date = " ".join([t[0],t[1],day,t[3]])

final_game_date = datetime.strptime(game_date, "%a, %B %d, %Y");

print final_game_date
"""

#print(doc.find("table").find(id="tblListGames2").find("tbody").find_all("tr"))

t = doc.find("table").find(id="tblListGames2").find("tbody")

#doc3 = BeautifulSoup(open('sched2.txt'))

print "*********************************************************"
#print t.tr.next_sibling.next_sibling.next_sibling.next_sibling


if 'RowHeader' in t.tr.td['class']:
	print t.tr.td.text.strip()

for sib in t.tr.next_siblings:
	if not isinstance(sib, NavigableString):
	#if(type(sib) is bs4.element.Tag):
	#if(callable(sib.select)):
		if(sib.select(".RowHeader")):
			print "****** Game Day: *****",sib.td.text.strip()
		#else:
		# print "************ ",sib
		#for tt in t:
		#	print tt
		"""
		t1 = convert(sib.attrs)
		if t1.has_key('class'):
			print t1['class']
			"""
		#print 'class' in sib.attrMap
		#if((sib.get("class")).contains("sch-main-gm")):
		#	print "    game"#,g.td.span.text
	#print "Sib: ",sib," Type: ",type(sib)



"""
gamedays = doc.findAll('td', {'class':'RowHeader'})
for gameday in gamedays:
	print gameday.string


print doc2.tr.next_sibling

"""
