# Desafio 110: Adicione o módulo moeda.py criado nos desafios anteriores, 
# uma função chamada resumo(), que mostre na tela algumas informações geradas 
# pelas funções que já temos no módulo criado até aqui.
from modulos.ex110.moeda import resumo

valor = float(input('Digite um valor: R$ '))
resumo(valor, 85, 15)
