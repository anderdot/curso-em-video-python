n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 6:
    print('Passou!')
else:
    print('Se ferrou!')
print('Nota: {:.1f}.'.format(media))
