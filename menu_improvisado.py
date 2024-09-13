#Fazer um código em python que manda para o banco de dados uma doença à ser inserida.

from conexao_bd import *
from consultas import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from func_verificacoes import *
import os
import datetime


def Insert_dados_doenca(cursor):
    nomes_populares=[]
    sintomas={}
    while True:
        limpar_tela()
        print("CADASTRO DE DOENÇAS:")
        
        while True:
            cid = input("Digite o CID (ou 'voltar' para retornar ao menu): ")
            if cid.lower() == 'voltar':
                break
            if verificar_cid_existe(cursor,cid):
                print(f'CID já cadastrado: {cid}')
            else:
                break
        if cid.lower() == 'voltar':
            break

        while True:
            nome_tecnico = input("Digite o nome técnico da doença: ")
            if verificar_doenca(cursor,nome_tecnico):
                print(f"Doenca já cadastrada: {nome_tecnico}")
            else:
                break
    
        patogeno = input("Digite o patógeno: ")
        tipo_patogeno=input("Digite o tipo de patógeno: ")
        if verificar_tipo_patogeno(cursor,tipo_patogeno):
            tipo_patogeno_id=obter_id_tipo_patogeno(cursor,tipo_patogeno)
        else:
            tipo_patogeno_id=cadastrar_tipo_patogeno(cursor,tipo_patogeno)
        if not verificar_patogeno(cursor,patogeno):
            cadastrar_patogeno(cursor,patogeno,tipo_patogeno_id)
        patogeno_id=obter_id_patogeno(cursor, patogeno)

        while op.lower() != 'n':
            sintoma = input("Digite o sintoma: ")
            while True:
                nivel_de_ocorrencia = input("Digite o nível de ocorrência \n('muito raro', 'raro', 'pouco comum', 'comum', 'muito comum'): ")
                if nivel_de_ocorrencia not in ['muito raro', 'raro', 'pouco comum', 'comum', 'muito comum']:
                    print("Nível de ocorrência fora do padrão, tente novamente.")
                else:
                    break
            if not verificar_sintoma(cursor,sintoma):
                cadastrar_sintoma(cursor,sintoma)
            sintomas[sintoma]=nivel_de_ocorrencia
            op=input('Deseja cadastrar mais? (Y/n): ')

        op=''
        
        while op.lower() != 'n':
            nome_popular = input("Digite o nome popular: ")
            op=input('Deseja cadastrar mais? (Y/n): ')
            nomes_populares.append(nome_popular)

        dados = f"CID: {cid} Nome Técnico: {nome_tecnico} \nNome Popular: {nomes_populares} \nPatógeno: {patogeno} \nSintomas: {sintomas}"

        doenca_id=cadastrar_doenca(cursor,cid,nome_tecnico,patogeno_id)

        for nome in nomes_populares:
            cadastrar_nome_popular(cursor,nome,doenca_id)

        for sintoma,taxa_raridade in sintomas.items():
            sintoma_id=obter_id_sintoma(cursor,sintoma)
            inserir_taxa_ocorrencia(cursor,doenca_id,sintoma_id,taxa_raridade)
        
        registrar_operacao("Cadastrar Doença", dados)
 
        print("Doença cadastrada com sucesso.")
        input("\nPressione Enter para voltar ao menu...")
        break


def Emissao_de_relatorios(cursor):
    while True:
        limpar_tela()
        tipo_relatorio=input("TIPOS DE RELATORIO:\n [1]- RELATORIO CONTENDO DADOS DE UMA DOENÇA ESPECÍFICA \n [2]- RELATORIO DE DOENÇAS MAIS PROVAVEIS COM BASE EM UM CONJUNTO DE SINTOMAS\n 3- VOLTAR\nOPÇÃO (1,2 ou 3):")
        if tipo_relatorio == "1":
            nome_doenca=input("Digite o nome técnico da doença")
            if verificar_doenca(cursor,nome_doenca):
                gerar_relatorio_doenca_especifica(cursor,nome_doenca)
            else:
                print("Doença não encontrada!")
            dados=f"\nNome da doença: {nome_doenca}"
            registrar_operacao("Emissão de relatorios",dados)
        elif tipo_relatorio == "2":
            lista_sintomas=[]
            lista_sintomas_id=[]
            op=''
            while op.lower() != 'n':
                sintoma=input("Digite o sintoma: ")
                if verificar_sintoma(cursor,sintoma):
                    lista_sintomas.append(sintoma)
                    lista_sintomas_id.append(obter_id_sintoma(cursor,sintoma))
                op=input('Deseja cadastrar mais? (Y/n): ')
            gerar_relatorio_doencas_mais_provaveis(cursor,lista_sintomas_id,lista_sintomas)
            dados=f"\nSintomas: {lista_sintomas}"
            registrar_operacao("Emissão de relatorios",dados)
        elif tipo_relatorio == "3":
            break
        else:
            print("OPÇÃO INVALIDA")

# def Consultas_por_opcao(cursor, indice_escolhido, dado):
#     colunas = ['CID', 'nome', 'nome_popular', 'patogeno_id']

#     if(indice_escolhido != 2):
#         b = cursor.execute('select * from doenca ? = ?', [colunas[indice_escolhido], dado])
#     else:
#         b = cursor.execute('select * from doenca join nomespopulares on doenca.id = nomespopulares.doenca_id where nomespopulares.nomes_populares = ?', [colunas[indice_escolhido]])
#     print(b)

def Pesquisa_Doencas(cursor):
    while True:
        limpar_tela()
        opcao=input("PESQUISA DE DOENÇAS\n [1] -> Nome Popular\n[2] -> Nome técnico\n[3] -> CID\n[4] -> Patogeno\n[5] -> SAIR\n OPÇÂO")
        if opcao == "1":
            Nome_popular=input("Digite um Nome popular: ")
            Consultas_por_opcao(cursor,opcao,Nome_popular)
            dados=f"\nNome-Popular: {Nome_popular}"
            registrar_operacao("Pesquisar Doença",dados)
        elif opcao == "2":
            Nome_Tecnico=input("Digite o Nome técnico: ")
            Consultas_por_opcao(cursor,opcao,Nome_Tecnico)
            dados=f"\nNome-Popular: {Nome_Tecnico}"
            registrar_operacao("Pesquisar Doença",dados)
        elif opcao == "3":
            CID=input("Digite o CID da Doença: ")
            Consultas_por_opcao(cursor,opcao,CID)
            dados=f"\nNome-Popular: {CID}"
            registrar_operacao("Pesquisar Doença",dados)
        elif opcao == "4":
            Patogeno=input("Digite o Patogeno: ")
            Consultas_por_opcao(cursor,opcao,Patogeno)
            dados=f"\nNome-Popular: {Patogeno}"
            registrar_operacao("Pesquisar Doença",dados)

def Apoio_Diagnostico(cursor):
     while True:
        limpar_tela()
        lista_sintomas=[]
        lista_sintomas_id=[]
        op=''
        while op.lower() != 'n':
            sintoma=input("Digite o sintoma: ")
            if verificar_sintoma(cursor,sintoma):
                lista_sintomas.append(sintoma)
                lista_sintomas_id.append(obter_id_sintoma(cursor,sintoma))
                op=input('Deseja cadastrar mais? (Y/n): ')
            else:
                print("SINTOMA NÃO CADASTRADO-TENTE NOVAMENTE")
        listar_doencas(cursor,lista_sintomas_id)
        dados=f"\nSintomas: {lista_sintomas}"
        registrar_operacao("Apoio Diagnostico:", dados)

        
def menu(crusor):
    while True:
        limpar_tela()
        print("Menu Principal:")
        print("1. Cadastrar doenca")
        print("2. Consulta ao Catálogo de Doenças")
        print("3. Apoio ao Diagnóstico")
        print("4. Emissao de relatorios")
        print("5. Sair")
        opcao = input("Escolha uma opção (1-4): ")
        if opcao == "1":
            Insert_dados_doenca(cursor)
        elif opcao == "2":
            Pesquisa_Doencas(cursor)
        elif opcao == "3":
            Apoio_Diagnostico(cursor)
        elif opcao == "4":
            Emissao_de_relatorios(cursor)
        elif opcao == "5":
            registrar_operacao("--SAIDA DO SISTEMA--",None)
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")  # Pausa para leitura


if __name__=="__main__":
    registrar_operacao("--ENTRADA NO SISTENMA--", None)
    cursor = cursor.cursor()
    menu(cursor)
