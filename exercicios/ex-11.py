#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))
n3 = float(input('Digite um número real:  '))

print(f'O dobro do primeiro com a metade do segundo = {(n1*2)+(n2/2)}')
print(f'A soma do triplo do primeiro com o terceiro = {(n1*3)+n3}')
print(f'O terceiro elevado ao cubo = {n3**3}')
