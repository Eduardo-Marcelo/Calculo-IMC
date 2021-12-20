print('Olá, Seja bem-vindo')
print('Para começar precisamos de algumas informações')

peso = int(input('Informe seu peso: '))

altura = float(input("Informe sua altura: "))

resultado = peso / (altura * altura)

if resultado < 18.5:
    print('Abaixo do peso')
elif resultado > 18.5 and resultado < 24.9:
    print('Peso ideal')
elif resultado > 25 and resultado < 29.9:
    print('Sobrepeso')
elif resultado > 30 and resultado < 39.9:
    print('Obeso')
elif resultado > 40:
    print('Obeso Mórbido')            
