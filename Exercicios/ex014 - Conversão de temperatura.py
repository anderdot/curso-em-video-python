# Desafio 014: Informado uma temperatura em ºC converta em ºF
from cores import cor

temperatura = float(input('Digite a temperatura em ºC: '))
print('A temperatura é {}{}{}ºF.'.format(cor.verde, 9 * temperatura / 5 + 32, cor.reset))
