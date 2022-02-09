lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche[2])
lanche[3] = 'Picolé'
lanche.append('Bolacha')
lanche.insert(0, 'Cachorro-Quente')
print(lanche)
# del lanche(3)
lanche.pop(3) # parametro. senão o último
if 'Pizza' in lanche:
    lanche.remove('Pizza')
else:
    print('Não tem pizza')
lanche.sort()
print(lanche)
lanche.sort(reverse = True)
print(lanche)
print(len(lanche))

for cont in range(0,2):
    lanche.append(input('Digite um novo lanche: '))
for c, v in enumerate(lanche):
    print(f'Na posição {c} tem o valor {v}!')
    
print('*' * 50)
a = [1, 2, 3, 4]
b = a # linka uma lista na outra
b = a[:] # cria uma cópia da lista
b[2] = 5
print(a)
print(b)
