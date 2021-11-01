#Aprofundar nas sintaxes
#Aprender a utilizar condicionais
#Aprender a utilizar operadores lógicos

a = int(input("Informe o 1º valor: "))
b = int(input("Informe o 2º valor: "))
c = int(input('Informe o 3º valor: '))

if a > b and a > c:
    print('O maior número é: {}'.format(a))
elif b > a and b > c:
    print('O maior número é: {}'.format(b))
else:
    print('O maior número é: {}'.format(c))
print('Final do programa')
