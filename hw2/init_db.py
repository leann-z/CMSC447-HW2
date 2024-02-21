import sqlite3

# database file name
db_file = 'database.db'

#create table statement
create_table_sql = """
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    points INTEGER NOT NULL
);
"""

#database content!
users_data = [
    ("Steve Smith", 211, 80),
    ("Jian Wong", 122, 92),
    ("Chris Peterson", 213, 91),
    ("Sai Patel", 524, 94),
    ("Andrew Whitehead", 425, 99),
    ("Lynn Roberts", 626, 90),
    ("Robert Sanders", 287, 75),
]

# connect to sql database
conn = sqlite3.connect(db_file)

# create cursor
cursor = conn.cursor()

# this command creates the sqllite table
cursor.execute(create_table_sql)

insert_sql = 'INSERT INTO Users (name, id, points) VALUES (?, ?, ?)'
cursor.executemany(insert_sql, users_data)

# make sure to commit!!!
conn.commit()

# close the connection, now the database is made
conn.close()