# Trabalho Final - Banco de Dados

Este repositório contém um sistema para gerenciar doenças, seus patógenos associados e sintomas, além de gerar relatórios baseados nesses dados. O sistema utiliza consultas SQL integrado a uma API para interagir com o banco de dados e permite o cadastro e a recuperação de informações relacionadas a doenças, sintomas e patógenos.

## Configurações de uso

Antes de utilizar o sistema, certifique-se de que você tem as bibliotecas necessárias instaladas. As principais dependências incluem uma biblioteca para conexão com o banco de dados (como sqlite3) e uma para geração de PDFs (como reportlab). Para instalá-las, execute:

```dart
    pip install reportlab
```

### Configuração do Banco de Dados

O código faz referência a uma conexão de banco de dados através do módulo conexao_db. Certifique-se de que o arquivo conexao_db.py esteja configurado corretamente e forneça uma conexão válida com o banco de dados.

### Execução do Código

Salve o Código: Salve o código fornecido em um arquivo com a extensão .py, por exemplo, sistema_doencas.py.

### Execute o Código:

Abra um terminal ou prompt de comando.
Navegue até o diretório onde o arquivo Python está salvo.
Execute o código com o seguinte comando:

```dart
    python sistema_doencas.py
```

## Funcionalidades

- **Listar Doenças**: Exibe todas as doenças cadastradas no banco de dados.
- **Cadastrar Doença**: Adiciona uma nova doença ao sistema.
- **Cadastrar Sintoma**: Registra novos sintomas.
- **Cadastrar Patógeno**: Insere novos patógenos e tipos de patógenos.
- **Gerar Relatório de Doença Específica**: Cria um relatório detalhado de uma doença específica em formato PDF.
- **Gerar Relatório de Doenças Mais Prováveis**: Gera um relatório com base em sintomas fornecidos, exibindo as doenças mais prováveis.

## Requisitos

- Python 3.x
- SQLite3
- Bibliotecas: reportlab

## Colaboradores

- João Gustavo Silva Guimarães
- João Marcos Silva Hess
- João Pedro Freitas de Paula Dias
- Leandro Sousa Costa
