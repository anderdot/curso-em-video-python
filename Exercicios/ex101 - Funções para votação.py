# Desafio 101: Crie um programa que tenha uma função chamada voto() que vai 
# receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas 
# eleições.
from rotinas import var, titulo

def voto(nascimento):
    from datetime import date
    
    atual = date.today().year
    idade = atual - nascimento
    titulo('Resultado', 35)
    if idade < 16:
        return f'Com {var(idade)} anos {var("não")} vota.'
    elif idade < 18 or idade > 65:
        return f'Com {var(idade)} anos o voto é {var("opcional")}.'
    else:
        return f'Com {var(idade)} anos o voto é {var("obrigatório")}.'


nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))
