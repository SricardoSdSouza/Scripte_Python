'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        #Adiciona o parêntese '(' na pilha
        pilha.append('(')
    elif simb == ')':
        #testa o tamanho da pilha se tiver um '(' registrado ele remove
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
#Testa se a pilha ta vazia é porque os parênteses foram pares e a expressão esta correta
if len(pilha)  == 0:
    print('Sua expressão está válida!.')
else:
    print('Sua expressão não é válida')
print('-=-'*20)