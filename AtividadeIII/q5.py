# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 à 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

number = int(input('\nDigite um número para formar a tabuada: '))
multiplication_table = 10

for i in range(multiplication_table + 1):
    total = number * i
    print(number, 'x', i , '=',total)
