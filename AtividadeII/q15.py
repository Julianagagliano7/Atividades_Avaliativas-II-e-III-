#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

hourly_earnings = float(input('\nDigite quanto você ganha por hora (reais): '))
hours = float(input('\nDigite o número de horas que você trabalhou este mês: '))

gross_salary = (hourly_earnings * hours)
income_tax = (gross_salary * 0.11)
inss_value = (gross_salary * 0.08)
syndicate_value =(gross_salary * 0.05)
net_salary = (gross_salary) - (income_tax + inss_value + syndicate_value)

print('\nSalário Bruto =' , gross_salary , 'reais')
print('Valor pago de IR = ', income_tax , 'reais')
print('Valor pago ao INSS = ' , inss_value ,'reais')
print('Valor pago ao Sindicato = ', syndicate_value , 'reais')
print('Salário Líquido = ', net_salary , 'reais')
