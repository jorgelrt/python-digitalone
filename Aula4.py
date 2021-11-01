#Aprofundar nas sintaxes básicas
#Aprender a utilizar laços de repetição
#Criar programas com condicional e laços de repetição

#FOR com RANGE - imprimir os 100 primeiros números

for x in range(100): #obtém de zero à 99
    print(x)

#Verificando se o número é primo
div = 0
a = int(input('Informe o número: '))
for x in range(1, a+1):
    resto = a%x
    if resto == 0:
        div += 1
if div==2:
    print('O número {} é primo'.format(a))
else:
    print('O numero {} não é primo'.format(a))





