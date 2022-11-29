from Cliente import Cliente
from Boleto import Boleto
import random
import string
import os,sys

def obtener_datos_cliente(partidos):
    # ingresar los datos del cliente con sus respectivas validaciones
    nombre = input('Ingrese su nombre: ')
    while not nombre.isalpha():
        print('Nombre invalido')
        nombre = input('Ingrese su nombre: ')
    cedula = input('Ingrese su cedula: ')
    while not cedula.isdigit() or len(cedula) < 7:
        print('Cedula invalida')
        cedula = input('Ingrese su cedula: ')
    edad = input('Ingrese su edad: ')
    while not edad.isdigit() or int(edad) < 0:
        print('Edad invalida')
        edad = input('Ingrese su edad: ')

    # mostrar los partidos
    print('Partidos:')
    for i in range(len(partidos)):
        print(f'{i+1}. {partidos[i]}')

    # seleccionar el partido
    partido = input('Seleccione el partido que desea comprar: ')
    while not partido.isdigit() or int(partido) < 1 or int(partido) > len(partidos):
        print('Partido invalido')
        partido = input('Seleccione el partido que desea comprar: ')
    partido = partidos[int(partido)-1]

    # seleccionar el tipo de entrada
    tipo_entrada = input('Seleccione el tipo de entrada que desea comprar (General o VIP): ')
    while tipo_entrada.lower() != 'general' and tipo_entrada.lower() != 'vip':
        print('Tipo de entrada invalido')
        tipo_entrada = input('Seleccione el tipo de entrada que desea comprar (General o VIP): ')
    tipo_entrada = tipo_entrada.lower()

    # crear el cliente
    cliente = Cliente(nombre, cedula, edad, partido, tipo_entrada)
    return cliente

def obtener_asiento(mapa):
    # mostrar el mapa del estadio
    print('Mapa del estadio:')
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            print(mapa[i][j], end=' ')
        print()

    # seleccionar el asiento
    asiento = input('Seleccione el asiento que desea comprar: ')
    while not asiento.isdigit() or int(asiento) < 1 or int(asiento) > len(mapa)*len(mapa[0]):
        print('Asiento invalido')
        asiento = input('Seleccione el asiento que desea comprar: ')
    asiento = int(asiento)

    # obtener la fila y columna del asiento
    fila = 0
    columna = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == asiento:
                fila = i
                columna = j
                break

    # verificar si el asiento esta ocupado
    if mapa[fila][columna] == 'X':
        print('El asiento esta ocupado, seleccione otro')
        return obtener_asiento(mapa)
    else:
        return mapa[fila][columna], fila, columna
    
def calcular_costo_entrada(cliente):
    # calcular el costo de la entrada
    if cliente.tipo_entrada == 'general':
        costo_entrada = 50
    else:
        costo_entrada = 120

    # calcular el iva
    iva = costo_entrada * 0.16

    # calcular el total
    total = costo_entrada + iva

    return costo_entrada, iva, total


def crear_compra(partidos, mapa):

    # obtener los datos del cliente
    cliente = obtener_datos_cliente(partidos)

    # obtener el asiento
    asiento, fila, columna = obtener_asiento(mapa)

    # calcular el costo de la entrada
    costo_entrada, iva, total = calcular_costo_entrada(cliente)

    # generar codigo unico del boleto
    letras = string.ascii_lowercase
    codigo = ''.join(random.choice(letras) for i in range(6))

    # crear boleto
    boleto = Boleto(codigo, asiento, total, cliente)

    # mostrar la compra
    print('Compra:')
    print(f'Nombre: {cliente.nombre}')
    print(f'Cedula: {cliente.cedula}')
    print(f'Edad: {cliente.edad}')
    print(f'Partido: {cliente.partido}')
    print(f'Tipo de entrada: {cliente.tipo_entrada}')
    print(f'Asiento: {boleto.asiento}')
    print(f'Costo: {costo_entrada}')
    print(f'IVA: {iva}')
    print(f'Total: {total}')

    # confirmar compra
    confirmacion = input('¿Desea confirmar la compra? (Si/No): ')
    while confirmacion.lower() != 'si' and confirmacion.lower() != 'no':
        print('Opcion invalida')
        confirmacion = input('¿Desea confirmar la compra? (Si/No): ')
    confirmacion = confirmacion.lower()

    if confirmacion == 'si':
        # cambiar el asiento a ocupado
        mapa[fila][columna] = 'X'

        # guardar el boleto en el archivo
        with open(os.path.join(sys.path[0], 'boletos.txt'), 'a') as archivo:
            archivo.write(f'{boleto}\n')
        
            print('Pago exitoso, su codigo de compra es:', codigo)
    
    else:
        return None
