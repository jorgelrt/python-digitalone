#Aprofundar nas sintaxes básicas
#Aprender variáveis em Python
#Realizar interações com usuário

a = 10
b = 6

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

#Para saber qual tipo é uma variável utilize type().
print('type(soma) = ' + str(type(soma)))

#Converte int para string str()
print('Soma: ' + str(soma))

print(subtracao)

print(multiplicacao)

#Qual o tipo da variavel "divisao"
print('type(divisao) = ' + str(type(divisao)))
print(divisao)

#Imprimindo float como integer
print('Imprimindo float como integer: ' + str(int(divisao)))

print(resto)

#Convertendo de string para integer
x = '1'
soma2 = int(x) + 1
print('Soma2: ' + str(soma2))

print('Para comentar + de uma linha, pressione CRTL + /')