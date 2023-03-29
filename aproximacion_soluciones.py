import time


def main():
    # numero objetivo al que se le quiere calcular la raiz cuadrada
    n = int(input("Elegí un número: "))

    # error aceptado
    epsilon = 0.01

    # paso que se ira sumando secuencialemente hasta aproximarse a la raiz cuadrada de n
    paso = episilon**2

    # se comienza desde 0.0
    respuesta = 0.0

    # inicio de cronometro
    inicio = time.time()

    # mientras que el modulo de la diferencia entre la respuesta al cuadrado y el numero n
    # sea mayor al error aceptado lo que hace este bucle es ir sumando a la respuesta el paso
    # previamente definido (en este caso epsilon al cuadrado).
    # además tambien se tiene que cumplir que la respuesta sera menor o igual al numero n
    # esto para prevenir bucles infinitos.
    while abs(respuesta**2 - n) >= episilon and respuesta <= n:
        print(respuesta)
        respuesta += paso

    if abs(respuesta**2 - n) >= episilon:
        print(
            f'No se encontro la raiz cuadrada de {n}. El ultimo valor probado fue {respuesta}')
    else:
        print(f'La raiz cuadrada de {n} es proxima a {respuesta}')

    #
    print(f'Se resolvio en {time.time()-inicio} segundos')


if __name__ == '__main__':
    main()
