# Desafio 032: Verifica se um ano digitado é bissexto.
from cores import cor
from datetime import date

ano = int(input('Digite um ano (0 para o atual): '))
if ano == 0:
    ano = date.today().year
print('O ano de {} {}{}{} bissexto.'.format(
    ano, 
    cor.verde, 
    'é' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'não é', 
    cor.reset))
