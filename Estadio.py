class Estadio:
    def __init__(self, id, nombre, ubicacion, capacidad, restaurantes):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.restaurantes = restaurantes

    def __str__(self):
        return f'Nombre: {self.nombre}, Ubicacion: {self.ubicacion}, Capacidad: {self.capacidad}, Restaurantes: {self.restaurantes}'