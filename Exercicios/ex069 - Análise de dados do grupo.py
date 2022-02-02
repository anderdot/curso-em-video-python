# Desafio 069: Crie um programa que leia a idade e o sexo de varias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não 
# continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos
from cores import cor

pessoa = 1
maior18 = totalM = m20 = 0
while True:
    print('~' * 40)
    print(f'cadastro da {pessoa}º pessoa.')
    while True:
        idade = int(input('idade: '))
        if idade > 0:
            break
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            break
        
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        totalM += 1
    elif idade > 20:
        m20 += 1
    
    while True:
        escolha = input('Deseja cadastrar mais pessoas? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
    pessoa += 1
print('~' * 40)
print(f'{cor.verde}{maior18}{cor.reset} são maiores de 18 anos.')
print(f'{cor.verde}{totalM}{cor.reset} homens foram cadastrados.')
print(f'{cor.verde}{m20}{cor.reset} mulheres tem mais de 20 anos.')
