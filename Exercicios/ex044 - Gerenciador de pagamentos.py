# Desafio 0044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e as condições de pagamento.
# À vista no dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
from cores import cor

#print('{:^=40}'.format(' Lojinha '))
preco = float(input('Digite o valor da compra: '))
print('''[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Digite a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    print(f'O valor de cada parcela será de R$ {total / 2:.2f} reais.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas vezes deseja parcelar: '))
    print('O valor de cada parcela em {1}{2}x{0} será de R$ {1}{3:.2f}{0} reais.'.format(
        cor.reset,
        cor.verde,
        parcelas,
        total / parcelas
    ))
else:
    total = 0
    print(f'{cor.vermelho}Opção inválida!{cor.reset}')
print(f'Sua compra custará R$ {cor.verde}{total:.2f}{cor.reset} reais no total.')
