# Desafio 029: Digite a velocidade de um veiculo e ele mostra se recebeu uma multa
# limite é 80km e paga 7 reais por quilometro acima do limite.
from cores import cor

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Multado em R$ {}{:.2f}{} reais.'.format(
        cor.verde, 
        (velocidade - 80) * 7, 
        cor.reset))
print('Tenha um ótimo dia!')
