from rotinas import var, err, titulo

def mostrarPessoas(pessoas):
    for linha in pessoas:
        pessoa = linha.split(';')
        pessoa[1] = pessoa[1].replace('\n', '')
        print(f'| {pessoa[0] + " ":.<38}{" " + pessoa[1]:.>3} anos |')
    

def destaque(frase, tamanho=50):
    titulo(tamanho=50, pular=True)
    print(f'|{var(frase.upper()):^{tamanho + 6}}{"|":>}')
    titulo(tamanho=50)


def resultado(frase):
    titulo(tamanho=50, pular=True)
    print(frase)
    titulo(tamanho=50)


def gerarMenu(opcoes):
    destaque('Menu de opções', 50)
    for i, v in enumerate(opcoes):
        print(f' [{var(i + 1)}] {v}')
    print(f' [{var("0")}] Sair')
    return verificarMenu(len(opcoes))


def verificarMenu(tamanho):
    while True:
        opcao = leiaInt('Digite uma das opções.')
        if 0 <= opcao <= tamanho:
            return opcao
        else:
            resultado(err('Erro: Digite um número dentro do intervalo.'))


def leiaInt(frase):
    while True:
        try:
            inteiro = int(entradaDados(frase))
        except (ValueError, TypeError):
            resultado(err('Erro: Digite um número inteiro.'))
        else:
            return inteiro
    
def entradaDados(frase):
    print()
    print(frase)
    digitado = input('> ')
    return digitado
