#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

farenheit = float(input('\nDigite a temperatura em Farenheit: '))
celsius = ((farenheit - 32)/9) * 5

print(farenheit, 'farenheits =' , celsius , 'celsius')