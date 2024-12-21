import unittest
from parte1.producto import Producto


class TestProducto(unittest.TestCase):

    def test_calcular_precio_total(self):
        # Crear un producto con nombre, descripcion, precio y cantidad
        producto = Producto("Laptop", "Computadora portátil", 1200.0, 2)
        # Verificar que el precio total calculado sea correcto
        self.assertEqual(producto.calcular_precio_total(), 2400.0)

    def test_descripcion_correcta(self):
        # Crear un producto con nombre, descripcion, precio y cantidad
        producto = Producto("Celular", "Un celular de alta gama", 1200.0, 2)
        # Verificar que la descripcion del producto sea la correcta
        # Corregir a descripcion
        self.assertEqual(producto.descripcion, "Un celular de alta gama")

    def test_cantidad_incorrecta(self):
        # Verificar que se lance un ValueError cuando la cantidad es negativa
        with self.assertRaises(ValueError):
            Producto("TV", "Televisor de 40 pulgadas", 500.0, -3)

