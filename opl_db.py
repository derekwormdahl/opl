import sqlite3
import collections
from ordereddict import OrderedDict
import json

conn = sqlite3.connect('opl.db')

c = conn.cursor()

"""
c.execute('''create table gameday (id integer primary key autoincrement, gamedate text, created_date text, last_updated_date text)''')

c.execute('''create table game 
	(id integer primary key autoincrement, gamecode text, gameday_id integer, 
	gametime text, hometeam text, awayteam text, homescore integer, awayscore integer,
	gamelocation text, gamelocation_url text, gamelocation_coords text, created_date text, last_updated_date text)''')  
"""

def create_gameday(gamedate):
	conn = sqlite3.connect('opl.db')
	c = conn.cursor()
	c.execute("""insert into gameday (gamedate) values (?)""", (gamedate,))
	conn.commit()
	c.execute("""select last_insert_rowid() from gameday""")
	rowid = c.fetchone()
	c.close()
	conn.close()
	return rowid[0]

def select_gameday():
	conn = sqlite3.connect('opl.db')
	c = conn.cursor()
	c.execute("select id, gamedate, created_date, last_updated_date  from gameday")
	rows = c.fetchall()

	rowarray_list = []
	for r in rows:
		t = OrderedDict()
		t['id'] = r[0]
		t['gamedate'] = r[1]
		t['created_date'] = r[2]
		t['last_updated_date'] = r[3]
		rowarray_list.append(t)

	j = json.dumps(rowarray_list)
	print j	

def create_game(gamecode, gameday_id, gametime, hometeam, awayteam, homescore, awayscore, gamelocation, gamelocation_url, gamelocation_coords):
	conn = sqlite3.connect('opl.db')
	c = conn.cursor()
	c.execute("""insert into game (gamecode, gameday_id, gametime, hometeam, awayteam, homescore, awayscore, gamelocation, gamelocation_url, gamelocation_coords) values (?,?,?,?,?,?,?,?,?,?)""", (gamecode, gameday_id, gametime, hometeam, awayteam, homescore, awayscore, gamelocation, gamelocation_url, gamelocation_coords))
	conn.commit()
	c.execute("""select last_insert_rowid() from game""")
	rowid = c.fetchone()
	c.close()
	conn.close()
	return rowid[0]

def select_game():
	conn = sqlite3.connect('opl.db')
	c = conn.cursor()
	c.execute("select id, gamecode, gameday_id, gametime, hometeam, awayteam, homescore, awayscore, gamelocation, gamelocation_url, gamelocation_coords, created_date, last_updated_date from game")
	rows = c.fetchall()

	rowarray_list = []
	for r in rows:
		t = OrderedDict()
		t['id'] = r[0]
		t['gamecode'] = r[1]
		t['gameday_id'] = r[2]
		t['gametime'] = r[3]
		t['hometeam'] = r[4]
		t['awayteam'] = r[5]
		t['homescore'] = r[6]
		t['awayscore'] = r[7]
		t['gamelocation'] = r[8]
		t['gamelocation_url'] = r[9]
		t['gamelocation_coords'] = r[10]
		t['created_date'] = r[11]
		t['last_updated_date'] = r[12]
		rowarray_list.append(t)

	j = json.dumps(rowarray_list)
	print j	

c.execute('''create table division (id integer primary key autoincrement, gender text, age integer, title text, url text, created_date text, last_updated_date text)''')
def create_division(gender, age, title, url):
	conn = sqlite3.connect('opl.db')
	c = conn.cursor()
	c.execute("""insert into division (gender, age, title, url) values (?,?,?,?)""", (gender, age, title, url))
	conn.commit()
	c.execute("""select last_insert_rowid() from division""")
	rowid = c.fetchone()
	c.close()
	conn.close()
	return rowid[0]

def select_division():
	conn = sqlite3.connect('opl.db')
	c = conn.cursor()
	c.execute("select id, gender, age, title, url, created_date, last_updated_date from division")
	rows = c.fetchall()

	rowarray_list = []
	for r in rows:
		t = OrderedDict()
		t['id'] = r[0]
		t['gender'] = r[1]
		t['age'] = r[2]
		t['title'] = r[3]
		t['url'] = r[4]
		t['created_date'] = r[5]
		t['last_updated_date'] = r[6]
		rowarray_list.append(t)

	j = json.dumps(rowarray_list)
	print j	
"""
c.execute('''create table division (id integer primary key autoincrement, gender text, age integer, title text, url text, created_date text, last_updated_date text)''')

c.execute("insert into gameday (gamedate) values ('Sat, September 9, 2012')")

c.execute('select last_insert_rowid() from gameday')
firstid = c.fetchone()
print "RowID1: ", firstid


c.execute("insert into gameday (gamedate) values ('Sun, September 10, 2012')")
c.execute('select last_insert_rowid() from gameday')
secondid = c.fetchone()
print "RowID2: ", secondid


c.execute("insert into game (gamecode, gameday_id, gametime, hometeam, awayteam, gamelocation) values ('2500',1,'11:00 am','Athletica','FC Portland','LCC')")
c.execute("insert into game (gamecode, gameday_id, gametime, hometeam, awayteam, gamelocation) values ('2501',2,'11:00 am','Athletica','THUSC','LCC')")


for row in c.execute('select * from gameday'):
	print row

for row in c.execute('select * from game'):
	print row


for row in c.execute('select gd.gamedate, g.gametime, g.hometeam, g.awayteam, g.gamelocation from gameday gd, game g where gd.id = g.gameday_id'):
	print row
"""

conn.close()
