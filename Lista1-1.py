sexo = input('Digite o seu sexo(Ex: m ou h: ')

altura = float(input(f'Digite a sua altura(Ex:1.80): '))

if (sexo==h):
    pi = (72.7*altura)-58
    print("Seu peso ideal é:{pi}")

else:
    pi = ((62.1*altura)-44.7)
    print("Seu peso ideal é:{pi}")
