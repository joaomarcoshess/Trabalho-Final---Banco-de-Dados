from os import system, name
import datetime

def registrar_operacao(tipo_operacao, dados):
    with open("log_operacoes.txt", "a") as log:
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{agora} - {tipo_operacao} - {dados}\n")


def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def string_cleaner(string):
    word = []

    for letter in string:

        if letter == "'" or letter == "(" or letter == ")" or letter == ",":
            pass
        
        else:
            word.append(letter)

    return word

def verificar_entrada(palavra_de_entrada):
    if palavra_de_entrada in ['sim', 'siM', 'sIM', 'SIM', 'Sim', 'SIm', 'SiM', 's', 'S', '1', 'y', 'Y', 'yes', 'Yes', 'YES']:
        return True
    else:
        return False


