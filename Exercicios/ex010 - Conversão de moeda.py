# Desafio 010: Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre 
# quantos dolares ela pode compra.
from cores import cor

reais = float(input('Digite quanto dinheiro você tem: R$ '))
print('Com R$ {:.2f} reais, você pode comprar US$ {}{:.2f}{} dolares.'.format(
    reais, 
    cor.verde,
    reais / 5.68, # kkkkk
    cor.reset)) 
