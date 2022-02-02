# Desafio 037: escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal 
from cores import cor

numero = int(input('Digite um número: '))
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
escolha = int(input('Escolha qual base: '))
if escolha == 1:
    print('O número {1}{2}{0} convertido em {1}binário{0} é {1}{3}{0}.'.format(
        cor.reset, 
        cor.verde,
        numero,
        bin(numero)[2:]))
elif escolha == 2:
    print('O número {1}{2}{0} convertido em {1}Octal{0} é {1}{3}{0}.'.format(
        cor.reset, 
        cor.verde,
        numero,
        oct(numero)[2:]))
elif escolha == 3:
    print('O número {1}{2}{0} convertido em {1}Hexadecimal{0} é {1}{3}{0}.'.format(
        cor.reset, 
        cor.verde,
        numero,
        hex(numero)[2:]))
else:
    print('Opção Inválida!')
    