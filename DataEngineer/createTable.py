import csv
import sqlite3


dbName = 'SalesHistory.db'
tableName = 'Sales2024'
conn = sqlite3.connect(dbName)

conn.execute(f'''CREATE TABLE {tableName} (
    Id Pedido,
    Data,
    Id Cliente,
    Fornecedor,
    Cod Produto,
    Qtd,
    Vlr Unit,
    Vlr IPI,
    Vlr Tot Unit,
    Vlr Tot IPI)''')

conn.commit
conn.close

print('Table Created successfully')
