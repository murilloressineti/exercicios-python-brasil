#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

n = str(input('Digite o seu nome: '))
s = float(input(f'{n}, informe qual é o seu salário: '))
d = 1
while d != 0:
    d = int(input('Informe quantos dias por semana você trabalha: '))
    if d > 7:
        print('ERRO! Digite um número válido.')
    if d <= 7:
        break
h = int(input('Informe quantas horas você trabalha por dia: '))

horas = ((d*4)*h)
salario = s/horas

res = print(f'Você trabalha {horas} horas no mês e recebe {salario:.2f} por hora.')
