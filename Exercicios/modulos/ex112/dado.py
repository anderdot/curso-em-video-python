from rotinas import err

def leiaDinheiro(mensagem):
    while True:
        numero = input(mensagem).replace(',', '.').strip()
        if numero.isalpha() or numero == '':
            print(err(f'\'{numero}\' não é uma entrada válida!'))
        else:
            break
    return float(numero)
