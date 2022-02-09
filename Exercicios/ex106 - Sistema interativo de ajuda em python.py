# Desafio 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário 
# digitar a palavra 'FIM', o programa se encerrará. 
# Importante: use cores.
from rotinas import var, titulo, err

def ajuda(comando):
    titulo(err(f'Acessando manual do comando \'{comando}\''.upper()), 80, True)
    help(comando)


while True:
    titulo(var('Sistema de ajuda interativa'.upper()), 80)
    comando = input('Digite uma função ou biblioteca: ')
    if comando.upper().strip() == 'SAIR':
        break
    ajuda(comando)
