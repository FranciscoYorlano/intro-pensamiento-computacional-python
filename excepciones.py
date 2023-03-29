
def divide_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista_1 = list(range(20))


# print(divide_lista(lista_1, 0))
print('123' + '456')
