# Busqueda binaria es de los algoritmos mas eficientes
import time


def main():
    # definicion de número n y margen de error epsilon:
    n = int(input("Elige un número: "))
    epsilon = 0.000000000000001

    # minimo, maximo y respuesta x:
    minimo = 0.0
    maximo = max(1.0, n)
    x = (minimo + maximo) / 2

    # medición de iteraciones y tiempo de respuesta:
    iteraciones = 0
    inicio = time.time()

    # iteraciones de busqueda binaria
    while abs(x**2 - n) >= epsilon:
        if iteraciones > 99999:
            print(
                f'Se ha alcanzado el limite de iteraciones. Se obtuvo los siguientes resultados:')
            break
        print(f""" 
        =============ITERACIÓN: {iteraciones}
        minimo={minimo}; 
        maximo={maximo}; 
        x = {x}""")

        if x**2 < n:
            minimo = x
        else:
            maximo = x

        x = (minimo + maximo) / 2
        iteraciones += 1

    # respuesta x
    print(f'La raiz cuadrada de {n} es {x}')

    # conclusiones de medición:
    if time.time()-inicio >= 1:
        print(f'Se resolvio en {time.time()-inicio} segundos')
    else:
        print(f'Se resolvio en {(time.time()-inicio) * 1000} milisegundos')
    print(f'Iteraciones para respuesta = {iteraciones}')


if __name__ == '__main__':
    main()
