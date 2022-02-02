# Desafio 058: Melhore o jogo do Desafio 028 onde o computador vai "pensar" em
# um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from cores import cor
from random import randint
from time import sleep

pensado = randint(1, 10)
print('-=-' * 15)
print('{:^45}'.format('Você? mero mortal. Ousa me desafiar?'))
print('{:^45}'.format('HA HA HA HA'))
print('-=-' * 15)
sleep(1)

tentativas = 0
acertou = False
frase = True
while not acertou:
    print('Pode tentar.' if frase else 'Você errou.', end = ' ')
    frase = False
    numero = int(input('Digite um número: '))
    tentativas += 1
    if numero == pensado:
        acertou = True;
    print('-=-' * 15)
print('{:^45}'.format('Essa NÃÃÃÃÃO. Fui derrotado x.x'))
if tentativas == 1:
    print('{:^45}'.format('Em {1}uma{0} tentativa, o miseravel é um {1}gênio{0}.'.format(
        cor.reset,
        cor.verde,
    )))
else:
    print('{:^45}'.format(f'Pelo menos você fez {cor.verde}{tentativas}{cor.reset} tentativas. >:)'))
    