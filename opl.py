from bs4 import BeautifulSoup
import urllib2
from decimal import *
from datetime import datetime

doc = BeautifulSoup(urllib2.urlopen("http://www.oregonpremierleague.com/schedules/Fall2012/47896539.html","html5lib"));

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


#result = " ".join([t[0],t[1],day,t[3]])
#print result

