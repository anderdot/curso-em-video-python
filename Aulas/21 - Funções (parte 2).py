# Função de ajuda interativa
from re import A


help(print)

def contador1(i, f, p):
    """Faz uma contagem e mostra na tela.

    Args:
        i (int): Início da contagem
        f (int): Fim da contagem
        p (int): Passo da contagem
    """
    while i <= f:
        print(i, end=' ')
        i += p
    print('Fim')
    

help(contador1)
print('-==-' * 10)

def somar(a=0, b=0, c=0):
    print(f'A soma é {a + b + c}')
    
somar()
somar(1)
somar(1, 2)
somar(1, 2, 3)

print('-==-' * 10)

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    

a = 5
teste(a)
print(f'A fora vale {a}')

print('-==-' * 10)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print('Fatorial é', fatorial(5))