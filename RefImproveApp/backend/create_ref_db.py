import sqlite3

# Create the db for referee improvement database
connection = sqlite3.connect("referee_improvement.db")

# Create cursor
cursor = connection.cursor()

# Create table

table = """CREATE TABLE IF NOT EXISTS
refereeeImprove(game_id TEXT PRIMARY KEY,
    date TEXT,
    comment TEXT,
    fieldNUM INTEGER,
    homeTeam TEXT,
    awayTeam TEXT)
"""

cursor.execute(table)

# How to add elements 
# cursor.execute("INSERT INTO refereeImprove (game_id, date, comment, fieldNUM, homeTeam, awayTeam)
# VALUES ('game1', '2024-06-03', 'Good game overall', 1, 'Home Team', 'Away Team')")

