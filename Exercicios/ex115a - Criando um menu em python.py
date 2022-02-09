# Desafio 115a: Crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as
# pessoas cadastradas.
from modulos.ex115.interface import gerarMenu, destaque, leiaInt, entradaDados
from modulos.ex115.arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrar

nome_arquivo = 'Exercicios\modulos\ex115\Lista de pessoas.txt'
if not arquivoExiste(nome_arquivo):
    criarArquivo(nome_arquivo)

while True:
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa']
    opcao = gerarMenu(opcoes)
    if opcao == 0:
        print('Até mais.')
        break
    destaque(opcoes[opcao - 1])
    if opcao == 1:
        lerArquivo(nome_arquivo)
    if opcao == 2:
        nome = entradaDados('Digite um nome: ')
        idade = leiaInt('Digite uma idade: ')
        cadastrar(nome_arquivo, nome, idade)
