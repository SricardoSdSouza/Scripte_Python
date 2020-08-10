'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".'''
# Solução do Guanabara
cidade = str(input('Digite em qual cidade você nasceu: ')).strip()
print(cidade[0:5].upper()=='SANTO')