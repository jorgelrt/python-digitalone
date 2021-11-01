nota1 = float(input('Informe a nota do 1º bimestre: '))
if nota1 > 10: #validação de entrada - boa prática
    nota1 = float(input('Erro. Favor informar corretamente a nota do 1º bimestre: '))
nota2 = float(input('Informe a nota do 2º bimestre: '))
if nota2 > 10: #validação de entrada - boa prática
    nota1 = float(input('Erro. Favor informar corretamente a nota do 2º bimestre: '))
nota3 = float(input('Informe a nota do 3º bimestre: '))
if nota3 > 10: #validação de entrada - boa prática
    nota3 = float(input('Erro. Favor informar corretamente a nota do 3º bimestre: '))
nota4 = float(input('Informe a nota do 4º bimestre: '))
if nota4 > 10: #validação de entrada - boa prática
    nota4 = float(input('Erro. Favor informar corretamente a nota do 4º bimestre: '))
if (nota1+nota2+nota3+nota4)/4 >= 7:
    print('Aluno aprovado com média {}'.format((nota1+nota2+nota3+nota4)/4))
else:
    print('Aluno em recuperação, média: {}'.format((nota1+nota2+nota3+nota4)/4))
