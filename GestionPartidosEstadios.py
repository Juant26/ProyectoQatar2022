import os, sys
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
import json
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido

def obtener_equipos():
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'
    response = requests.get(url)
    equipos_api = json.loads(response.text)

    # guardar los equipos en una lista de objetos
    equipos_obtenidos = []
    for equipo in equipos_api:
        equipos_obtenidos.append(Equipo(equipo['id'], equipo['name'], equipo['fifa_code'], equipo['flag'], equipo['group']))

    return equipos_obtenidos

def obtener_estadios():
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json'
    response = requests.get(url)
    estadios_api = json.loads(response.text)

    # guardar los estadios en una lista de objetos
    estadios_obtenidos = []
    for estadio in estadios_api:
        estadios_obtenidos.append(Estadio(estadio['id'], estadio['name'], estadio['location'], estadio['capacity'], estadio['restaurants']))

    return estadios_obtenidos

# guardar los restaurantes de cada estadio en un archivo
def guardar_restaurantes(estadios):
    # guardar los restaurantes en el archivo
    with open(os.path.join(sys.path[0], 'restaurantes.txt'), 'w') as archivo:
        for e in estadios:
            archivo.write(f'{e.id}/{e.restaurantes}\n')


def obtener_partidos():
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json'
    response = requests.get(url)
    partidos_api = json.loads(response.text)

    # guardar los partidos en una lista de objetos
    partidos_obtenidos = []
    for partido in partidos_api:
        partidos_obtenidos.append(Partido(partido['id'], partido['home_team'], partido['away_team'], partido['date'], partido['stadium_id']))

    return partidos_obtenidos

def obtener_partidos_por_equipo(equipos, partidos):
    # obtener el equipo
    equipo = input('Ingrese el nombre del equipo: ')
    equipo = equipo.lower()

    # buscar el equipo en la lista de equipos
    for e in equipos:
        if equipo == e.nombre_pais.lower():
            # si el equipo existe, buscar los partidos
            print(f'Partidos de {e.nombre_pais}:')
            for p in partidos:
                if e.nombre_pais == p.equipo_local or e.nombre_pais == p.equipo_visitante:
                    print(f'Equipo Local: {p.equipo_local}, Equipo Visitante: {p.equipo_visitante}, Fecha y Hora: {p.fecha_hora}, Estadio: {p.id_estadio}')
            break
    else:
        print('El equipo no existe')


def obtener_partidos_por_estadio(estadios, partidos):
    # obtener el estadio
    estadio = input('Ingrese el nombre del estadio: ')
    estadio = estadio.lower()

    # obtener el id del estadio
    for e in estadios:
        if estadio == e.nombre.lower():
            id_estadio = e.id
            break
    else:
        print('El estadio no existe')
        return

    # buscar el estadio en la lista de estadios
    for p in partidos:
        if id_estadio == p.id_estadio:
            print(f'Equipo Local: {p.equipo_local}, Equipo Visitante: {p.equipo_visitante}, Fecha y Hora: {p.fecha_hora}, Estadio: {estadio}')

def obtener_partidos_por_fecha(estadios, partidos):
    # obtener la fecha
    fecha = input('Ingrese la fecha (mm/dd/aaaa): ')

    # buscar los partidos en la fecha
    print(f'Partidos en la fecha {fecha}:')
    for p in partidos:
        if fecha == p.fecha_hora[:10]:

            # obtener el nombre del estadio
            for e in estadios:
                if p.id_estadio == e.id:
                    estadio = e.nombre
                    break

            print(f'Equipo Local: {p.equipo_local}, Equipo Visitante: {p.equipo_visitante}, Fecha y Hora: {p.fecha_hora}, Estadio: {estadio}')