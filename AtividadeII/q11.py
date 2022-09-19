#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1 = int(input('\nDigite o número 1: '))
num2 = int(input('\nDigite o número 2: '))
num3 = float(input('\nDigite o número 3: '))

result1 = ((num1 * 2) * (num2/2))
result2 = ((num1 * 3) + num3)
result3 = (num3 * num3 * num3)

print('\nResultado 1 = ', result1)
print('Resultado 2 = ', result2)
print('Resultado 3 = ', result3)