def run():
    LIMITE = 1000 #las constantes deben estar en MAY

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: #mientras potencia2 sea menor a LIMITE se queda en el bucle
        print('2 elevado a ' + str(contador) + ' es igual a:  ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()