# Desafio 031: Dado uma distancia da viagem, calcule o valor, 0.50$ pra cada 
# quilometro até 200km e 0.45 para viagens acima de 200km.
from cores import cor

d = float(input('Digite a distância da viagem: '))
print('O custo será de R$ {}{:.2f}{} reais.'.format(
    cor.verde, 
    d * 0.50 if d <= 200 else d * 0.45, 
    cor.reset))
