#Interação com o usuário
a = int(input('Entre com o 1º valor: '))
b = int(input('Entre com o 2º valor: '))

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

#Saída padrão - Não importa o tipo, .format realiza a concatenacao na string. Qdo não informado alias entre chaves, atentar p/ ordem
print('Soma: {}, Subtracao: {}'.format(soma, subtracao))

#Para colocar na ordem, informamos um alias dentro da chave
print('Soma: {soma}, Subtracao: {sub}'.format(sub = subtracao, soma = soma))

#Em linhas separadas sem usa um outro print com \n
print('Soma: {soma}\n'
      'Subtração: {sub}\n'
      'Divisão: {div}\n'
      'Multiplicação: {mult}\n'
      'Resto: {resto}'.format(soma = soma, sub = subtracao, div = divisao, mult = multiplicacao, resto = resto))

#Colocando toda a saída numa string
saidaTexto = ('Soma: {soma}\n'
      'Subtração: {sub}\n'
      'Divisão: {div}\n'
      'Multiplicação: {mult}\n'
      'Resto: {resto}'.format(soma = soma, sub = subtracao, div = divisao, mult = multiplicacao, resto = resto))

print(saidaTexto)







