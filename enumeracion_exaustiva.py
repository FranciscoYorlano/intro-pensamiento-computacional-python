import time as t


def main():

    numero = int(input("Elige un número:"))
    respuesta = 0
    inicio = t.time()
    while respuesta**2 < numero:
        print(respuesta)
        respuesta += 1
    if respuesta**2 == numero:
        print(f'La raiz cuadrada de {numero} es {respuesta}')
    else:
        print(f'{numero} no tiene raiz exacta')
    print(f'El programa resolvio en {(t.time()-inicio)*1000} milisegundos.')


if __name__ == '__main__':
    main()
