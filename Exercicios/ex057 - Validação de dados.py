# Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter
# um valor correto.
from cores import cor

sexo = input('informe seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MF':
    print('Dados inválidos. Por favor, ', end = '')
    sexo = input('informe seu sexo [M/F]: ').upper().strip()[0]
print('Sexo {1}{2}{0} registrado com {1}sucesso{0}.'.format(
    cor.reset,
    cor.verde,
    sexo,
))
    
