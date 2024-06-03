# This will file will have functions to store comments about referees
import sqlite3

connection = sqlite3.connect("referee_improvement.db")

"""This will store the comments about the game and other values to the database"""
def store_comments(date, comment, field_num, home_team, away_team):
    try:
    # Create cursor
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO refereeImprove (game_id, date, comment, fieldNUM, homeTeam, awayTeam) VALUES ('game1', {date}, {comment}, {field_num}, {home_team}, {away_team})")
        return True # Valid execution
    except:
        return False # Invalid execution
