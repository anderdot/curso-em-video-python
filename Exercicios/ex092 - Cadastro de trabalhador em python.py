# Desafio 092: Crie um programa que leia nome, ano de nascimento e carteira 
# de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS 
# for diferente de ZERO, o dicionário receberá também o ano de contratação e 
# o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa 
# vai se aposentar.
from cores import cor
from datetime import datetime

dados = {}
dados['nome'] = input('Digite seu nome: ')
nascimento = int(input('Digite seu ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = input('Digite sua carteira de trabalho (0 - Não tenho): ')
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite seu salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print(f'{" Dados ":-^40}')
for k, v in dados.items():
    print(f' - {cor.verde}{k}{cor.reset} tem o valor de {cor.verde}{v}{cor.reset}.')
