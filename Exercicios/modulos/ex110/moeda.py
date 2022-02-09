from rotinas import var, titulo

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
    preco = f'{preco:10.2f}'.replace('.', ',')
    return f' {moeda}{var(preco)}'

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    titulo('Resumo do valor', 50)
    print(f' {f"Valor analisado ":.<20}{moeda(preco):.>36}')
    print(f' {f"Metade ":.<20}{metade(preco, True):.>36}')
    print(f' {f"Dobro ":.<20}{dobro(preco, True):.>36}')
    print(f' {f"Taxa de {taxa_aumento}% ":.<20}{aumentar(preco, taxa_aumento, True):.>36}')
    print(f' {f"Desconto de {taxa_reducao}% ":.<20}{diminuir(preco, taxa_reducao, True):.>36}')
    titulo(tamanho=50)
    