import os,sys

def validar_boleto(boletos, codigo):
    # validar el codigo
    for boleto in boletos:
        codigo_boleto = boleto.split(',')[0].split(' ')[-1]
        estado = boleto.split(',')[1].split(' ')[-1]

        if codigo == codigo_boleto and estado == 'False':
            # cambiar el estado del boleto a usado
            boletonew = boleto.replace('False', 'True')

            # registrar asistencia en archivo
            with open(os.path.join(sys.path[0], 'asistencia.txt'), 'a') as archivo:
                archivo.write(f"{boletonew.split(',')[7].split(' ')[-1]}\n")
            print('Boleto valido, asistencia registrada')
            # reemplazar el boleto en la lista de boletos
            boletos[boletos.index(boleto)] = boletonew

            # guardar los cambios en el archivo
            with open('boletos.txt', 'w') as archivo:
                archivo.writelines(boletos)
                return True

    print('Boleto invalido o usado')
    return False
