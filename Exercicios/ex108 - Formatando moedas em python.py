# Desafio 108: Adapte o código do desafio #107, criando uma função adicional 
# chamada moeda() que consiga mostrar os números como um valor monetário 
# formatado.
from rotinas import var, titulo
from modulos.ex108 import moeda as m

valor = int(input('Digite um valor: R$ '))
titulo('Análise', 50)
print(f'A metade de {m.moeda(valor)} é {m.moeda(m.metade(valor))}.')
print(f'O dobro de {m.moeda(valor)} é {m.moeda(m.dobro(valor))}.')
print(f'A taxa de 10% de {m.moeda(valor)} é {m.moeda(m.aumentar(valor, 10))}.')
print(f'O desconto de 15% de {m.moeda(valor)} é {m.moeda(m.diminuir(valor, 15))}.')
