import sqlite3

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


def get_db_szie():
        # Connect to the SQLite database
    conn = sqlite3.connect("referee_improvement.db")
    cursor = conn.cursor()

    # Execute a query to count the number of rows in your table
    size = cursor.execute("SELECT COUNT(*) FROM refereeeImprove")

    # Fetch the result of the query
    size = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return size