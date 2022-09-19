#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

height = float(input('\nDigite sua altura: '))
ideal_weight_women = ((72.7 * height) - 58)
ideal_weight_men = ((62.1 * height) - 44.7)

print('\nPeso ideal (mulher): ' , ideal_weight_women)
print('Peso ideal (homem): ' ,  ideal_weight_men)
