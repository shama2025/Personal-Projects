import sqlite3

"""This will store the parameters in the referee database"""
def store_comments(date, comment, field_num, home_team, away_team):
    try:
        # Connect to the database
        connection = sqlite3.connect("referee_improvement.db")
        cursor = connection.cursor()
        
        size = get_db_szie()

        # Use parameterized query to avoid SQL injection and handle data types
        cursor.execute("INSERT INTO refereeeImprove (game_id, date, comment, fieldNUM, homeTeam, awayTeam) VALUES (?, ?, ?, ?, ?, ?)",
                       (f'game{size+1}', date, comment, field_num, home_team, away_team))
        
        # Commit the transaction
        connection.commit()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        return True  # Successful execution
    except Exception as e:
        print(e)
        return False  # Error during execution

"""This will get the size of the db so the primary key can be incremented"""
def get_db_szie():
    conn = sqlite3.connect("referee_improvement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM refereeeImprove")

    get_size = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return get_size