import GestionPartidosEstadios
import GestionVentaEntradas
import GestionAsistenciaPartidos
import GestionEstadisticas
import GestionVentaRestaurantes
import os,sys

def main():

    # obtener los equipos, estadios y partidos
    equipos = GestionPartidosEstadios.obtener_equipos()
    estadios = GestionPartidosEstadios.obtener_estadios()
    partidos = GestionPartidosEstadios.obtener_partidos()

    # crear el mapa del estadio
    mapa = []
    for i in range(10):
        fila = []
        for j in range(10):
            fila.append((i*10)+j+1)
        mapa.append(fila)

    # abrir el archivo de boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r') as archivo:
        boletos = archivo.readlines()

    # abrir archivo restaurantes
    with open(os.path.join(sys.path[0], 'restaurantes.txt'), 'r') as archivo:
        restaurantes = archivo.readlines()

    # obtener restaurantes con id de cada estadio
    #GestionPartidosEstadios.guardar_restaurantes(estadios)

    print('Bienvenido al sistema de gestión de partidos y estadios')
    print('1. Obtener partidos de un equipo')
    print('2. Obtener partidos de un estadio')
    print('3. Obtener partidos de una fecha')
    print('5. Comprar boleto')
    print('6. Usar boleto')
    print('7. Comprar en restaurantes')
    print('8. Obtener estadísticas')
    print('9. Salir')
    opcion = input('Ingrese una opción: ')
    while opcion != '9':
        if opcion == '1':
            GestionPartidosEstadios.obtener_partidos_por_equipo(equipos, partidos)
        elif opcion == '2':
            GestionPartidosEstadios.obtener_partidos_por_estadio(estadios, partidos)
        elif opcion == '3':
            GestionPartidosEstadios.obtener_partidos_por_fecha(estadios, partidos)
        elif opcion == '5':
            GestionVentaEntradas.crear_compra(partidos, mapa)
            # recargar el archivo de boletos
            with open('boletos.txt', 'r') as archivo:
                boletos = archivo.readlines()
        elif opcion == '6':
            # obtener el codigo del boleto
            codigo = input('Ingrese el codigo del boleto: ')

            GestionAsistenciaPartidos.validar_boleto(boletos, codigo)
        elif opcion == '7':
            GestionVentaRestaurantes.obtener_datos_cliente(boletos, restaurantes)
            # recargar archivo restaurantes
            with open('restaurantes.txt', 'r') as archivo:
                restaurantes = archivo.readlines()
        elif opcion == '8':
            print('1. Obtener promedio de gasto de un cliente VIP')
            print('2. Obtener datos de los partidos')
            print('3. Obtener partido con mayor asistencia')
            print('4. Obtener partido con mayores boletos vendidos')
            print('5. Obtener top 3 productos más vendidos')
            print('6. Obtener top 3 clientes con mas boletos')
            opcion2 = input('Ingrese una opción: ')
            print()
            if opcion2 == '1':
                print(f"El promedio de gasto de un client VIP es: {GestionEstadisticas.promedio_gasto_vip()}")
            elif opcion2 == '2':
                print(GestionEstadisticas.tabla_asistencia())
            elif opcion2 == '3':
                print(GestionEstadisticas.partido_mas_asistencia(partidos))
            elif opcion2 == '4':
                print(GestionEstadisticas.partido_mas_boletos(partidos))
            elif opcion2 == '5':
                print(GestionEstadisticas.tres_productos_mas_vendidos())
            elif opcion2 == '6':
                print(GestionEstadisticas.tres_clientes_mas_boletos())
            else:
                print('Opción inválida')
        else:
            print('Opción inválida')

        print()
        print('1. Obtener partidos de un equipo')
        print('2. Obtener partidos de un estadio')
        print('3. Obtener partidos de una fecha')
        print('5. Comprar boleto')
        print('6. Usar boleto')
        print('7. Comprar en restaurantes')
        print('8. Obtener estadísticas')
        print('9. Salir')

        opcion = input('Ingrese una opción: ')


main()