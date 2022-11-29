class Equipo:
    def __init__(self, id, nombre_pais, codigo_fifa, bandera, grupo):
        self.id = id
        self.nombre_pais = nombre_pais
        self.codigo_fifa = codigo_fifa
        self.bandera = bandera
        self.grupo = grupo

    def __str__(self):
        return f'Nombre del pais: {self.nombre_pais}, Codigo FIFA: {self.codigo_fifa}, Bandera: {self.bandera}, Grupo: {self.grupo}'