# Desafio 025: Verificar se um nome tem silva.
from cores import cor

nome = input('Digite seu nome: ').strip().lower()
print('O seu nome {}{}{} Silva.'.format(
    cor.verde,
    'tem' if 'silva' in nome else 'não tem',
    cor.reset))
