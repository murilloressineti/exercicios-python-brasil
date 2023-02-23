#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Digite a nota do 1º bimestre: '))
n2 = float(input('Digite a nota do 2º bimestre: '))
n3 = float(input('Digite a nota do 3º bimestre: '))
n4 = float(input('Digite a nota do 4º bimestre: '))

media = ((n1+n2+n3+n4)/4)

print(f'A média do aluno no ano foi: \033[1;34m{media}\033[m')
if media < 7:
    print('\033[1;31mREPROVADO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
