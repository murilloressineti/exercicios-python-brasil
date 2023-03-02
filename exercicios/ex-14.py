#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

n = str(input('Olá, insira o seu nome: '))
s = float(input(f'{n}, insira quanto você ganha por hora: '))
h = int(input('Insira quantas horas você trabalha por dia: '))
d = 1
while d != 0:
    d = int(input('Informe quantos dias por semana você trabalha: '))
    if d > 7:
        print('ERRO! Digite um número válido.')
    if d <= 7:
        break
print(f'{n}, o seu salário no mês é:')
sb = ((s*h)*d*4)
ir = sb*11/100
inss = sb*8/100
sin = sb*5/100
sl = sb-ir-inss-sin
print(f'+ Salário Bruto: R${sb:.2f}')
print(f'- IR (11%): R${ir:.2f}')
print(f'- INSS (8%): R${inss:.2f}')
print(f'- Sindicato (5%): R${sin:.2f}')
print(f'= Salário Líquido: R${sl:.2f}')
