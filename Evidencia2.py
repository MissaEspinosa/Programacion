# Se importa el modulo para creacion de tupla nominada
from collections import namedtuple
# Importacion de modulo FECHA para las validaciones
import datetime
# Importamos PANDAS para pasar los servicios y sus detalles a un CSV
import pandas as pd
# Creamos un diccionario para guardar los folios
diccionario = {}
# Creacion de tupla nominada para registros
Registros = namedtuple("Registro",("Fecha", "Nombre", "Servicio", "Equipos", "Montos"))
# Diccionario donde se almacenaran los registros 
registros = {}
# Funcion para creacion de registros
def RegistrarUnServicio():
    # Se crean listas para multiples servicios, equipos y sus respectivos montos sin iva
    listaServicios = []
    listaDeEquipos = []
    montosCobrados = []
    global registros
    print("-----Registrar un Servicio-----")
    nombre_cliente = input("Ingrese su nombre: ")
    # Ciclo para permitir solo formato de fecha valido
    while True:
        try:
            fecha_str = input("Ingrese la fecha en formato (dd/mm/aaaa): ")
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            print("El valor de la fecha que fue proporcionado no puede ser procesado")
            continue
        except Exception:
            print("Se ha presenrado una excepción")
            break
        else:
            # Al validarse la fecha se pasa a otro ciclo el cual servira para 
            # añadir diferentes servicios, equipos y sus montos que el cliente haya realizado.
            while True:
                servicio = input("Descripcion del servicio: ")
                # Se agregan valores a la lista de servicios realizados al cliente
                listaServicios.append(servicio)
                descripcion_del_equipo = input("Descripcion del equipo: ")
                listaDeEquipos.append(descripcion_del_equipo)
                # Ciclo para validar solo valores numericos
                while True:
                    try:
                        montoCobrado = float(input("Monto cobrado: "))
                        montosCobrados.append(montoCobrado)
                        break
                    except:
                        print("Error!! El monto debe ser numerico!!!")
                        continue
            # Opcion para salir del registro
                print('[n] no [Presionar ENTER] si')
                opcion = input("¿Desea agregar otro servicio?")
                if opcion == 'n':
                    break
            detalles = [listaServicios + listaDeEquipos]
            df_servicios = pd.DataFrame(detalles)
            df_servicios.to_csv("Servicios.csv", header=True, index=False)
# Se agregan valores a la tupla nominada junto a otras listas
            registro = Registros(fecha,nombre_cliente,listaServicios,listaDeEquipos,montosCobrados)
            if diccionario.keys():
                clave = max(diccionario.keys())+1
            else:
                clave = 1
                diccionario[clave] = registro
                print("¡Registro exitoso!")
                for llave in diccionario:
                    print(f"Este es tu folio: {llave}")
    
            registros[fecha] = registro
            montoMasIva = sum(montosCobrados)*.16
            montosCobrados = sum(montosCobrados) + montoMasIva
            print()
            print(f"El cliente {nombre_cliente} debe pagar un monto total con IVA incluido ${montosCobrados}")
            print()
            break
        
        # Funcion utilizada para mostrar todos los registros de servicios que hay actualmente
def DesplegarTodosLosDatos():
    print("\tFecha\tCliente\tServicios\tEquipos\tMontos Cobrado")
    print("-" * 50)
    for elemento in registros.items():
        print(f"{elemento[0]}{elemento[1][1]}\t{elemento[1][2]}\t{elemento[1][3]}\t{elemento[1][4]}")
        print("-" * 50)
        print()
# Funcion para consultar servicios realizados mediante folios de cliente
def BuscarFolio():
    llave = int(input("Ingrese el folio: "))
    print("-" * 50)
    print(f"Fecha del registro: {diccionario[llave].Fecha}")
    print(f"Nombre del cliente: {diccionario[llave].Nombre}")
    print(f"Descripcion del servicio: {diccionario[llave].Servicio}")
    print(f"Descripcion del equipo: {diccionario[llave].Equipos}")
    print("-" * 50)
# Funcion para consultar servicios realizados mediante fechas
def ConsultarPorFechas():
    global registros
    while True:
        try:
            buscarFecha = input("Fecha de la venta en formato (dd/mm/aaaa): ")
            fecha = datetime.datetime.strptime(buscarFecha, "%d,%m,%Y").date()
        except ValueError:
            print("El valor de la fecha que fue proporcionado no puede ser procesado")
            continue
        except Exception:
            print("Se ha presentado una excepcion")
            break
        else:
            for elemento in registros.items():
                if elemento[1][1] == fecha:
                    print("\nFolio\tFecha\tCliente\tServicios\tEquipos\tMontos cobrado")
                    print(f"{elemento[0]}\t{elemento[1][1]}\t{elemento[1][2]}\t{elemento[1][3]}\t{elemento[1][4]}\t{elemento[1][5]}")
                    break
# Funcion para crear un menu principal por el cual se entra a otras funciones
def Menu():
    while True:
        print("\n---------Menu---------")
        print("[1] Registrar un servicio")
        print("[2] Mostrar todos los servicios")
        print("[3] Consultar un servicio mediante el folio")
        print("[4] Consultar servicios en fecha especifica")
        print("[5] Salir del programa")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            RegistrarUnServicio()
        if opcion == "2":
            DesplegarTodosLosDatos()
        if opcion == "3":
            BuscarFolio()
        if opcion == "4":
            ConsultarPorFechas()
        if opcion == "5":
            print("¡Hasta la proxima!")
            break
# Funcion activa para entrar directamente al menu al empezar a ejecutar el programa
Menu()