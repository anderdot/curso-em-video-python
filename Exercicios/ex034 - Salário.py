# Desafio 034: Escreva um programa que pergunte o salário de um funcionario e 
# calcule o valor do seu aumento. 
# para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, um aumento de 15%.
from cores import cor

salario = float(input('Digite seu salário: R$ '))
reajuste = salario * 10 / 100
if salario <= 1250:
    reajuste += salario * 5 / 100
print('Com o reajuste seu salário de R$ {}{:.2f}{} reais aumentará para R$ {}{:.2f}{} reais.'.format(
    cor.verde,
    salario,
    cor.reset,
    cor.verde,
    salario + reajuste,
    cor.reset))
