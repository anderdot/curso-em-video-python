# Desafio 105: Faça um programa que tenha uma função notas() que pode receber 
# várias notas de alunos e vai retornar um dicionário com as seguintes 
# informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
from rotinas import var, titulo

def notas(*n, situacao=False):
    """Função para analisar as notas e situações do aluno.

    Args:
        *n (Float): Todas as notas do aluno.
        situacao (bool, optional): Se deve ou não mostrar a situação do aluno. Defaults to False.
    Returns:
        dicionário: Notas e situação do aluno
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoável'
        else:
            r['situacao'] = 'Ruim'
    return r
    

titulo(var('Notas'), 90)
print(notas(10, 9.5, 8, situacao=True))
print(notas(5, 9, 4, situacao=True))
print(notas(6, 5, 2, situacao=True))
print(notas(8, 7, 8, 7, 6, 10, 9))
