# Desafio 013: Faça um programa que leia o salario de um funcionario e exiba novamente 
# com reajuste de 15%
from cores import cor

salario = float(input('Digite o salario do funcionario: R$ '))
print('O salário com reajuste de 15% é {}{:.2f}{} reais.'.format(
    cor.verde,
    salario + salario * 15 / 100,
    cor.reset))
