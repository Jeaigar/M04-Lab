import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('books.db')

# Create a cursor object
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE books
    (title TEXT,
    author TEXT,
    year INTEGER)
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
