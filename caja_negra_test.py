# PRUEBA DE CAJA NEGRA
# Se basan en la especificacion de la funcion o del programa.
# Prueba inputs y valida outputs
# Unit testing: prueba modulo por modulo
# Integration testing: prueba la integracion de los modulos.

# modulo de python que permite generar pruebas
import unittest


def suma(num_1, num_2):
    return num_1 + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -15
        num_2 = -20

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -35)


if __name__ == '__main__':
    unittest.main()
