from func_utilitarias import *
from menu_improvisado import menu

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors

import io

# Tem que verificar antes se o patogeno_id é válido e se o CID não existe para outra doença
def cadastrar_doenca(cursor, cid, nome_tecnico, patogeno_id):
  cursor.execute('INSERT INTO Doenca (nome, cid, patogeno_id) VALUES (?, ?, ?)', [nome_tecnico, cid, patogeno_id])
  doenca_id = cursor.lastrowid # Obtém o ID da doença cadastrada (AUTO_INCREMENT)
  cursor.connection.commit()
  return doenca_id

# Tem que verificar antes se doença_id é válido
def cadastrar_nome_popular(cursor, nome_popular, doenca_id):
    cursor.execute('INSERT INTO NomesPopulares (nomes_populares, doenca_id) VALUES (?, ?)', (nome_popular, doenca_id))
    cursor.connection.commit()


# Tem antes que verificar se a doença_id e sintoma_id são validos
def inserir_taxa_ocorrencia(cursor, doenca_id, sintoma_id, nivel_ocorrencia):
    cursor.execute('INSERT INTO TaxaDeOcorrencia (doenca_id, sintoma_id, nivel_ocorrencia) VALUES (?, ?, ?)', [doenca_id, sintoma_id, nivel_ocorrencia])
    cursor.connection.commit()


# Retorna o id de um sintoma a partir de seu nome
def obter_id_sintoma(cursor, nome_sintoma):
    cursor.execute('SELECT id FROM Sintoma WHERE nome = ?', [nome_sintoma])
    resultado = cursor.fetchone()
    cursor.connection.commit()
    return resultado[0]

# Retorna o id de um patógeno a partir de seu nome
def obter_id_patogeno(cursor, nome_patogeno):
    cursor.execute('SELECT id FROM Patogeno WHERE nome_cientifico = ?', [nome_patogeno])
    resultado = cursor.fetchone()
    cursor.connection.commit()
    return resultado[0]

# Retorna o id de um tipo de patógeno a partir de seu nome
def obter_id_tipo_patogeno(cursor, tipo_patogeno):
    cursor.execute('SELECT id FROM TipoDePatogeno WHERE tipo = ?', [tipo_patogeno])
    resultado = cursor.fetchone()
    cursor.connection.commit()
    return resultado[0]

# Tem que verificar se o sintoma ja existe antes de chamar essa função
def cadastrar_sintoma(cursor, sintoma):
    cursor.execute('INSERT INTO Sintoma (nome) VALUES (?)', [sintoma])
    cursor.connection.commit()

# Tem que verificar se o patogeno ja existe antes de chamar essa função
def cadastrar_patogeno(cursor, patogeno, tipoPatogenoId):
    cursor.execute('INSERT INTO Patogeno (nome_cientifico, tipopatogeno_id) VALUES (?, ?)', [patogeno, tipoPatogenoId])
    cursor.connection.commit()

# Tem que verificar se o tipo de patogeno ja existe antes de chamar essa função
def cadastrar_tipo_patogeno(cursor, tipo_patogeno):
    cursor.execute('INSERT INTO TipoDePatogeno (tipo) VALUES (?)', [tipo_patogeno])
    tipo_patogeno_id = cursor.lastrowid # Obtém o ID do tipo de patogeno cadastrado (AUTO_INCREMENT)
    cursor.connection.commit()
    return tipo_patogeno_id

def consulta_doenca(cursor, indice_escolhido, dado):
    colunas = ['CID', 'nome', 'nome_popular', 'patogeno_id']
    if(indice_escolhido != 2):
        cursor.execute('select * from doenca ? = ?', [colunas[indice_escolhido], dado])
    else:
        cursor.execute('select * from doenca join nomespopulares on doenca.id = nomespopulares.doenca_id where nomespopulares.nomes_populares = ?', [dado])
        consulta = cursor.fetchall()
        return {'id:':consulta[0][0],
        'nome:':consulta[0][1],
        'CID:':consulta[0][2],
        'Nome popular:':consulta[0][-2]}


def Consultas_por_opcao(cursor, indice_escolhido, dado):
    print(indice_escolhido == "1")
    if indice_escolhido == "1":
        cursor.execute(f'''
            SELECT d.id
            FROM Doenca AS d
            JOIN NomesPopulares AS np ON d.id = np.doenca_id
            WHERE np.nomes_populares = ?
        ''', (dado,))
        doenca_id = cursor.fetchall()[0][0]
    elif indice_escolhido == "2":
        cursor.execute(f'''
            SELECT d.id
            FROM Doenca AS d
            WHERE d.nome = ?
        ''', (dado,))
        doenca_id = cursor.fetchall()[0][0]

    elif indice_escolhido == "3":
        cursor.execute(f'''
            SELECT d.id
            FROM Doenca AS d
            WHERE d.cid = ?
        ''', (dado,))
        doenca_id = cursor.fetchall()[0][0]

    elif indice_escolhido == "4":
        cursor.execute(f'''
            SELECT d.id
            FROM Doenca AS d
            JOIN Patogeno AS p ON d.patogeno_id = p.id
            WHERE p.nome_cientifico = ?
        ''', (dado,))
        doenca_id = cursor.fetchall()[0][0]

    obter_dados_doenca(cursor, doenca_id)

# Verifica se o sintoma já existe a partir de seu nome:
def verificar_sintoma(cursor, nome_sintoma):
  cursor.execute('SELECT COUNT(*) FROM Sintoma WHERE nome = ?', [nome_sintoma])
  count = cursor.fetchone()[0]
  return count > 0

# Gera o relatorio de uma doença especifica
# Tem que verificar antes se o nome da doença é valido
def gerar_relatorio_doenca_especifica(cursor, nome_doenca):

    # Obtém os dados da doença
    cursor.execute('''
        SELECT d.id, d.nome, d.cid, p.nome_cientifico, t.tipo
        FROM Doenca AS d
        JOIN Patogeno AS p ON d.patogeno_id = p.id
        JOIN TipoDePatogeno AS t ON p.tipopatogeno_id = t.id
        WHERE d.nome = ?
    ''', [nome_doenca])

    doenca_dados = cursor.fetchone()

    doenca_id, nome_doenca, cid, patogeno, tipo_patogeno = doenca_dados

    # Obtém os nomes populares
    cursor.execute('''
        SELECT nomes_populares
        FROM NomesPopulares np
        JOIN Doenca d ON np.doenca_id = d.id
        WHERE d.nome = ?
    ''', [nome_doenca])

    nomes_populares = cursor.fetchall()

    # Verifica se existe ou não nomes populares cadastrados na doença especifica
    if nomes_populares:
        nomes_populares = ', '.join([np[0] for np in nomes_populares])

    else:
        nomes_populares = 'Nenhum nome popular cadastrado'

    cursor.execute('''
        SELECT GROUP_CONCAT(CONCAT(s.nome, ' (', t.nivel_ocorrencia, ')') ORDER BY 
            CASE 
                WHEN t.nivel_ocorrencia = 'muito comum' THEN 1
                WHEN t.nivel_ocorrencia = 'comum' THEN 2
                WHEN t.nivel_ocorrencia = 'pouco comum' THEN 3
                WHEN t.nivel_ocorrencia = 'raro' THEN 4
                ELSE 5
            END
            SEPARATOR ', ') AS sintomas
        FROM Doenca AS d
        JOIN TaxaDeOcorrencia AS t ON d.id = t.doenca_id
        JOIN Sintoma AS s ON t.sintoma_id = s.id
        WHERE d.nome = ?
        GROUP BY d.id;
    ''', [nome_doenca])
    
    result = cursor.fetchone()

    if result:
        sintomas_taxas = result[0]

    else:
        sintomas_taxas = 'Nenhum sintoma registrado'

    # Cria o PDF
    nome_arquivo = f"Relatório da Doença {nome_doenca}.pdf"
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Estilos
    styles = getSampleStyleSheet()
    elements = []

    # Cabeçalho
    header = f"Relatório da Doença: {nome_doenca}"
    elements.append(Paragraph(header, styles['Title']))
    elements.append(Spacer(1, 12))

    # Adiciona os dados da doença no PDF
    elements.append(Paragraph(f"<b>ID:</b> {doenca_id}", styles['Normal']))
    elements.append(Paragraph(f"<b>Nome:</b> {nome_doenca}", styles['Normal']))
    elements.append(Paragraph(f"<b>CID:</b> {cid}", styles['Normal']))
    elements.append(Paragraph(f"<b>Nomes Populares:</b> {nomes_populares}", styles['Normal']))
    elements.append(Paragraph(f"<b>Patógeno:</b> {patogeno}", styles['Normal']))
    elements.append(Paragraph(f"<b>Tipo do Patógeno:</b> {tipo_patogeno}", styles['Normal']))
    elements.append(Paragraph(f"<b>Sintomas e Taxa de Ocorrência:</b> {sintomas_taxas}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Gera o PDF
    doc.build(elements)

    # Salva o PDF
    with open(nome_arquivo, 'wb') as f:
        f.write(buffer.getvalue())

    print(f"Relatório gerado: {nome_arquivo}")


# Gera o relatorio de doenças mais provaveis apartir de uma lista de sintomas
# Tem que verificar antes se todos sintomas da lista são validos
# Tem que obter o id de cada sintoma e passar a lista de id dos sintomas e nome dos sintomas
def gerar_relatorio_doencas_mais_provaveis(cursor, sintomas_id, nome_sintomas):
    aux = ', '.join('?' for _ in sintomas_id)
    
    # Executa a consulta de doenças mais prováveis com base nos sintomas, Consulta "h" do tp 1
    cursor.execute(f'''
        SELECT d.id, d.nome, d.cid, p.nome_cientifico, t.tipo, 
        SUM(
            CASE 
               WHEN tdo.sintoma_id IN ({aux}) THEN 
                    CASE tdo.nivel_ocorrencia
                        WHEN 'muito comum' THEN 5
                        WHEN 'comum' THEN 4
                        WHEN 'pouco comum' THEN 3
                        WHEN 'raro' THEN 2
                        WHEN 'muito raro' THEN 1
                        ELSE 0
                    END
               ELSE 0
            END
        ) -
        (SELECT COUNT(*)
            FROM Sintoma s
            LEFT JOIN TaxaDeOcorrencia t ON s.id = t.sintoma_id AND t.doenca_id = d.id
            WHERE s.id IN ({aux})
              AND t.sintoma_id IS NULL
        ) AS pontuacao
        FROM Doenca AS d
        LEFT JOIN Patogeno AS p ON d.patogeno_id = p.id
        LEFT JOIN TipoDePatogeno AS t ON p.tipopatogeno_id = t.id
        LEFT JOIN TaxaDeOcorrencia tdo ON d.id = tdo.doenca_id
        LEFT JOIN Sintoma s ON tdo.sintoma_id = s.id
        GROUP BY d.id
        ORDER BY pontuacao DESC;
    ''', sintomas_id + sintomas_id)
    
    # Obter todas as doenças
    doencas = cursor.fetchall()

    # Configura o PDF
    nome_arquivo = "Relatório das Doencas mais provaveis.pdf"
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Estilos
    styles = getSampleStyleSheet()
    elements = []

    # Cabeçalho
    header = f"Relatório das Doenças Mais Prováveis para os sintomas: {', '.join(nome_sintomas)}"
    elements.append(Paragraph(header, styles['Title']))
    elements.append(Spacer(1, 12))
    
    for doenca in doencas:
        doenca_id, nome_doenca, cid, patogeno, tipo_patogeno, pontuacao = doenca

        # Obtém os nomes populares
        cursor.execute('''
            SELECT nomes_populares
            FROM NomesPopulares np
            JOIN Doenca d ON np.doenca_id = d.id
            WHERE d.nome = ?
        ''', [nome_doenca])

        nomes_populares = cursor.fetchall()

        # Verifica se existe ou não nomes populares cadastrados na doença especifica
        if nomes_populares:
            nomes_populares = ', '.join([np[0] for np in nomes_populares])

        else:
            nomes_populares = 'Nenhum nome popular cadastrado'

        # Obtém os sintomas e taxas de ocorrência da mesma forma da consulta "c" no TP1
        cursor.execute('''
            SELECT GROUP_CONCAT(CONCAT(s.nome, ' (', t.nivel_ocorrencia, ')') ORDER BY 
                CASE 
                    WHEN t.nivel_ocorrencia = 'muito comum' THEN 1
                    WHEN t.nivel_ocorrencia = 'comum' THEN 2
                    WHEN t.nivel_ocorrencia = 'pouco comum' THEN 3
                    WHEN t.nivel_ocorrencia = 'raro' THEN 4
                    ELSE 5
                END
                SEPARATOR ', ') AS sintomas
            FROM Doenca AS d
            JOIN TaxaDeOcorrencia AS t ON d.id = t.doenca_id
            JOIN Sintoma AS s ON t.sintoma_id = s.id
            WHERE d.nome = ?
            GROUP BY d.id;
        ''', [nome_doenca])
        
        result = cursor.fetchone()

        if result:
            sintomas_taxas = result[0]
            
        else:
            sintomas_taxas = 'Nenhum sintoma registrado'
                
        # Adiciona os dados da doença no PDF
        elements.append(Paragraph(f"<b>Relatório da Doença:</b> {nome_doenca}", styles['Heading2']))
        elements.append(Paragraph(f"<b>ID:</b> {doenca_id}", styles['Normal']))
        elements.append(Paragraph(f"<b>Nome:</b> {nome_doenca}", styles['Normal']))
        elements.append(Paragraph(f"<b>CID:</b> {cid}", styles['Normal']))
        elements.append(Paragraph(f"<b>Nomes Populares:</b> {nomes_populares}", styles['Normal']))
        elements.append(Paragraph(f"<b>Patógeno:</b> {patogeno}", styles['Normal']))
        elements.append(Paragraph(f"<b>Tipo do Patógeno:</b> {tipo_patogeno}", styles['Normal']))
        elements.append(Paragraph(f"<b>Sintomas e Taxa de Ocorrência:</b> {sintomas_taxas}", styles['Normal']))
        elements.append(Spacer(1, 12))
    
    # Gera o PDF
    doc.build(elements)

    # Salva o PDF
    with open(nome_arquivo, 'wb') as f:
        f.write(buffer.getvalue())

    print(f"Relatório gerado: {nome_arquivo}")

# Funcionalidade 3
# Tem que verificar antes se todos os sintomas passados são válidos
def listar_doencas(cursor, sintomas_id):
    aux = ', '.join('?' for _ in sintomas_id)

    # Consulta as doenças mais prováveis com base nos sintomas
    cursor.execute(f'''
        SELECT d.id, d.nome, d.cid, p.nome_cientifico, t.tipo,
        SUM(
            CASE 
               WHEN tdo.sintoma_id IN ({aux}) THEN 
                    CASE tdo.nivel_ocorrencia
                        WHEN 'muito comum' THEN 5
                        WHEN 'comum' THEN 4
                        WHEN 'pouco comum' THEN 3
                        WHEN 'raro' THEN 2
                        WHEN 'muito raro' THEN 1
                        ELSE 0
                    END
               ELSE 0
            END
        ) -
        (SELECT COUNT(*)
            FROM Sintoma s
            LEFT JOIN TaxaDeOcorrencia t ON s.id = t.sintoma_id AND t.doenca_id = d.id
            WHERE s.id IN ({aux})
              AND t.sintoma_id IS NULL
        ) AS pontuacao
        FROM Doenca AS d
        LEFT JOIN Patogeno AS p ON d.patogeno_id = p.id
        LEFT JOIN TipoDePatogeno AS t ON p.tipopatogeno_id = t.id
        LEFT JOIN TaxaDeOcorrencia tdo ON d.id = tdo.doenca_id
        LEFT JOIN Sintoma s ON tdo.sintoma_id = s.id
        GROUP BY d.id
        ORDER BY pontuacao DESC;
    ''', sintomas_id + sintomas_id)
    
    # Obter todas as doenças
    doencas = cursor.fetchall()

    # Calculando o número total de páginas (10 é o número de doenças por página)
    if (len(doencas) % 10) == 0:
        len(doencas) // 10
    else:
        total_paginas = (len(doencas) // 10) + 1

    # Determina qual pagina esta sendo mostrado
    pagina_atual = 1
    
    while True:
        limpar_tela()
        inicio = (pagina_atual - 1) * 10
        fim = inicio + 10
        
        # Exibe as doenças da página atual
        print(f"\nDoenças na página {pagina_atual}:")
        for i in range(inicio, fim):
            if i < len(doencas):
                doenca = list(doencas[i])
                print(f"{i + 1} - Nome: {doenca[1]}")

        opcao=input("Escolha uma opção:\n [1] -> Selecionar página.\n[2] -> Selecionar Doença\n[3] -> Retornar para o menu\n")
        
        if opcao == "1":
            pagina_atual=int(input(f"Digite o número da página entre 1 e {total_paginas}: "))

            # print(type(pagina_atual), type(total_paginas))
            if pagina_atual < 1 or pagina_atual > total_paginas:
                print(f"Insira um número de página válido entre 1 e {total_paginas}.")
                pass

        elif opcao == "2":
            # Solicita o número da doença pra mostrar os dados dela
            num_da_doenca = int(input("\nInsira o número da doença que deseja obter os dados: "))
            
            if num_da_doenca <= 0 or num_da_doenca > len(doencas):
                print("Insira um número de doença válido.")
                pass

            else:
                doenca = doencas[num_da_doenca - 1]
                obter_dados_doenca(cursor, doenca[0])

        elif opcao == "3":
            # registrar_operacao("--Retornando ao Menu--",None)
            # False
            break            

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")  # Pausa para leitura

    return

# Função apenas para obter os dados da doença escolhida para a funcionalidade 4
def obter_dados_doenca(cursor, doenca_id):
    # Consulta para mostrar todos os dados de uma doença
    cursor.execute(f'''
        SELECT d.id AS doenca_id, d.nome AS nome_doenca, d.cid AS cod_doenca,
            GROUP_CONCAT(DISTINCT n.nomes_populares SEPARATOR ', ') AS nomes_populares,
            p.nome_cientifico AS patogeno, tp.tipo AS tipo_patogeno,
            GROUP_CONCAT(CONCAT(s.nome, ' (', t.nivel_ocorrencia, ')') ORDER BY 
                CASE 
                    WHEN t.nivel_ocorrencia = 'muito comum' THEN 1
                    WHEN t.nivel_ocorrencia = 'comum' THEN 2
                    WHEN t.nivel_ocorrencia = 'pouco comum' THEN 3
                    WHEN t.nivel_ocorrencia = 'raro' THEN 4
                    ELSE 5
                END
                SEPARATOR ', ') AS sintomas_taxas
        FROM Doenca AS d
        LEFT JOIN NomesPopulares AS n ON d.id = n.doenca_id
        LEFT JOIN Patogeno AS p ON d.patogeno_id = p.id
        LEFT JOIN TipoDePatogeno AS tp ON p.tipopatogeno_id = tp.id
        LEFT JOIN TaxaDeOcorrencia AS t ON d.id = t.doenca_id
        LEFT JOIN Sintoma AS s ON t.sintoma_id = s.id
        WHERE d.id = ?
        GROUP BY d.id;
    ''', [doenca_id])

    # Obtem os dados da doença
    doenca = cursor.fetchall()

    doenca = list(doenca[0])

    doenca_id, nome_doenca, cod_doenca, nomes_populares, patogeno, tipo_patogeno, sintomas_taxas = doenca
    limpar_tela()
    print(f"ID da Doença: {doenca_id}")
    print(f"Nome da Doença: {nome_doenca}")
    print(f"CID da Doença: {cod_doenca}")
    print(f"Nomes Populares: {nomes_populares}")
    print(f"Patógeno: {patogeno}")
    print(f"Tipo de Patógeno: {tipo_patogeno}")
    print(f"Sintomas e Taxas de Ocorrência: {sintomas_taxas}")
    input("\nPressione Enter para continuar...")  # Pausa para leitura
