def convertidor(tipo_pesos, valor_dolar):
    pesos = input('cuantos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ('tienes $' + dolares + ' dolares')

menu = '''
Bienvenido al convertidor de ⌚

1 - Pesos colombianos
2 - mexicanos
3 - argentinos

Elige una opción: '''

opcion = input(menu)

if opcion == '1':
    convertidor('colombianos', 3500)
elif opcion == '2':
    convertidor('mexicano', 24)
elif opcion == '3':
    convertidor('argentino', 65)
else:
    print(' porfavor volver a ejecutar una opción correcta')



