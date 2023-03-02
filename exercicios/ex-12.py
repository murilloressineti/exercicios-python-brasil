#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

n = str(input('Olá! Insira o seu nome: '))
s = str(input(f'{n}, qual o seu sexo? Insira [M ou F]: ')).strip().upper()
a = float(input('Insira a sua altura: '))
p = float(input('Por último, insira o seu peso atual: '))
rm = ((72.7*a)-58)
rf = ((62.1*a)-44.7)
if s == 'M':
    print(f'{n}, analisando o seu peso atual {p}kg o seu peso ideal é {rm:.2f}kg.')
    if p > rm:
        print('Você precisa emagrecer um pouco mais!')
    else:
        print('Você precisa engordar um pouco mais!')
elif s == 'F':
    print(f'{n}, analisando o seu peso atual {p}kg, o seu peso ideal é {rf:.2f}kg.')
    if p > rf:
        print('Você precisa emagrecer um pouco mais!')
    else:
        print('Você precisa engordar um pouco mais!')
