# Desafio 103: Faça um programa que tenha uma função chamada ficha(), que 
# receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele 
# marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo 
# que algum dado não tenha sido informado corretamente.
from rotinas import var, titulo

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {var(nome)} fez {var(gols)} gol(s)')
    

titulo('Ficha do jogador', 40)
n = input('Digite o nome: ')
g = input('Digite o número de gols: ')
g = int(g) if g.isnumeric() else 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
    