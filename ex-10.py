#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input('Celsius: '))
f = (c * 9/5 + 32)
print(f'Fahrenheit: {f:.2f}')