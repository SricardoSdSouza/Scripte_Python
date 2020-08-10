'''Desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Informe o Primeiro Termo : '))
razao =int(input('Informe a Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro,decimo + razao,razao):
    print('{}'.format(c),end=' ->')
print('Acabou')