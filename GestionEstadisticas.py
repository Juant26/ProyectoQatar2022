import GestionPartidosEstadios
import os,sys

def promedio_gasto_vip():
    #abrir archivo boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r') as archivo:
        boletos = archivo.readlines()

    total_boletos = 0
    for boleto in boletos:
        precio = boleto.split(',')[3].split(' ')[-1]
        total_boletos += float(precio)

    #abrir archivo compras
    with open(os.path.join(sys.path[0], 'compras.txt'), 'r') as archivo:
        compras = archivo.readlines()

    total_compras = 0
    for compra in compras:
        precio = compra.split(',')[1]
        total_compras += float(precio)

    # promedio total
    promedio_total = (total_boletos + total_compras) / (len(boletos) + len(compras))

    return promedio_total

def tabla_asistencia():
    # abrir archivo asistencia
    with open(os.path.join(sys.path[0], 'asistencia.txt'), 'r') as archivo:
        asistencias = archivo.readlines()

    # abrir archivo boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r') as archivo:
        boletos = archivo.readlines()

    # contar ocurriencias de asistencia
    asistencias_dict = {}
    for asistencia in asistencias:
        if asistencia.strip() in asistencias_dict:
            asistencias_dict[asistencia.strip()] += 1
        else:
            asistencias_dict[asistencia.strip()] = 1

    # contrar ocurrencias de boletos
    boletos_dict = {}
    for boleto in boletos:
        if boleto.split(',')[7].split(' ')[-1] in boletos_dict:
            boletos_dict[boleto.split(',')[7].split(' ')[-1]] += 1
        else:
            boletos_dict[boleto.split(',')[7].split(' ')[-1]] = 1

    # info partidos
    partidos = GestionPartidosEstadios.obtener_partidos()
    for partido in partidos:
        id = str(partido.id)
        if id in asistencias_dict:
            asis = asistencias_dict[id]
            partido = f"{partido}, Asistencia: {asis}"
        else:
            asis = 0
            partido = f"{partido}, Asistencia: {asis}"

        if id in boletos_dict:
            bolets = boletos_dict[id]
            partido = f"{partido}, Boletos Vendidos: {bolets}"
        else:
            bolets = 0
            partido = f"{partido}, Boletos Vendidos: {bolets}"

        # calcular relacion
        if bolets > 0:
            relacion = asis / bolets
        else:
            relacion = 0

        partido = f"{partido}, Relacion: {relacion}"

        print(partido)

def partido_mas_asistencia(partidos):
    # abrir archivo asistencia
    with open(os.path.join(sys.path[0], 'asistencia.txt'), 'r') as archivo:
        asistencias = archivo.readlines()

    # contar ocurriencias de asistencia
    asistencias_dict = {}
    for asistencia in asistencias:
        if asistencia.strip() in asistencias_dict:
            asistencias_dict[asistencia.strip()] += 1
        else:
            asistencias_dict[asistencia.strip()] = 1

    # obtener partido con mayor asistencia
    max_asistencia = 0
    id_partido = 0
    for id, asis in asistencias_dict.items():
        if asis > max_asistencia:
            max_asistencia = asis
            id_partido = id

    for partido in partidos:
        if str(partido.id) == id_partido:
            print(f"El partido con mayor asistencia es: {partido} con {max_asistencia} asistentes")

def partido_mas_boletos(partidos):
    # abrir archivo boletos
    with open(os.path.join(sys.path[0], 'asistencia.txt'), 'r') as archivo:
        boletos = archivo.readlines()

    # contar ocurriencias de boletos
    boletos_dict = {}
    for boleto in boletos:
        if boleto.split(',')[7].split(' ')[-1] in boletos_dict:
            boletos_dict[boleto.split(',')[7].split(' ')[-1]] += 1
        else:
            boletos_dict[boleto.split(',')[7].split(' ')[-1]] = 1

    # obtener partido con mayor asistencia
    max_boletos = 0
    id_partido = 0
    for id, bolets in boletos_dict.items():
        if bolets > max_boletos:
            max_boletos = bolets
            id_partido = id

    for partido in partidos:
        if str(partido.id) == id_partido:
            print(f"El partido con mayores boletos vendidos es: {partido} con {max_boletos} boletos vendidos")

def tres_productos_mas_vendidos():
    # abrir archivo compras
    with open(os.path.join(sys.path[0], 'compras.txt'), 'r') as archivo:
        compras = archivo.readlines()

    # contar ocurriencias de compras
    compras_dict = {}
    for compra in compras:
        for producto in compra.split('[')[1].replace("'", '').replace(", ", ",").split(']')[0].split(','):
            if producto in compras_dict:
                compras_dict[producto] += 1
            else:
                compras_dict[producto] = 1

    # obtener los 3 productos mas vendidos
    productos = []
    for producto, cantidad in compras_dict.items():
        productos.append((producto, cantidad))

    productos.sort(key=lambda x: x[1], reverse=True)

    print(f"Los 3 productos mas vendidos son: {productos[0]}, {productos[1]}, {productos[2]}")


def tres_clientes_mas_boletos():
    # abrir archivo boletos
    with open(os.path.join(sys.path[0], 'boletos.txt'), 'r') as archivo:
        boletos = archivo.readlines()

    # contar ocurriencias de boletos
    boletos_dict = {}
    for boleto in boletos:
        cliente = boleto.split(',')[5].split(' ')[-1]
        if cliente in boletos_dict:
            boletos_dict[cliente] += 1
        else:
            boletos_dict[cliente] = 1

    # obtener los 3 clientes que mas compraron
    clientes = []
    for cliente, cantidad in boletos_dict.items():
        clientes.append((cliente, cantidad))

    clientes.sort(key=lambda x: x[1], reverse=True)

    print(f"Los 3 clientes que mas compraron boletos son los de las cedulas: {clientes[0]}, {clientes[1]}, {clientes[2]}")