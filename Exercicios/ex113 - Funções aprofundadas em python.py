# Desafio 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from rotinas import var, titulo, err

def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except (ValueError, TypeError):
            print(err('Erro: Digite um número inteiro.'))
            continue
        else:
            return valor
    

def leiaFloat(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except (ValueError, TypeError):
            print(err('Erro: Digite um número real.'))
            continue
        else:
            return valor

titulo('Validação de entrada')
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Os números digitados foram {var(inteiro)} e {var(real)}')
