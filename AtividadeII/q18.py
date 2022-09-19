#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

file_size = float(input('Digite o tamanho do arquivo em (MB): '))

speed = float(input('Digite a velocidade de um link de internet em (MBPS): '))

time = (file_size / speed)

print('Demorará ', time, 'segundos para realizar o download deste arquivo')