
tamanho_arquivo = float(input("Qual é o tamanho do arquivo que deseja baixar em MB? "))

velocidade_internet = float(input("Qual é a velocidade de download em Mpbs? "))

arquivo_em_mbps = tamanho_arquivo * 8

tempo_download = float(arquivo_em_mbps / velocidade_internet)

minutos = tempo_download // 60
segundos = tempo_download % 60

print(f"Para baixar esse arquivo de tamanho {tamanho_arquivo}MB\n"
      f"com um velocidade de download de {velocidade_internet}/Mbps\n"
      f"irá demorar cerca de {minutos:.0f} minutos e {segundos:.0f} segundos")
