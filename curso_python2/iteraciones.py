#WHILE
#CASO 1: Sencillo
# contador = 0
# while contador <= 10:
#     print(contador)
#     contador += 1

#CASO 2: duos
con_int = 0
con_ext = 0

while con_ext < 5:
    while con_int < 6:
        print(con_ext, con_int)
        con_int += 1

        if con_int >= 3: #si se desea colocar un break o pausa en cierto numero
            break
    con_ext += 1
    con_int = 0
