# if / elif      / else
# se / se não se / se não
# Tab representa 4 espaços essa hierarquia representa 
# que este trecho de codigo está dentro de if o trecho 
# "print('você entrou no sistema)'''

# if / elif      / else
# se / se não se / se não

condicao1 = True # ele vai chegar sempre a primeira condição que estiver true
condicao2 = True # se todas estiverem falsew ele vai pro else
condicao3 = True # else é sempre a ultima condicação a ser executada
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')