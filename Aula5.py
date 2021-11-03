#Aprender sobre listas
#Aprender sobre tuplas
#Aplicabilidade de lista e tuplas

lista = [1, 3, 5, 7]
lista_animal = ['cachorro','gato','elefante']
print('Tipo: {}'.format(type(lista)))
print('Valores contidos na lista: {}'.format(lista))

print('Valor da posição[1]: {l}'.format(l = lista_animal[1]))

for x in lista: #x herda o valor contido na lista
    print('Valores contidos na lista {}: '.format(lista))


cont = 0
while cont < len(lista):
    print('Valor da posição[{}] = {}'.format(cont,lista[cont]))
    cont += 1


#1ª forma de realizar um somatório
soma = 0
for x in lista:
    soma += x
print('Somatório é: {}'.format(soma))

#2ª forma de realizar um somatório
print('Somatório: {}'.format(sum(lista)))

#utilizando os métodos
print('Maior valor da lista {}'.format(max(lista)))
print('Menor valor da lista {}'.format(min(lista)))
#vale p string tbm
print('Maior valor(string) da lista {}'.format(max(lista_animal)))
print('Menor valor(String) da lista {}'.format(min(lista_animal)))

#Verificando se há um valor na lista
valorList = 'gato'
if valorList in lista_animal:
    print('verdadeiro, há o valor {} na lista'.format(valorList))
else:
    print('falso, não há o valor {}} na lista'.format(valorList))

#multiplicando os valores existentes da lista
nova_lista = lista * 3
nova_lista_animal = lista_animal * 3
for x in nova_lista:
    print(nova_lista)

for x in nova_lista_animal:
    print(nova_lista_animal)

#incluindo valores na lista
lista_animal.append('lobo')
for x in lista:
    print(lista)

for x in lista_animal:
    print(lista_animal)
lista.append(21)

#retirar a última posição da lista
lista.pop()
for x in lista:
    print(lista)

lista_animal.pop()
for x in lista_animal:
    print(lista_animal)

#remover um elemento da lista especifico por índice
lista.pop(0)
for x in lista:
    print(lista)
#remover um elemento que sabe o nome ou valor
lista_animal.remove('gato')
for x in lista_animal:
    print(lista_animal)






