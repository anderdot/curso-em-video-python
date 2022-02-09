from rotinas import var

def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return res
    

def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return res
    

def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res

def moeda(preco=0, moeda='R$ '):
    preco = f'{preco:.2f}'.replace('.', ',')
    return f'{moeda}{var(preco)}'
