def factorial(n):
    """[Calculo factorial]
        Calcula el factorial de n.
        n int > 0
        return n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input(f'Escribe un entero:  '))

print(factorial(n))

##----OTRA FORMA DE HACERLO PERO YA CON UNA LIBRERIA---##
# import sys
# print(sys.getrecursionlimit(1))