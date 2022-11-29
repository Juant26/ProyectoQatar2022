class Producto:
    def __init__(self, nombre, cantidad, precio, tipo, adicional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.tipo = tipo
        self.adicional = adicional

    def __str__(self):
        return f'Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}, Tipo: {self.tipo}, Adicional: {self.adicional}'