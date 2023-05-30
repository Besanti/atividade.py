import csv

def listar.conteudo('starwars.csv'):
    with open('starwars.csv', 'r') as arquivo.csv:
        leitor_csv = csv.reader(arquivo.csv)
        for linha in leitor_csv:
            print(linha)
           
            arquivo.csv = 'This Pc/Downloads/articles.csv'
listar.conteudo(arquivo.csv)
