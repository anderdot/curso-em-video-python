# Desafio 109: Modifique as funções que form criadas no desafio 107 para que 
# elas aceitem um parâmetro a mais, informando se o valor retornado por elas 
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from rotinas import titulo
from modulos.ex109 import moeda as m

valor = int(input('Digite um valor: R$ '))
titulo('Análise', 50)
print(f'A metade de {m.moeda(valor)} é {m.metade(valor, True)}.')
print(f'O dobro de {m.moeda(valor)} é {m.dobro(valor, True)}.')
print(f'A taxa de 10% de {m.moeda(valor)} é {m.aumentar(valor, 10, True)}.')
print(f'O desconto de 15% de {m.moeda(valor)} é {m.diminuir(valor, 15, True)}.')
