#def imprimir_mensaje():
#    print('mensaje especial')
#    print('aprendiendo a realizar funciones')

#imprimir_mensaje()

def convesacion(mensaje):
    print('hola')
    print('como estas')
    print(mensaje)
    print('adios')

opcion = int(input(' elije una opcion 1,2,3: '))
if opcion == 1:
    convesacion('elegiste la opcion ' + str(opcion) )
elif opcion == 2:
    convesacion('elegiste la opcion ' + str(opcion) )
elif opcion == 3:
    convesacion('elegiste la opcion ' + str(opcion) )
else:
    print('elige una opción')
