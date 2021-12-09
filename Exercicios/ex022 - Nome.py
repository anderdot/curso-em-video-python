# Desafio 022: Ler o nome completo de uma pessoa, deixar em maiusculo e 
# minusculo, contar a quantidade de letras e quantas letras tem o primeiro nome.
from cores import cor

nome = input('Digite seu nome: ').strip()
print('Maiúsculo: {}{}{}'.format(cor.verde, nome.upper(), cor.reset))
print('Minusculo: {}{}{}'.format(cor.verde, nome.lower(), cor.reset))
print('Quantidade de letras: {}{}{}'.format(
    cor.verde,
    len(nome) - nome.count(' '),
    cor.reset))
# print('Primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Primeiro nome: {}{}{}'.format(cor.verde, separa[0], cor.reset))
print('Primeiro nome tem {}{}{} letras'.format(cor.verde, len(separa[0]), cor.reset))
