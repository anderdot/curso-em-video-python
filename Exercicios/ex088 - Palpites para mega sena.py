# Desafio 088: Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 0 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# Desafio extra: Sortear 3 pares e 3 impares em cada palpite, fazer um top 10
# dos números mais e menos sorteados.
from cores import cor
from random import randint
from time import sleep

controle_pares = 3
controle_impares = 3
pares = impares = 0

top = 10
sorteados = []

palpite = []
palpites = []
jogos = int(input('Quantos jogos sortear: '))
while len(palpites) < jogos:
    while len(palpite) < 6:
        numero = randint(1, 60)
        if numero not in palpite:
            if numero % 2 == 0: 
                if pares < controle_pares:
                    palpite.append(numero)
                    pares += 1
                    inserir = True
            elif numero % 2 == 1:
                if impares < controle_impares:
                    palpite.append(numero)
                    impares += 1
                    inserir = True
                    
            if inserir:
                existe = False
                for p in sorteados:
                    if numero == p[0]:
                        p[1] += 1
                        existe = True
                        break
                if not existe:
                    sorteados.append([numero, 1])
    palpite.sort()
    palpites.append(palpite[:])
    # print(f'Pares: {pares} : ímpares: {impares}')
    pares = impares = 0
    palpite.clear()
print(f'{" Jogos Sorteados ":-^40}')
for i, p in enumerate(palpites):
    print(f'Jogo {i + 1:02}: {cor.verde}{p}{cor.reset}')
    # sleep(0.2)

sorteados = sorted(sorteados, key=lambda sorteado: sorteado[1])
print(f'{" Números MENOS Sorteados ":-^40}')
for i, s in enumerate(sorteados):
    print(f'{s[0]:2} saiu {cor.verde}{s[1]}{cor.reset} vez(es).')
    if i == top - 1:
        break
sorteados = sorted(sorteados, key=lambda sorteado: sorteado[1], reverse=True)
print(f'{" Números MAIS Sorteados ":-^40}')
for i, s in enumerate(sorteados):
    print(f'{s[0]:2} saiu {cor.verde}{s[1]}{cor.reset} vez(es).')
    if i == top - 1:
        break
