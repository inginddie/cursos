objetivo = int(input('Escoge un entero:  '))
respuesta = 0

while respuesta ** 2 < objetivo:
    print (respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada del {objetivo} es {respuesta}')
else:
    print(f'El {objetivo} no tiene una raiz cuadrada exacta')