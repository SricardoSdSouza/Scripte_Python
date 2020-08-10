'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele'''

algo=input("Digite alguma coisa que desejar :")
print("o que foi digitado é do tipo primitivo =",type(algo))
print('O que foi digitado é número? ',algo.isnumeric())
print('o que foi digitado é alfa numérico?',algo.isalnum())
print('o que foi digitado é alfabétido?',algo.isalpha())
print('o que foi digitado é ou são digitos?',algo.isdigit())
print('o que foi digitado esta em maiúscula ?',algo.isupper())
print('o que foi digitado esta em minúscula ?',algo.islower())
print('o que foi digitado esta em decimal ?',algo.isdecimal())
print('o que foi digitado foi espaço ?',algo.isspace())
print('o que foi digitado pode ser impresso ?',algo.isprintable())
#capitalizado é quando existe uma letra maiúscula e o restante minuscula ou vice versa
print('o que foi digitado esta capitalizado ?',algo.istitle())