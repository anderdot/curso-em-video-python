# Desafio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos 
# internos chamados moeda e dado. Transfira todas as funções utilizadas nos 
# desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
# ja meio que tinha feito
from modulos.ex111.moeda import resumo

valor = float(input('Digite um valor: R$ '))
resumo(valor, 85, 15)
