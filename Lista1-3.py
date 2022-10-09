peso_arquivo = float(input('Informe quantopesa o arquivo em MB: '))
internet = float(input('Informe a velocidade de sua internet em Mbps: '))
tempo = ((peso_arquivo*8)/internet)/60
print(f"O tempo necessário para dowolad é:", tempo, " minutos.")
