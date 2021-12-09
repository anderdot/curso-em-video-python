# Desenvolva um programa que leia duas notas de um aluno e calcule a média.
from cores import cor

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
print('A média das notas é {}{:.1f}{}.'.format(cor.verde, (n1 + n2) / 2, cor.reset))
