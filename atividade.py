import csv
import pandas as pd
import requests

df = pd.read_csv('starwars.csv')

arq = open('starwars.csv')
for registro in csv.DictReader(arq, delimiter=','):

  print(registro)
