class Cliente:
    def __init__(self, nombre, cedula, edad, partido, tipo_entrada):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.tipo_entrada = tipo_entrada

    def __str__(self):
        return f'Nombre: {self.nombre}, Cedula: {self.cedula}, Edad: {self.edad}, Partido: {self.partido}, Tipo de entrada: {self.tipo_entrada}'