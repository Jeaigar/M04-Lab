from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

# Create an engine that connects to the books.db SQLite database
engine = create_engine('sqlite:///books.db')

# Initialize metadata object
metadata = MetaData()

# Reflect the books table
books = Table('books', metadata, autoload_with=engine)

# Build a select statement to get the title column from the books table
stmt = select([books.columns.title]).order_by(books.columns.title)

# Execute the statement and fetch all results
with engine.connect() as connection:
    result = connection.execute(stmt).fetchall()

# Print the titles in alphabetical order
for row in result:
    print(row[0])
