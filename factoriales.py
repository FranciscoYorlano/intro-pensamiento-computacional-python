import sys


def factorial(n):
    '''
    Calcula n! por recursividad
    n int 
    return n!
    '''
    print(f'Se va a calcular {n}!')

    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def factorial_for(n):
    '''
    Calcula n! mediante productoria
    n int
    return n!
    '''
    i = 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    return factorial


def main():
    # EL MÁXIMO DE RECURSIVIDAD ES 1000, O SEA QUE UNA FUNCION PUEDE LLAMARSE A SI
    # MISMA HASTA 1000 VECES.
    # imprimimos el limite de recursion que trae python por defecto:
    print(
        f'El numero máximo de recursion por default es: {sys.setrecursionlimit(10000)}')

    n = int(input('Escribe un número entero para calcular su factorial: '))

    print(f'El factorial de {n} calculado mediante recursividad es:')
    print(factorial(n))

    print(f'El factorial de {n} calculado mediante for es:')
    print(factorial_for(n))


if __name__ == '__main__':
    main()
