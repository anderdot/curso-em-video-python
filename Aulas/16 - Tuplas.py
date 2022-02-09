# TUPLAS SÃO IMUTÁVEIS

# () TUPLA - não obrigatório
# [] LISTA
# {} DICIONARIO

lanche = (
    'hambúrguer', 
    'Suco', 
    'Pizza', 
    'Pudim',
    'Batata Frita'
)

print(lanche[2])        # mostrar só o elemento
print(lanche[0:2])      # do 0 até o 2, desconsiderando o último
print(lanche[:2])       # do inicio até o 2
print(lanche[1:])       # do 1 em diante
print(lanche[-1])       # último elemento
print(len(lanche))      # mostrar quantos elementos dentro da tupla

for c in lanche:        # Printar elemento por elemento
    print(c)

for c in range(0, len(lanche)):   # Printar elemento por indice
    print(c)

print(sorted(lanche))

a = (1, 2, 6)
b = (4, 5, 6, 7)

c = b + a
print(c)
print(c.count(8))
print(c.index(6))
print(c.index(6, 3))

pessoa = ('Anderson', 23)
del(pessoa)

