from pymarc import MARCReader
import csv
import os
import sys

from escrever_csv import *
from extrair_metadados import *      
        
metadados = []    
for _,_, i in os.walk('marc'):
    for j in i:
        metadados.append(extrair_metadados(j))

escrever_csv(metadados)
