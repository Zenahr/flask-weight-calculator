import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE weights (ID INTEGER PRIMARY KEY AUTOINCREMENT, WEIGHT DECIMAL NOT NULL, DATE_TIME TEXT NOT NULL)')
print ("Table created successfully")
conn.close()