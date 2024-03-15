import sqlite3

# Define SQLite queries
# CREATE_TABLE_QUERY = """
# CREATE TABLE IF NOT EXISTS items (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     quantity INTEGER
# );
# """
# INSERT_ITEM_QUERY = "INSERT INTO items (name, quantity) VALUES (?, ?);"
# SELECT_ALL_ITEMS_QUERY = "SELECT * FROM items;"

SELECT_ERE_TRACKS_QUERY = """
SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '?ere*';
"""

# Connect to SQLite database
conn = sqlite3.connect('db/chinook.db')
cursor = conn.cursor()

# Create table if not exists
# cursor.execute(CREATE_TABLE_QUERY)

# Insert data into table
# item_data = [('Item1', 10), ('Item2', 20)]
# cursor.executemany(INSERT_ITEM_QUERY, item_data)
# conn.commit()

# Retrieve data from table
cursor.execute(SELECT_ERE_TRACKS_QUERY)
items = cursor.fetchall()
print("All ere tracks in database:")
for item in items:
    print(item)

# Close database connection
conn.close()