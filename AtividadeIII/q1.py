# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def average_calculation(x,y):
    average = (x + y)/2
    if average >= 7.0:
        print('Aprovado!')
    elif average < 7.0:
        print('Reprovado!')
    elif average == 10:
        print('Aprovado com distinção!')
    else:
        print('Inserção de notas inválidas!')
    return average

a = int(input('Digite a primeira nota: (0-10): '))
b = int(input('Digite a segunda nota:  (0-10): '))

print(average_calculation(a,b))