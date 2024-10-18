import csv
import sqlite3


dbName = 'SalesHistory.db'
tableName = 'Sales2024'
conn = sqlite3.connect(dbName)
conn.execute(f'CREATE TABLE {tableName} (Id_pedido, Data, Id_Cliente, Fornecedor, Cod_Produto, Qtd., Vlr Uni, Vlr IPI, Vlr Tot, Vlr Tot IPI)')

conn.commit
conn.close

print('Table Created successfully')
