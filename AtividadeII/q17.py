#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = int(input('Digite o valor da área(m²): '))

#1º Situação - Comprar somente latas de 18L
print('\nPRIMEIRA SITUAÇÃO\n')

n_liters = (area/6.0)
total_price_liters = (n_liters * 80.0/18.0)
n_cans = (total_price_liters / 80.0)

print('\nVocê precisará de: ',n_cans , 'latas de tinta') #arredondamento para cima
print('\nPreço total = ', total_price_liters , 'reais')  #arredondamento para cima

print('\n')

#2º Situação - Comprar Galões de 3.6L
print('\nSEGUNDA SITUAÇÃO\n')

n_liters2 = (area/6.0)
total_price_liters2 = (n_liters2 * 25/3.60)
n_gallons = (total_price_liters2 / 25.0)

print('\nVocê precisará de: ',n_gallons , 'galões') #arredondamento para cima
print('\nPreço total = ', total_price_liters2 , 'reais')  #arredondamento para cima

#3º Situação - Latas e Galões - Menor desperdício + 10% de folga
print('\nTERCEIRA SITUAÇÃO\n')

n_cans2 = (area/108.0)
total_price_cans = (n_cans2 * 80.0)
n_gallons2 = (area/21.6)
total_price_gallons = (n_gallons2 * 25.0)

print('\nVocê precisará de ', n_cans2 , 'latas de 18L e pagará: ' , total_price_cans , 'reais')

print('\nVocê precisará de ', n_gallons2 , 'latas de 18L e pagará: ' , total_price_gallons, 'reais')

