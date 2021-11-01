#Números primos até 100
valores = ''
for num in range(1,101):
    div = 0
    for x in range(1, num+1):
        resto = num%x
        if resto == 0:
            div += 1
    if div == 2:
        valores = str(valores) + str(num) + str(' | ')
print('Primos até 100: {}'.format(valores))