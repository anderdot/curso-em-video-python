# Desafio 102: Crie um programa que tenha uma função fatorial() que receba 
# dois parâmetros: o primeiro que indique o número a calcular e outro chamado 
# show, que será um valor lógico (opcional) indicando se será mostrado ou não 
# na tela o processo de cálculo do fatorial.
from rotinas import var, titulo

def fatorial(n, show=False):
    """Calcula o fatorial de um número

    Args:
        n (int): O número que será calculado o fatorial
        show (bool, optional): Se ira aparecer ou não o calculo. Defaults to False.

    Returns:
        int: O fatorial do número pedido.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{var(i)} {"x" if i > 1 else "="} ', end='')
        f *= i
    return f


help(fatorial)
titulo('Calcular o fatorial', 40)
numero = int(input('Digite um número: '))
while True:
    escolha = input('Deseja ver o cálculo? [S/N]: ').strip().upper()[0]
    if escolha in 'SN':
        break
titulo('Resultado', 40)
if escolha == 'S':
    print(f'O calculo foi [', end='')
    print(f'{var(fatorial(numero, True))}].')
else:
    print(f'O fatorial de {var(numero)} é {var(fatorial(numero))}.')
