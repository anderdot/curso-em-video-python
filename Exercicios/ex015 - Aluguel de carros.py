# Desafio 015: Escreve um programa que pergunte a quantidade de km percorridos e os dias
# de aluguel. Calcule o quanto sera pago sabendo que custa R$60 por dia e 
# R$ 0.15 por km
from cores import cor

km = float(input('Digite quantos quilometros foi percorrido: ')) 
dias = int(input('Digite quantos dias de aluguel: '))
print('O total a pagar é R$ {}{:.2f}{} reais.'.format(
    cor.verde, 
    km * 0.15 + dias * 60, 
    cor.reset))
