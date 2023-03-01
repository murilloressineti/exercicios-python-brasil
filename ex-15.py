'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

print('Digite a Largura e o Comprimento da área que você deseja pintar.')
l = int(input('Largura: '))
c = int(input('Comprimento: '))
a = l*c

litro = a/3
latas = int(litro/18)
if litro % 18 != 0:
    latas += 1
p = latas * 80

print(f'Para uma área de {a}m² você precisará de {latas} lata(s) de tinta (18L) e pagará R${p:.2f} ')
