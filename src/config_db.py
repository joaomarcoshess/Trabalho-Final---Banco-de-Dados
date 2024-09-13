import mariadb


# Cria um pool de conexões com o banco de dados
def criar_pool():
    return mariadb.ConnectionPool(
        pool_name='doencas-pool',
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='doencas',
        pool_size=2)

# Cria uma única conexão com o banco de dados
def criar_conexao():
    return mariadb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='doencas')