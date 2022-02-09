from rotinas import var, err
from modulos.ex115.interface import mostrarPessoas

def arquivoExiste(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+', encoding='utf8')
        arquivo.close()
    except Exception as ex:
        print(err(f'Houve um erro na criação do arquivo. {ex}'))
    else:
        print(f'Arquivo {var(nome_arquivo)} criado com sucesso!')
        
        
def lerArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt', encoding='utf8')
    except:
        print(err('Erro ao ler o arquivo.'))
    else:
        # print(arquivo.read())
        mostrarPessoas(arquivo)
    finally:
        arquivo.close


def cadastrar(nome_arquivo, nome='<desconhecido>', idade=0):
    try:
        arquivo = open(nome_arquivo, 'at', encoding='utf8')
    except:
        print(err('Houve um erro na abertura do arquivo.'))
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print(err('Houve um erro na hora de escrever os dados.'))
        else:
            print('Novo registro adicionado com sucesso!')
    finally:
        arquivo.close()
        