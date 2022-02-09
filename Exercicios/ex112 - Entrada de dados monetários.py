# Desafio 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, 
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que 
# seja capaz de funcionar como a função imputa(), mas com uma validação de 
# dados para aceitar apenas valores que seja monetários.
from modulos.ex112.moeda import resumo
from modulos.ex112.dado import leiaDinheiro

valor = leiaDinheiro('Digite um valor: R$ ')
resumo(valor, 85, 15)
