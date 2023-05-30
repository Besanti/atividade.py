import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('starwars.csv')

arq = open('starwars.csv')
for registro in csv.DictReader(arq, delimiter=','):

  print(registro)
