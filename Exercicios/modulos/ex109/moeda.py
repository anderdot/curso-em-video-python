from rotinas import var

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return moeda(res) if formato else res
    

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return moeda(res) if formato else res
    

def dobro(preco=0, formato=False):
    res = preco * 2
    return moeda(res) if formato else res


def metade(preco=0, formato=False):
    res = preco / 2
    return moeda(res) if formato else res

def moeda(preco=0, moeda='R$ '):
    preco = f'{preco:.2f}'.replace('.', ',')
    return f'{moeda}{var(preco)}'
