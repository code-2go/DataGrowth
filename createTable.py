import csv
import sqlite3


dbName = 'SalesHistory.db'
tableName = 'Sales2024'
conn = sqlite3.connect(dbName)
conn.execute(f'CREATE TABLE {tableName} (Product1, Quantity, Value)')

conn.commit
conn.close