#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

counter = 4
sum = 0

for i in range(1 , counter + 1):
    number = float(input('\nDigite um número (maior do que 0 e menor do que 10): '))
    sum+=number
    average=sum/i

print('\nMédia = ', average)
