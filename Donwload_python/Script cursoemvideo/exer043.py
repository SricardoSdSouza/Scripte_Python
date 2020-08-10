'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:
-Abaixo de 18.8: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida.'''

'''print('\033[36m*****\033[m'*10)
print('\033[34mVamos calcular o seu "IMC" cuidando da saúde!!\033[m')
print('\033[36m*****\033[m'*10)
altura = float(input('Informe a sua altura : '))
peso= float(input('Informe o seu peso : '))
imc = peso/(altura**2)
if imc <= 18.5 :
    print('\033[31mEstá abaixo do peso, seu IMC foi: {:.2f}\033[m'.format(imc))
elif imc > 18.5 and imc <=25:
    print('Está com o peso, seu IMC foi: {:.2f} - \033[32mIDEAL\033[m'.format(imc))
elif imc > 25 and imc <= 30:
    print('Alerta seu IMC foi: {:.2f} - \033[33mSobrepeso\033[m'.format(imc))
elif imc > 30 and imc <= 40 :
    print('Atenção! seu iMC foi: {:.2f} - \033[33mObesidade\033[m '.format(imc))
else:
    print('\033[1;31;43mPERIGO! esta com OBESIDADE MÓRBIDA\033[m seu IMC foi: {:.2f}'.format(imc))'''
# Resolução do Guanabara
altura = float(input('Qual é sua altura (m): '))
peso= float(input('Qual é seu peso (kg): '))
imc = peso/(altura**2)
print('O IMC dessa pessoa pe de {:.1f}'.format(imc))
if imc <= 18.5 :
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40 :
    print('Você esta em OBESIDADE!')
else:
    print('Você esta em OBESIDADE MÓRBIDA, cuidado!')
