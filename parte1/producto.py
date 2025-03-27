class Producto:
    def __init__(self, nombre, descripcion, precio, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.precio * self.cantidad

    def __str__(self):
      return f"Producto(nombre={self.nombre}, descripcion={self.descripcion}, precio={self.precio}, cantidad={self.cantidad})"


p1 = Producto("Celular","Un celular de alta gama", 3000.0, 5)
print(p1.calcular_precio_total()) 
print(p1)  