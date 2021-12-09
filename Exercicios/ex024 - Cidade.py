# Desafio 024: Mostre se uma pessoa nasceu ou não em uma cidade que começa com 'santo'.
from cores import cor

cidade = input('Digite a cidade onde nasceu: ').strip().lower()
print('Essa cidade possui {1}Santo{0} no nome? {1}{2}{0}.'.format(
    cor.reset,
    cor.verde,
    'Sim' if cidade[:5] == 'santo' else 'Não'))
