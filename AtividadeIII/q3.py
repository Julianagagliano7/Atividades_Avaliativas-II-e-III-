# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%) : R$ 55,00
# (-) INSS ( 10%) : R$ 110,00
# FGTS (11%) : R$ 121,00
# Total de descontos : R$ 165,00
# Salário Liquido : R$ 935,00

income_tax = inss_value = syndicate_value = 0

hourly_earnings = float(input('\nDigite quanto você ganha por hora (reais): '))
hours = float(input('\nDigite o número de horas que você trabalhou este mês: '))

gross_salary = (hourly_earnings * hours)

if gross_salary <= 900:
    print('Isento do desconto IR')
    income_tax = 0
elif gross_salary <= 1500:
    income_tax = (gross_salary * 0.05)
elif gross_salary <= 2500:
    income_tax = (gross_salary * 0.1)
else:
    income_tax = (gross_salary * 0.2)

inss_value = (gross_salary * 0.1)
syndicate_value = (gross_salary * 0.03)
fgts_value = (gross_salary * 0.11)
net_salary = (gross_salary) - (income_tax + inss_value + syndicate_value)

print('\nSalário bruto =', hourly_earnings,'X',hours , '=', gross_salary)
print('Desconto IR =', income_tax)
print('Desconto INSS(-10%) =',inss_value)
print('Desconto do Sindicato =',syndicate_value)
print('FGTS(não descontado!) =',fgts_value)
print('Salário Bruto =',net_salary)

