def titulo(frase):
    print('-==-' * 10)
    print(f'{frase:^40}') 
    print('-==-' * 10)
    

titulo('Curso em Video')

def somar(a, b):
    print(a + b)


print('-==-' * 10)
somar(1, 1)
somar(a=1, b=2)
somar(b=2, a=3)

def contador(*numeros): # cria uma tupla
    print(len(numeros))


print('-==-' * 10)
contador(0, 1)
contador(0, 1, 1)
contador(0, 1, 1, 2)
contador(0, 1, 1, 2, 3)
contador(0, 1, 1, 2, 3, 5)

def dobrar(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2


print('-==-' * 10)
lista = [1, 2, 3, 5, 7]
dobrar(lista)
print(lista)

def somarPacote(*numeros):
    print(sum(numeros))
    

print('-==-' * 10)
somarPacote(1, 1, 2, 3, 5, 8, 13)
