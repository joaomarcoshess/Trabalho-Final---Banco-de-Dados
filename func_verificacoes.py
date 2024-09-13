# Verifica se a doença já existe a partir de seu nome
def verificar_doenca(cursor, nome_doenca):
    cursor.execute('SELECT COUNT(*) FROM Doenca WHERE nome = ?', [nome_doenca])
    count = cursor.fetchone()[0]
    return count > 0

# Verifica se o sintoma já existe a partir de seu nome
def verificar_sintoma(cursor, nome_sintoma):
    cursor.execute('SELECT COUNT(*) FROM Sintoma WHERE nome = ?', [nome_sintoma])
    count = cursor.fetchone()[0]
    return count > 0

# Verifica se o patógeno já existe a partir de seu nome
def verificar_patogeno(cursor, nome_patogeno):
    cursor.execute('SELECT COUNT(*) FROM Patogeno WHERE nome_cientifico = ?', [nome_patogeno])
    count = cursor.fetchone()[0]
    return count > 0

# Verifica se o tipo de patógeno já existe a partir de seu nome
def verificar_tipo_patogeno(cursor, tipo_patogeno):
    cursor.execute('SELECT COUNT(*) FROM TipoDePatogeno WHERE tipo = ?', [tipo_patogeno])
    count = cursor.fetchone()[0]
    return count > 0

# Verifica se o CID já existe
def verificar_cid_existe(cursor, cid):
    cursor.execute('SELECT COUNT(*) FROM Doenca WHERE cid = ?', [cid])
    count = cursor.fetchone()[0]
    return count > 0