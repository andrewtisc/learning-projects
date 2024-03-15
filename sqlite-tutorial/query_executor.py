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

# Connect to SQLite database
conn = sqlite3.connect('db/chinook.db')
cursor = conn.cursor()

# Function to execute all commands from a SQL file
def execQueriesFromFile(file_name):
    # Read file
	with open(file_name, 'r') as file:
        # Get array of SQL commands from file
		sql_commands = file.read().split(';')
		print(sql_commands)
		# Execute all commands
		for c in sql_commands:
			try:
				cursor.execute(c)
				printCursorResults()
			except:
				print(f"Command skipped: {c}")
                
# Function to print out the results from executed commands
def printCursorResults():
    lines = cursor.fetchall()
    for l in lines:
        print(l)

execQueriesFromFile('ere_tracks.sql')
conn.close()