# Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ou serviço militar, 
# se é hora de se alistar ou se já passou o tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que ja passou.
from cores import cor
from datetime import date

atual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = atual - anoNascimento
print('Quem nasceu em {1}{2}{0} tem {1}{3}{0} anos em {1}{4}{0}.'.format(
    cor.reset,
    cor.verde,
    anoNascimento,
    idade,
    atual
))
if idade == 18:
    print(f'{cor.verde}Você esta na idade de se alistar!{cor.reset}') #usar mais isso
elif idade < 18:
    print('Faltam {}{}{} anos para o seu alistamento'.format(
        cor.verde,
        18 - idade,
        cor.reset
    ))
    print('Seu alistamento será em {}{}{}.'.format(
        cor.verde,
        atual + (18 - idade),
        cor.reset
    ))
else:
    print('Você ja deveria ter se alistado há {}{}{} anos.'.format(
        cor.verde,
        idade - 18,
        cor.reset
    ))
    print('Seu alistamento foi em {}{}{}.'.format(
        cor.verde,
        atual - (idade - 18),
        cor.reset
    ))
