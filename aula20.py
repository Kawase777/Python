# Solicita os valores ao usuário
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

# Faz a comparação
if segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior que {primeiro_valor=}")
elif segundo_valor < primeiro_valor:
    print(f"{primeiro_valor=} é maior que {segundo_valor=}")
else:
    print(f"{primeiro_valor=} e {segundo_valor=} são iguais")
