import unittest
from parte2.logica import fibonacci, fibonacci_memo, analizar_texto


class TestLogica(unittest.TestCase):

    def test_fibonacci(self):
        # Prueba para Fibonacci recursivo
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_memo(self):
        # Prueba para Fibonacci optimizado
        self.assertEqual(fibonacci_memo(5), 5)
        self.assertEqual(fibonacci_memo(10), 55)

    def test_analizar_texto(self):
        # Prueba para la función de analizar texto
        texto = "Hola, este es un ejemplo de análisis."
        resultado = analizar_texto(texto)
        # Comprobamos que los resultados sean correctos
        self.assertEqual(resultado, {'palabras': 7, 'letras': 29})

