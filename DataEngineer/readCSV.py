import csv
import sqlite3

dbname = 'SalesHistory.db'
csvfile ="histórico de vendas 2024"
tableName = 'sales2024'
with open (csvfile, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    conn = sqlite3.connect(dbname)

    for row in reader:
        conn.execute(f'''
                    INSERT INTO {tableName} 
                    (ID_Pedido, Data, ID_Cliente, Fornecedor, Qtd., Vlr.Unit, Vlr.IPI, Vlr.Tot., Vlr.Tot.IPI)
                    Values (?,?,?,?,?,?,?,?,?,?)
                     ''')
conn.commit()
conn.close()

print('Processed')