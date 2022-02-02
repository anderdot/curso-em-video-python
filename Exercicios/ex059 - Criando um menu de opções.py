# Desafio 058: Crie um programa que leia dois valores e mostre um menu como o abaixo.
# Seu programa deverá realizar a operação solicitada em cada caso.
# [1] Somar 
# [2] Multiplicar 
# [3] Maior
# [4] Novos números 
# [0] Sair
from cores import cor

novos = True
div = '-==-' * 8
print(div)

while True:
    if novos:
        n1 = float(input('Digite o 1º número: '))
        n2 = float(input('Digite o 2º número: '))
        novos = False;
        print(div)
    else:
        print(div)
    print(' [1] Somar')
    print(' [2] Multiplicar')
    print(' [3] Maior')
    print(' [4] Novos números')
    print(' [0] Sair')
    opcao = int(input('> '))
    print(div)
    
    if opcao == 0:
        break;
    elif opcao == 1:
        print('A soma de {1}{2}{0} e {1}{3}{0} é {1}{4}{0}.'.format(
            cor.reset,
            cor.verde,
            n1,
            n2,
            n1 + n2
        ))
    elif opcao == 2:
        print('A multiplicação de {1}{2}{0} e {1}{3}{0} é {1}{4}{0}.'.format(
            cor.reset,
            cor.verde,
            n1,
            n2,
            n1 * n2
        ))
    elif opcao == 3:
        print('O maior entre {1}{2}{0} e {1}{3}{0} é {1}{4}{0}.'.format(
            cor.reset,
            cor.verde,
            n1,
            n2,
            max(n1, n2)
        ))
    elif opcao == 4:
        novos = True;
    else:
        print('Entrada inválida!')
