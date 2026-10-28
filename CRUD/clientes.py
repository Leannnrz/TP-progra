import json
from colorama import Fore, Style
from CRUD import validaciones

archivo_clientes = "clientes.json"

'''
FUNCIONES CRUD DE CLIENTES
'''


def diccionario_clientes():
    try:
        with open(archivo_clientes, "r", encoding = "UTF-8") as archivo:
                lista_clientes = json.load(archivo)

        if type(lista_clientes) != list:
            print("Error: el archivo JSON debe contener una lista de clientes")
            return None

        for cliente in lista_clientes:
            if type(cliente) != dict:
                print("Error: cada cliente debe ser un diccionario")
                return None
            
            if "ID" not in cliente or "Nombre" not in cliente or "Edad" not in cliente or "Cobertura" not in cliente:
                print("Error: cada cliente debe tener las claves 'ID', 'Nombre', 'Edad' y 'Cobertura'")
                return None

        return lista_clientes

    except FileNotFoundError:
            print("Error: no se encontro el archivo JSON")
            return None
    except json.JSONDecodeError:
            print("Error: el archivo JSON no tiene datos validos")
            return None
    except (OSError, UnicodeDecodeError) as error:
            print(f"Error: no se pudo leer el archivo JSON: {error}")
            return None

def matriz_clientes():
     lista_clientes = diccionario_clientes()

     if lista_clientes is None:
            return None

     matriz = []

     for cliente in lista_clientes:
          fila = [
               cliente["ID"],
               cliente["Nombre"],
               cliente["Edad"],
               cliente["Cobertura"]
          ]
          matriz.append(fila)
     return matriz

def guardar_clientes(lista_clientes):
    try:
        with open(archivo_clientes, "w", encoding = "UTF-8") as archivo:
             json.dump(lista_clientes, archivo, indent=4, ensure_ascii=False)
        return True
    
    except(OSError, TypeError, ValueError) as error:
         print(f"Error: no se pudo guardar el archivo JSON: {error}")
         return False

# PARA AGREGAR UN CLIENTE
def alta_cliente():

    lista_clientes = diccionario_clientes()
    if lista_clientes is None:
         return

    print(f"{Fore.MAGENTA}{' Agregar Cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")

    while validaciones.validar_codigo_cliente(codigo) == False:
         print("Error: el codigo debe tener el formato C001.")
         codigo = input("Ingrese el código del cliente: ")

    while True:
         cantidad = 0

         for cliente in lista_clientes:
              if cliente["ID"] == codigo:
                   cantidad = cantidad + 1

         if cantidad == 0:
                break

         print(f"{Fore.RED}Error: el cliente ya existe.")
         codigo = input("Ingrese el código del cliente: ")

         while validaciones.validar_codigo_cliente(codigo) == False:
              print("Error: el codigo debe tener el formato C001.")
              codigo = input("Ingrese el código del cliente: ")

    nombre = input("Ingrese el nombre: ")
    
    while nombre == "":
         print("Error: el nombre no puede estar vacío.")
         nombre = input("Ingrese el nombre: ")

    try:
         edad = int(input("Ingrese la edad: "))

         while edad <= 0:
                print(f"{Fore.RED}Error: la edad debe ser mayor a 0.")
                edad = int(input("Ingrese la edad: "))

         cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): "))

         while cobertura != 1 and cobertura != 2:
                print ("Tipo de cobertura inválida: Ingrese una de las opciones.")
                cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): \n"))
    
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    nuevo_cliente = {
        "ID": codigo,
        "Nombre": nombre,
        "Edad": edad,
        "Cobertura": cobertura
    }

    lista_clientes.append(nuevo_cliente)

    if guardar_clientes(lista_clientes):
        print(f"{Fore.GREEN}Cliente agregado correctamente.\n")

# PARA MODIFICAR UN CLIENTE
def modificar_cliente():
    lista_clientes = diccionario_clientes()
    if lista_clientes is None:
        return
    
    print(f"{Fore.MAGENTA}{' Modificar cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")

    for cliente in lista_clientes:
         if cliente["ID"] == codigo:
              nombre = input("Nuevo nombre: ")
              edad = (input("Nueva edad: "))
              cobertura = (input("Nueva cobertura (1-Particular / 2-Obra Social): "))
              
              if nombre:
                  cliente["Nombre"] = nombre
              
              try:
                    if edad:
                        nueva_edad = int(edad)
                        if nueva_edad <= 0:
                             print("Error: la edad debe ser mayor a 0.")
                             return
                        cliente["Edad"] = nueva_edad

                    if cobertura:
                        nueva_cobertura = int(cobertura)
                        if nueva_cobertura != 1 and nueva_cobertura != 2:
                             print("Tipo de cobertura inválida: Ingrese una de las opciones.")
                             return
                        cliente["Cobertura"] = nueva_cobertura
              except ValueError:
                   print("Error: la edad y la cobertura deben ser validos.")
                   return

              if guardar_clientes(lista_clientes):
                   print(f"{Fore.GREEN}Cliente modificado correctamente.\n")
              return

    print("Cliente no encontrado.")

# PARA ELIMINAR UN CLIENTE
def eliminar_cliente():

    lista_clientes = diccionario_clientes()
    if lista_clientes is None:
        return
    
    print(f"{Fore.MAGENTA}{' Eliminar cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")

    for cliente in lista_clientes:
         if cliente["ID"] == codigo:
              lista_clientes.remove(cliente)
              if guardar_clientes(lista_clientes):
                   print(f"{Fore.GREEN}Cliente eliminado correctamente.\n")
              return

    print("Cliente no encontrado.")

# PARA MOSTRAR LISTA DE CLIENTES
def mostrar_clientes():
    dic_clientes = diccionario_clientes()
    if dic_clientes is None:
        return
    
    ancho_total = 70
    print()
    print(f"{Fore.MAGENTA}{' LISTADO DE CLIENTES '.center(70, '=')}")
    print(f'{"Código":<12}{"Nombre":<28}{"Edad":<10}{"Cobertura":>20}')
    print("-" * ancho_total)

    # Ordena la lista por el largo del nombre antes de mostrarla
    dic_clientes.sort(key=lambda cliente: len(cliente["Nombre"]))

    for cliente in dic_clientes:
        if cliente["Cobertura"] == 1:
            cobertura = "Particular"
        else:
            cobertura = "Obra Social"

        print(f'{cliente["ID"]:<12}{cliente["Nombre"]:<28}{cliente["Edad"]:<10}{cobertura:>20}\n')