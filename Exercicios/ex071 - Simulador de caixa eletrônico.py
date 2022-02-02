# Desafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No inicio pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada serão entregues
# obs. Considere que o caixa possui cédulas de R$ 50, 20, 10 e 1.
from cores import cor

while True:
    valor = int(input('Digite o valor a ser sacado. R$: '))
    if valor > 0:
        break
    
total = valor
cedula = 50
qtdCedula = 0
print(f'{" Boca do caixa ":~^40}')
while True:
    if total >= cedula:
        total -= cedula
        qtdCedula += 1
    else:
        if qtdCedula > 0:
            print('Total de {1}{2}{0} cédulas de R$ {1}{3}{0} {4}.'.format(
                cor.reset,
                cor.verde,
                qtdCedula,
                cedula,
                'real' if cedula == 1 else 'reais'
            ))
        qtdCedula = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
        
# Jeito porco que eu tinha feito
# nota50 = valor // 50
# total50 = valor % 50

# nota20 = total50 // 20
# total20 = total50 % 20

# nota10 = total20 // 10
# nota1 = total20 % 10

# print(f'{" Boca do caixa ":~^40}')
# print(f'Cédulas de 50: {nota50}')
# print(f'Cédulas de 20: {nota20}')
# print(f'Cédulas de 10: {nota10}')
# print(f'Cédulas de 01: {nota1}')
