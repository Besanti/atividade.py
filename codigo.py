import csv

def listar_conteudo(starwars_csv):
    with open(starwars_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)
           
            arquivo_csv = 'This Pc/Downloads/starwars.csv'
listar_conteudo(arquivo_csv)
