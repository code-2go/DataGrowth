import csv
import sqlite3

conn = sqlite3.connect('')
conn.execute(''CREATE TABLE Test (Product1, Quantity, Value)'')

conn.commit
conn.close