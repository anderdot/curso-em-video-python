# Desafio 011: Faça um programa que leia a largura e a altura de uma parede e calcula a sua 
# area e quantidade necessária de tinta para pinta-la, sabendo que 1 litro de 
# tinta pinta 2m²
from cores import cor

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('A area da parede é de {}{}{} m².'.format(cor.verde, area, cor.reset))
print('Será necessário {}{}{} litros de tinta.'.format(cor.verde, area / 2, cor.reset))
