# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1, 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;

total_votes = total_votes_lula = total_votes_jair = total_votes_ciro = total_votes_tebet = total_votes_null = total_votes_white = 0
start = percentage = 0

print('\n-------------------Eleições 2022-------------------------\n')

print('1 - Lula')
print('2 - Jair Bolsonaro')
print('3 - Ciro Gomes')
print('2 - Bolsonaro')
print('4 - Simone Tebet')
print('5 - Nulo')
print('6 - Branco')

start = int(input('\nDeseja iniciar o processo de votação? 1 - Sim / 0 - Não \n'))

while start != 0:
    vote_number = int(input('\nDigite o número do seu candidato:'))
    match vote_number:
        case 1:
            total_votes_lula+=1
            print('Você votou no Lula!')
        case 2:
            total_votes_jair+=1
            print('Você votou no Bolsonaro!')
        case 3:
            total_votes_ciro+=1
            print('Você votou no Ciro Gomes')
        case 4:
            total_votes_tebet+=1
            print('Você votou em Simone Tebet')
        case 5:
            total_votes_null+=1
            print('Você votou nulo!')
        case 6:
            total_votes_white+=1
            print('Você votou em branco!')
    total_votes+=1
    start = int(input('\nDeseja votar mais uma vez? Sim - 1 / 0 - Não \n'))

percentage = ((total_votes_null / total_votes) * 100)

print('\nQuantia total de Votos:', total_votes)
print('\nTotal de Votos no Lula:',total_votes_lula)
print('\nTotal de Votos no Bolsonaro:',total_votes_jair)
print('\nTotal de Votos no Ciro:',total_votes_ciro)
print('\nTotal de Votos na Simone Tebet:',total_votes_tebet)
print('\nTotal de Votos NULOS:',total_votes_null)
print('\nTotal de Votos BRANCOS:',total_votes_white)
print(f'\nPercentagem entre votos nulos e total de votos= {percentage :.2f}','%')