import csv
import sqlite3

dbName = 'Sales History.db'
conn = sqlite3.connect(dbName)
conn.execute('CREATE TABLE Test (Product1, Quantity, Value)')

conn.commit
conn.close