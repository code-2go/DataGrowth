import csv
import sqlite3


dbName = 'SalesHistory.db' # Variável para o nome do banco de dados
tableName = 'Sales2024' # Variável para o nome da tabela
conn = sqlite3.connect(dbName) # Conexão ao banco de dados, caso não exista, ele será automaticamente criado

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
    Vlr Tot IPI)''') # Criação da tabela

conn.commit # Commit, para confirmação
conn.close # Fechamento da conexão para encerrar a utilização de recursos do sistema

print('Table Created successfully') # Mensagem de confirmação do código
