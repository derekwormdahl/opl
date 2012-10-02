import opl_db

gameday_id = opl_db.create_gameday("sunday october 5, 2012")
print "Game Day ID:", gameday_id

opl_db.select_gameday()

game_id = opl_db.create_game("2000", gameday_id, "11:00 am", "Athletica Blue", "FC Portland", "", "", "LCC", "http://maps.google.com/stuff", "+12332.000")

print "Game ID:", game_id

opl_db.select_game()
