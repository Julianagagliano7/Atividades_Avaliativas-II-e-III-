#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hourly_earnings = float(input('\nDigite quanto você ganha por hora (reais): '))
hours = float(input('\nDigite o número de horas que você trabalhou este mês: '))

salary = (hourly_earnings * hours)
print('\nSalário total = ' , salary , 'reais')
