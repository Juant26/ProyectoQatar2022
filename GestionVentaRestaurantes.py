import json
import os,sys

# obtener cedula y buscar cliente en archivo boletos
def obtener_datos_cliente(boletos, restaurantes):
    # obtener cedula
    cedula = input('Ingrese su cedula: ')
    while not cedula.isdigit():
        print('Cedula invalida')
        cedula = input('Ingrese su cedula: ')

    es_vip = False
    # validar la cedula
    for boleto in boletos:
        cedula_boleto = boleto.split(',')[5].split(' ')[-1]
        tipo_entrada_boleto = boleto.split(',')[-1].split(' ')[-1]

        if cedula == cedula_boleto and tipo_entrada_boleto.strip() == 'vip':
            print('VIP validado')
            es_vip = True
            id_estadio_boleto = boleto.split(',')[-2].split(' ')[-1]
            edad_boleto = boleto.split(',')[6].split(' ')[-1]
            obtener_datos_comida(cedula, edad_boleto, id_estadio_boleto, restaurantes)

    if not es_vip:
        print('No es VIP')

def es_numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero


def obtener_datos_comida(cedula, edad, id_estadio, restaurantes):
    # obtener los restaurantes del estadio
    for restaurante in restaurantes:
        id_estadio_restaurante = restaurante.split('/')[0]

        if id_estadio_restaurante == id_estadio:
            res = [json.loads(idx.replace("'", '"')) for idx in [restaurante.split('/')[1]]]
            res = res[0]

            # mostrar restaurantes
            print('Restaurantes disponibles:')
            for i in range(len(res)):
                print(f'{i+1}. {res[i]["name"]}')

            # obtener restaurante
            rest = input('Ingrese el numero del restaurante: ')
            while not rest.isdigit() or int(rest) > len(res):
                print('Restaurante invalido')
                rest = input('Ingrese el numero del restaurante: ')

            # mostrar productos
            print('Productos disponibles:')
            if int(edad) < 18:
                print('Productos disponibles para menores de edad')
                for i in range(len(res['products'])):
                    if res['products'][i]['tipo'] != 'alcoholic':
                        precio = res[int(rest)-1]["products"][i]["price"] + res[int(rest)-1]["products"][i]["price"] * 0.16
                        print(f'{i+1}. {res[int(rest)-1]["products"][i]["name"]} - ${precio}')
            else:
                print('Productos disponibles')
                for i in range(len(res[int(rest)-1]['products'])):
                    precio = res[int(rest)-1]["products"][i]["price"] + res[int(rest)-1]["products"][i]["price"] * 0.16
                    print(f'{i+1}. {res[int(rest)-1]["products"][i]["name"]} - ${precio}')

            # obtener productos
            productos = []

            while True:
                producto = input('Seleccione el producto que desea comprar: ')
                while not producto.isdigit() or int(producto) < 1 or int(producto) > len(res[int(rest)-1]["products"]):
                    print('Producto invalido')
                    producto = input('Seleccione el partido que desea comprar: ')

                precio = res[int(rest)-1]["products"][int(producto)-1]["price"] + res[int(rest)-1]["products"][int(producto)-1]["price"] * 0.16
                productos.append(f'{res[int(rest)-1]["products"][int(producto)-1]["name"]} - ${precio}')
                print('Producto agregado')
                continuar = input('Desea agregar otro producto? (s/n): ')
                while continuar != 's' and continuar != 'n':
                    print('Opcion invalida')
                    continuar = input('Desea agregar otro producto? (s/n): ')
                if continuar == 'n':
                    break

            # calcular total
            total = 0
            for producto in productos:
                total += float(producto.split('$')[-1])

            # calcular descuento
            descuento = 0
            if es_numero_perfecto(int(cedula)):
                descuento = total * 0.15

            # mostrar total
            print(f'Productos: {productos}')
            print(f"Subtotal: ${total}")
            print(f"Descuento: ${descuento}")
            print(f"Total a pagar: ${total - descuento}")

            # confirmar compra
            confirmar = input('Desea confirmar la compra? (s/n): ')
            while confirmar != 's' and confirmar != 'n':
                print('Opcion invalida')
                confirmar = input('Desea confirmar la compra? (s/n): ')
            if confirmar == 's':
                print('Compra exitosa')
                print(f"Subtotal: ${total}")
                print(f"Descuento: ${descuento}")
                print(f"Total a pagar: ${total - descuento}")
                print('Gracias por su compra')



                # restar del inventario
                for producto in productos:
                    nombre = producto.split('-')[0].strip()
                    for i in range(len(res[int(rest)-1]["products"])):
                        if res[int(rest)-1]["products"][i]["name"].lower() == nombre.lower():
                            res[int(rest)-1]["products"][i]["quantity"] -= 1
                            break


                restaurantes.remove(restaurante)
                restaurantes.append(f'{id_estadio_restaurante}/{res}\n')

                
                # guardar cambios
                with open(os.path.join(sys.path[0], 'restaurantes.txt'), 'w') as f:
                    f.writelines(restaurantes)

                # solo guardar nombre de productos
                productos = [producto.split('-')[0].strip() for producto in productos]

                # guardar compra
                with open(os.path.join(sys.path[0], 'compras.txt'), 'a') as f:
                    f.write(f'{cedula},{total-descuento},{productos}\n')

                return

            else:
                print('Compra cancelada')
                return