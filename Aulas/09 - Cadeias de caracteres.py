frase = 'Curso em Vídeo Python'
print(frase[:5])
print(frase[9:])
print(frase[15:21])
print(frase[::2])
print(frase.count('o'))
print(frase.upper())
print(frase.lower())
print(frase.find('Vídeo'))
print(len(frase))
#print(frase.strip) # remove espaços frente e tras - r e l
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
print(frase)

print('''
Lorem Ipsum is simply dummy text of the printing and 
typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown 
printer took a galley of type and scrambled it to make a 
type specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages, and more recently with desktop 
publishing software like Aldus PageMaker including versions of Lorem Ipsum''')
