import random

def generar_pass():
    may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
    minu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
    simbolos = ['!', '#', '$', '%', '&', '/', '(', ')']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    caracteres = may + minu + simbolos + nums  #se crea la var caracteres para reunir los listados

    password = []

    for i in range(25):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)
    password = "".join(password)
    return password

def run():
    password = generar_pass()
    print('Tu nueva contraseña es:  ' + password)

if __name__ == "__main__":
    run()