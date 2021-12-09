import math
# python -m pip install emoji
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.3f}'.format(num, raiz))
print(emoji.emojize('Olá mundo :earth_americas:', use_aliases=True))
