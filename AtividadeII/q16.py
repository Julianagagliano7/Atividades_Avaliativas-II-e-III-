#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = int(input('\nDigite o tamanho da área a ser pintada (m²): '))

amount_liters = (area/3.0)
total_price_liters = (amount_liters * 4.44444)
n_cans = (total_price_liters / 18)

print('\nQuantidade de latas = ', n_cans)
print('\nPreço Total = ' , total_price_liters)

