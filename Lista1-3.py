shora = int(input("Informe seu salário por hora: "))
horas = int(input("Informe o número de horas trabalhadas no mês: "))
sbruto = shora * horas
print("Seu salário bruto é de: ", sbruto)
ir = (sbruto*0.11)
inss = (sbruto*0.08)
print('Você pagou ao INSS o valor de: ',inss)
sind = (sbruto*0.05)
print('Você pagou ao sindicato o valor de: ',sind)
descontos = ir + inss + sind
stotal = (sbruto - descontos)
print("O Seu salário liquido foi de: ",stotal)
print ("Você pagou:",descontos , "de desconto" )
