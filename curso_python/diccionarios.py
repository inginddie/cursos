def run():
    diccionario = {
        'llave1 ': 1,
        'llave2 ': 2,
        'llave3 ': 3
    }
    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])

    pobracion_paises = {
        'Arg': 50,
        'BRA': 150,
        'Col': 20,
    }
    # print(pobracion_paises['Col'])

    for pais in pobracion_paises.keys(): #si solo quiero imprimir las llaves osea arg, bra, col
        print(pais)
    for pais in pobracion_paises.values(): #si solo quiero imprimir los valores
        print(pais)
    for pais, poblacion in pobracion_paises.items(): #si quiero imprimir todo mas una frase
        print(pais + ' ' +'Tiene ' + str(poblacion) + ' ' +'habitantes')

if __name__ == "__main__":
    run()