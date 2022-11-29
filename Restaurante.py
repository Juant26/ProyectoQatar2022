class Restaurante:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def __str__(self):
        return f'Nombre: {self.nombre}, Productos: {self.productos}'