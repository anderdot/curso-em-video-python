# Desafio 114: Crie um código em Python que teste se o site pudim está acessível 
# pelo computador usado.
import urllib
import urllib.request
from rotinas import var, titulo, err

try:
    titulo('Testando conexão')
    url = 'http://www.pudim.com.br'
    print(f'Tentando acessar... {var(url)} ...')
    site = urllib.request.urlopen(url)
except:
    print(err('O site não esta acessível.'))
else:
    print(var('O site esta no ar.'))
    # print(site.read())
