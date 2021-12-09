# Desafio 020: Sortear a ordem de apresentação de quatro alunos.
from cores import cor
from random import shuffle

nomes = []
for i in range(1, 5):
    nomes.append(input('{}º aluno: '.format(i)))
    
shuffle(nomes)
for i in range(1, 5):
    print('{}{}{}{}'.format(
        cor.verde,
        nomes.pop(),
        cor.reset,
        '.' if i == 4 else ', '), end='')
