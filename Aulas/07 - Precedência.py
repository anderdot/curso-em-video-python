# 1º ()
# 2º **
# 3º * /  // %
# 4º + -
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:-^20}!'.format(nome))
print('-=' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('A soma é {}'.format(n1 + n2))
print('A subtração é {}'.format(n1 - n2))
print('A multiplicação é {}'.format(n1 * n2))
print('A divisão é {:.3f}'.format(n1 / n2))
print('A exponenciação é {}'.format(n1 ** n2))
print('A divisão inteira é {}'.format(n1 // n2), end=' ')
print('com resto da divisão {}'.format(n1 % n2))
