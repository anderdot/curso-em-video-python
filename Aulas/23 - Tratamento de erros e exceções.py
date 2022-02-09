try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except Exception as ex:
    print(f'Tivemos um problema: {ex}.')
else:
    print(f'O resultado é {r:.2f}.')
finally:
    print('Vou executar idependente')
