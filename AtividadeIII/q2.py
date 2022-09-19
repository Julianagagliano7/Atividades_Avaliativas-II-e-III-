#Faça um Programa que leia três números e mostre o maior e o menor deles.

def highest_value(x,y,z):
    biggest = x
    if y > biggest:
        biggest = y
    elif z > biggest:
        biggest = z
    return biggest

def lowest_value (x,y,z):
    lowest = x
    if y < lowest:
        lowest = y
    elif z < lowest:
        lowest = y
    return lowest

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

print('\nMaior valor:',highest_value(a,b,c))
print('\nMenor valor:',lowest_value(a,b,c))