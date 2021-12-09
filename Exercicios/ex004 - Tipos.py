# Desafio 004: Faça um exercício que leia algo pelo teclado e mostra na tela o 
# seu tipo primitivo e todas as informações possiveis sobre ela.  
from cores import cor

tipo = input('Digite algo: ')
print('Tipo: {}{}{}'.format(cor.verde, type(tipo), cor.reset)) 
print('É alpha numérico? {}{}{}'.format(cor.amarelo, tipo.isalnum(), cor.reset)) 
print('É Alpha?          {}{}{}'.format(cor.amarelo, tipo.isalpha(), cor.reset)) 
print('É ASCII?          {}{}{}'.format(cor.amarelo, tipo.isascii(), cor.reset)) 
print('É Decimal?        {}{}{}'.format(cor.amarelo, tipo.isdecimal(), cor.reset)) 
print('É Digito?         {}{}{}'.format(cor.amarelo, tipo.isdigit(), cor.reset)) 
print('É Identificador?  {}{}{}'.format(cor.amarelo, tipo.isidentifier(), cor.reset)) 
print('É Minúsculo?      {}{}{}'.format(cor.amarelo, tipo.islower(), cor.reset)) 
print('É Maiúsculo?      {}{}{}'.format(cor.amarelo, tipo.isupper(), cor.reset)) 
print('É Espaço?         {}{}{}'.format(cor.amarelo, tipo.isspace(), cor.reset)) 
print('É Printavel?      {}{}{}'.format(cor.amarelo, tipo.isprintable(), cor.reset)) 
print('É Titulo?         {}{}{}'.format(cor.amarelo, tipo.istitle(), cor.reset)) 
print('É Número?         {}{}{}'.format(cor.amarelo, tipo.isalnum(), cor.reset)) 
