#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Informe o tamanho do arquivo para download: MB'))
internet = float(input('Informe a velocidade da sua internet(download): mbps')) #velocidade por segundo (mbps)
tam_arquivo = arquivo * 8 #conversão de Megabyte(MB) para megabit(mbps)

velocidade_seg = internet
velocidade_min = internet*60

download_seg = tam_arquivo/velocidade_seg
download_min = tam_arquivo/velocidade_min

print(f'O seu arquivo de {arquivo:.2f}MB com uma internet de {internet:.2f}mbps, baixará por completo em {download_seg:.2f} segundo(s) '
      f'e {download_min:.2f} minuto(s)')
