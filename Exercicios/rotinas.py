# Funções que vão facilitar minha vida e deixar o código mais elegante
from cores import cor

# Colore em verde na hora de printar
def var(texto):
    return f'{cor.verde}{texto}{cor.reset}'


# Colore em vermelho na hora de printar
def err(texto):
    return f'{cor.vermelho}{texto}{cor.reset}'


# Printar os textos centralizados
def titulo(texto='', tamanho=40, pular=False):
    if pular:
        print()
    e = '' if texto == '' else ' '
    print(f'{e + texto + e:-^{tamanho}}')
