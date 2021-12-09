# Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparecem a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.
from cores import cor
 
frase = input('Digite uma frase: ').strip().lower()
print('A letra "A" aparece {}{}{} vezes.'.format(cor.verde, frase.count('a'), cor.reset))
print('Primeira vez em {}{}{}.'.format(cor.verde, frase.find('a') + 1, cor.reset))
print('Última vez em {}{}{}.'.format(cor.verde, frase.rfind('a') + 1, cor.reset))
