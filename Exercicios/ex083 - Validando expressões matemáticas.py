# Desafio 083: Crie um programa que o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta. 
from cores import cor

expressao = input('Digite sua expressão: ')
pilha = []
for p in expressao:
    if p == '(':
        pilha.append(p)
    elif p == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(p)
            break
print('Sua expressão é {}{}.'.format(
    str(cor.verde) + 'válida' if len(pilha) == 0 else str(cor.vermelho) + 'inválida',
    cor.reset
))
