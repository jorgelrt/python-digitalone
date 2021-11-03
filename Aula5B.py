#Tupla é imutável
tupla = (1,10,12,8)
print(tupla)

print('Valor da posição 2: {}'.format(tupla[2]))

#qtos registros exitem na tupla
print('Temos {} elementos na tupla'.format(len(tupla)))

#Converter lista p/ tupla(imutável)

lista_animal = ['viado','zebra','arara','galinha','pato']
tupla_animal = tuple(lista_animal)
print(tupla_animal)
#é imutável - tentativa de alterar algum valor da tupla
#tupla_animal[0] = 'foca' - DA ERRO!!!

#verificando o tipo
print('Verificando o tipo do objeto tupla_animal = {}'.format(type(tupla_animal)))

#convertendo a tupla em lista
lista_numerica = list(tupla)
print('Listando a conversão da tupla em lista: {}'.format(tupla))
#agora conseguimos alterar
lista_numerica[0] = 21
print('lista alterada derivada de tupla: {}'.format(lista_numerica))

