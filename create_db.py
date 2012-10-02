import sqlite3

conn = sqlite3.connect('opl.db')

c = conn.cursor()

c.execute('''create table gameday (id integer primary key autoincrement, gamedate text, created_date text, last_updated_date text)''')

c.execute('''create table game 
	(id integer primary key autoincrement, gamecode text, gameday_id integer, 
	gametime text, hometeam text, awayteam text, homescore integer, awayscore integer,
	gamelocation text, gamelocation_url text, gamelocation_coords text, created_date text, last_updated_date text)''')  
"""

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
