# Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar 
# de forma semelhante 'a função input() do Python, só que fazendo a validação 
# para aceitar apenas um valor numérico.
from rotinas import var, titulo, err

def leiaInt(texto):
    while True:
        n = input(texto)
        if n.isnumeric():
            return int(n)
        print(f'{err("Erro: Digite um número inteiro.")}')
    
    
titulo('Lendo dados', 40)
numero = leiaInt('Digite um número: ')
print(f'Você digitou {var(numero)} que é um número inteiro.')