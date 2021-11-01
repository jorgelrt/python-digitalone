nota1 = float(input('Informe a nota do 1º bimestre: '))
while nota1 > 10:
    nota1 = float(input('Erro. Favor informar corretamente a nota do 1º bimestre: '))
nota2 = float(input('Informe a nota do 2º bimestre: '))
while nota2 > 10:
    nota1 = float(input('Erro. Favor informar corretamente a nota do 2º bimestre: '))
nota3 = float(input('Informe a nota do 3º bimestre: '))
while nota3 > 10:
    nota3 = float(input('Erro. Favor informar corretamente a nota do 3º bimestre: '))
nota4 = float(input('Informe a nota do 4º bimestre: '))
while nota4 > 10:
    nota4 = float(input('Erro. Favor informar corretamente a nota do 4º bimestre: '))
if (nota1+nota2+nota3+nota4)/4 >= 7:
    print('Aluno aprovado com média {}'.format((nota1+nota2+nota3+nota4)/4))
else:
    print('Aluno em recuperação, média: {}'.format((nota1+nota2+nota3+nota4)/4))
