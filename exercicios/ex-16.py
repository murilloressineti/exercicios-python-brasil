'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

print('Digite a Largura e o Comprimento da área que você deseja pintar.')
l = int(input('Largura: '))
c = int(input('Comprimento: '))
a = l*c

litro = a/6 * 1.1


latas = int(litro/18)
if litro % 18 != 0:
    latas += 1
p = latas * 80
print(f'Para uma área de {a}m² você precisará de {latas} lata(s) de tinta (18L) e pagará R${p:.2f} ')

galoes = int(litro/3.6)
if litro % 3.6 != 0:
    galoes += 1
pg = galoes * 25
print(f'Para uma área de {a}m² você precisará de {galoes} galão(ões) de tinta (3,6L) e pagará R${pg:.2f} ')

mixlatas = int(litro/18)
mixgaloes = int((litro - mixlatas * 18) / 3.6)              # <- Tive dificuldade pra entender essa divisão
if ((litro - (mixlatas * 18) % 3.6 != 0 )):
    mixgaloes += 1
    preco_mix = (mixlatas * 80) + (mixgaloes * 25)

print(f'Se você deseja misturar latas e galões para econimizar, '
      f'para uma área de {a}m² você precisará de {mixlatas} lata(s) de tinta (18L) '
      f'e {mixgaloes} galão(ões) de tinta (3,6L) e pagará R${preco_mix:.2f}')
