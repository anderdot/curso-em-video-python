nome = input('Digite seu nome: ').strip().title()
if nome == 'Anderson':
    print('Que nome brabo!')
elif nome in 'José Maria':
    print('Já tomou a terceira dose?')
elif nome in 'Enzo Valentina':
    print('Puts ´m´')
else:
    print('Nada de interessante no seu nome.')
print('Tenha um bom dia, {}!'.format(nome))
