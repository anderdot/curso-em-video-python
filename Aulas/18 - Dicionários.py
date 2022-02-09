pessoas = {
    'nome': 'Anderson',
    'sexo': 'M',
    'idade': 23
}

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(pessoas)
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('*' * 15)

for k in pessoas.keys():
    print(k)

for p in pessoas.values():
    print(p)
    
for k, p in pessoas.items():
    print(f'{k} = {p}')
print('*' * 15)

pessoas["nome"] = 'Bruna'
pessoas["idade"] = 22
pessoas["sexo"] = 'F'

for k, p in pessoas.items():
    print(f'{k} = {p}')
print('*' * 15)

estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])
print('*' * 15)

estado = {}
brazil = []
for i in range(0, 2):
    estado['uf'] = input('Digite o nome do estado: ')
    estado['sigla'] = input('Digite a sigla: ')
    brazil.append(estado.copy())
print(brazil)

for e in brazil:
    for v in e.values():
        print(v, end=' ')
    print()
    