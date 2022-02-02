# Desafio 040: Crie um programa que leia duas notas de um aluno e calcule a média,
# mostrando no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média acima de 7.0: Aprovadofico 
from cores import cor

n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
media = (n1 + n2) / 2
print(f'Com a média de {media:.1f} você', end=' ')
if media < 5:
    print(f'foi {cor.vermelho}reprovado{cor.reset}.')
elif 7 > media >= 5: # media >= 5 and media < 7:
    print(f'ficou de {cor.anil}recuperação{cor.reset}.')
else:
    print(f'foi {cor.verde}aprovado{cor.reset}.')
