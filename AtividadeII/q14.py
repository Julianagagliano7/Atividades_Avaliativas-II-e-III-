#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


fish_weight = float(input('Digite o peso do peixe(kg): '))
max_weight = 50
fine_amount = 4

over_fish_weight = (fish_weight - max_weight)

if (over_fish_weight > 0):
    fine = (over_fish_weight * fine_amount)
else:
    fine = 0

print('\nO excesso em quilos foi: ', over_fish_weight)
print('\nO valor da multa é ', fine , 'reais')

