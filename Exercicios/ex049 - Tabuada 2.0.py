# Desafio 049: Refaça o desafio 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando o laço for.
from cores import cor

num = int(input('Digite um número: '))
print('-' * 15)
for i in range(1, 11):
    print('{} x {:2} = {}{}{}'.format(num, i, cor.verde, num * i, cor.reset))
print('-' * 15)
