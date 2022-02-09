galera = [
    ['joão', 19],
    ['Ana', 33],
    ['Joaquim', 13],
    ['Maria', 45]
]
print(galera)
print(galera[0])
print(galera[0][0])

print('*' * 30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')
print('*' * 30)

pessoas = []
pessoa = []
for i in range(0, 3):
    pessoa.append(input('Digite seu nome: '))
    pessoa.append(int(input('Digite sua idade: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
print(pessoas)

maior = menor = 0
for p in pessoas:
    if p[1] > 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} são de maior e {menor} são de menor.')

