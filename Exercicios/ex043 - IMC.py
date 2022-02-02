# Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# o IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso 
# 30 a 40: Obesidade
# Acima de 40: Obesidade Mórbida
from cores import cor

peso = float(input('Digite seu peso (em quilos): '))
altura = float(input('Digite sua altura (em metros): '))
imc = peso / altura ** 2
print(f'Seu IMC é {cor.verde}{imc:.1f}{cor.reset}, você', end=' ')
if imc < 18.5:
    print(f'esta {cor.verde}abaixo do peso{cor.reset}.')
elif 18.5 <= imc < 25:
    print(f'tem o {cor.verde}peso ideal{cor.reset}.')
elif 25 <= imc < 30:
    print(f'esta em {cor.verde}sobrepeso{cor.reset}.')
elif 30 <= imc < 40:
    print(f'esta em {cor.verde}obesidade{cor.reset}.')
else:
    print(f'esta em {cor.verde}obesidade mórbida{cor.reset}.')
