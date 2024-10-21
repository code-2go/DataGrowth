import csv
import sqlite3

dbname = 'SalesHistory.db'
csvfile ="histórico de pedidos 2024"
tableName = 'sales2024'

with open (csvfile, 'r') as file:
    reader = csv.reader(file) # Leitura do arquivo csv
    next(reader) # Pula a primeira linha (header) do arquivo
    conn = sqlite3.connect(dbname) # Conexão ao banco de dados

    for row in reader: # Looping para inserção de dados na tabela
        conn.execute(f'''
                    INSERT INTO {tableName} 
                    (ID_Pedido, Data, ID_Cliente, Fornecedor, Qtd., Vlr.Unit, Vlr.IPI, Vlr.Tot., Vlr.Tot.IPI)
                    Values (?,?,?,?,?,?,?,?,?,?)
                     ''')
conn.commit() 
conn.close() #Fechamento da conexão, poupando recursos do sistema

print('The file has been processed') 
