# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = input('Deseja continuar? [S/N]: ').upper();
# print('Fim')

n = 1
par = impar = 0
while n != 0: # usar o do while
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
