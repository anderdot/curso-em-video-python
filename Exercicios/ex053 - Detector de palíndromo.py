# Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um 
# palíndromo, desconsiderando os espaços.
from cores import cor

frase = input('Digite uma frase: ').strip()
# Separei a frase e depois juntei, pra eliminar espaços
junto = ''.join(frase.split())
inverso = junto[::-1] # for letra in range(len(junto) - 1, -1, -1):
print('A frase {1}{2}{0} inversa é {1}{3}{0}, logo {1}{4}{0} um palíndromo.'.format(
    cor.reset,
    cor.verde,
    junto,
    inverso,
    'é' if junto.lower() == inverso.lower() else 'não é'
))
