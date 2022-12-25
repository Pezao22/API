import mysql.connector as mysql

# Configuação com o banco de dados [Mariadb- HeidenSQL]
conexao = mysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="testpy"
)

cursor = conexao.cursor()

name_tabela = 'registro'

# Cria a tabela 

#cursor.execute(f"CREATE TABLE {name_tabela} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), telefone VARCHAR(100))")

#cursor.execute("SHOW TABLES") # exite as tabelas existenta 

# adiciona no banco de dados

def add(nome,mail,tel): # add(nome,email,telefone)
    inserir = f"INSERT INTO {name_tabela} (nome,email,telefone) VALUE(%s,%s,%s)"
    dados = (nome,mail,tel)
    cursor.execute(inserir,dados)
    conexao.commit()
    print(f'Adicionado {nome} - {mail} - {tel}')

# remover um valor passando como parametro nome da coluna e a chave de pesquina 

def rem(nomecoluna,valor): # rem(coluna,valor)
    remover = f"DELETE FROM {name_tabela} WHERE {nomecoluna} = '{valor}'"
    cursor.execute(remover)
    conexao.commit()
    print(f'Excluido {valor} da coluna {nomecoluna}')

# atualizar tabela conforme parametros

def update(nomecoluna,valor,valor2): # update(coluna,novo valor,antigo valor)
    atualizar = f"UPDATE {name_tabela} SET {nomecoluna} = '{valor}' WHERE {nomecoluna} = '{valor2}'"
    cursor.execute(atualizar)
    conexao.commit()
    print(f'Atualizado {valor2} da coluna {nomecoluna} para {valor2}')

# RETORNA A OS VALORES DA TABELA (REGISTRO)
def select():
    buscar = f'SELECT * FROM {name_tabela}'
    cursor.execute(buscar)
    result = cursor.fetchall()
    return result
    