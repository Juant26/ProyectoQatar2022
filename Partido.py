class Partido:
    def __init__(self, id, equipo_local, equipo_visitante, fecha_hora, id_estadio):
        self.id = id
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha_hora = fecha_hora
        self.id_estadio = id_estadio

    def __str__(self):
        return f'id: {self.id}, Equipo Local: {self.equipo_local}, Equipo Visitante: {self.equipo_visitante}, Fecha y Hora: {self.fecha_hora}, Estadio: {self.id_estadio}'