# eita
def fatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é {fatorial(numero)}')
