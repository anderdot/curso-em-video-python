# Desafio 036: Escreva um programa para aprovar o empréstimo bancário para comprar
# uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
# vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
# é negado.
from cores import cor

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite em quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
print('Uma casa no valor de R$ {1}{2:.2f}{0} reais para pagar em {1}{3}{0} anos, terá prestações de R$ {1}{4:.2f}{0} reais mensais.'.format(
    cor.reset,
    cor.verde, 
    casa,
    anos,
    prestacao))
if salario * 30 / 100 >= prestacao:
    print('{}Empréstimo aprovado!{}'.format(cor.verde, cor.reset))
else:
    print('{}Empréstimo recusado!{}'.format(cor.vermelho, cor.reset))
