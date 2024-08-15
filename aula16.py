#Usando a Função input para coletar dados
#input('Qual o seu nome? ') 

'''colocar espaço 
no final para texto n ficar colado
Isso só funciona no terminal.'''

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome=}')

'''Aqui eu vou receber o valor nome = usando a 
a função input para o nome que eu digitar
ir para o valor nome.

A função print usando a F string para coletar
os dados armazenados da função input'''


numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
