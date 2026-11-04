<<<<<<< HEAD
from colorama import Fore, Style

# Matriz de clientes
matriz_clientes = [
    ["C001", "Juan Perez", 25, 1],
    ["C002", "Maria Gomez", 42, 2],
    ["C003", "Carlos Lopez", 31, 1],
    ["C004", "Ana Martinez", 55, 2],
    ["C005", "Luis Fernandez", 19, 1],
    ["C006", "Sofia Torres", 38, 2],
    ["C007", "Diego Ramirez", 47, 1],
    ["C008", "Valentina Castro", 29, 2],
    ["C009", "Martin Rojas", 61, 2],
    ["C010", "Lucia Diaz", 34, 2]
]
=======
import json
from colorama import Fore, Style
from CRUD import validaciones
from FUNCIONES import excepciones, recursividad

archivo_clientes = "clientes.json"
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

encabezados =  ['ID', 'Nombre', 'Edad', 'Cobertura']
lista_clientes = [dict(zip(encabezados, fila)) for fila in matriz_clientes]


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

     matriz = recursividad.crear_matriz_clientes_recursivo(lista_clientes)

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

<<<<<<< HEAD
    print(f"{Fore.MAGENTA}{' Agregar Cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")

    cantidad = 0  # No existe el código, si existe se convierte en 1

    for cliente in lista_clientes:  # Recorremos la fila
        if cliente["ID"] == codigo:     # El primer elemento de la fila es el código
            cantidad = cantidad + 1

    while cantidad > 0:
        print(f"{Fore.RED}Error: el cliente ya existe.")
        codigo = input("Ingrese otro código: ")
=======
    lista_clientes = diccionario_clientes()
    if lista_clientes is None:
         return

    print(f"{Fore.MAGENTA}{' Agregar Cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")

    while validaciones.validar_codigo_cliente(codigo) == False:
         print("Error: el codigo debe tener el formato C001.")
         codigo = input("Ingrese el código del cliente: ")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    while True:
        cantidad = 0

        for cliente in lista_clientes:
            if cliente["ID"] == codigo:
<<<<<<< HEAD
                cantidad = cantidad + 1

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
        
    while edad <= 0:
        print(f"{Fore.RED}Error: la edad debe ser mayor a 0.")
        edad = int(input("Ingrese la edad: "))
        
    cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): "))
        
    while cobertura != 1 and cobertura != 2:
        print ("Tipo de cobertura inválida: Ingrese una de las opciones.")
        cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): \n"))
=======
               cantidad = cantidad + 1

        if cantidad == 0:
            break
         
        print(f"{Fore.RED}Error: el cliente ya existe.")
        codigo = input("Ingrese el código del cliente: ")

        while validaciones.validar_codigo_cliente(codigo) == False:
            print("Error: el codigo debe tener el formato C001.")
            codigo = input("Ingrese el código del cliente: ")

    nombre = excepciones.ingresar_texto("Ingrese el nombre: ")
    edad = excepciones.ingresar_entero_positivo("Ingrese la edad: ")
    cobertura = excepciones.ingresar_opcion("Tipo de cobertura (1-Particular / 2-Obra Social): ",[1, 2])
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    nuevo_cliente = {
        "ID": codigo,
        "Nombre": nombre,
        "Edad": edad,
        "Cobertura": cobertura
    }

    lista_clientes.append(nuevo_cliente)

<<<<<<< HEAD
    print(f"{Fore.GREEN}Cliente agregado correctamente.\n")
=======
    if guardar_clientes(lista_clientes):
        print(f"{Fore.GREEN}Cliente agregado correctamente.\n")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3


# PARA MODIFICAR UN CLIENTE
def modificar_cliente():
    
    lista_clientes = diccionario_clientes()

<<<<<<< HEAD
    print(f"{Fore.MAGENTA}{' Modificar cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")
    posicion = -1

    for i in range(len(lista_clientes)):    # Busca la posición del cliente
        if lista_clientes[i]["ID"] == codigo:
            posicion = i
=======
    if lista_clientes is None:
        return

    print(f"{Fore.MAGENTA}{' Modificar cliente '.center(30, '=')}")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    codigo = excepciones.ingresar_codigo("Ingrese el código del cliente: ",validaciones.validar_codigo_cliente,"C001")

    cliente = recursividad.buscar_cliente_recursivo(lista_clientes, codigo)

    if cliente is None:
        print("Cliente no encontrado.")
        return

<<<<<<< HEAD
    lista_clientes[posicion]["Nombre"] = input("Nuevo nombre: ")
    lista_clientes[posicion]["Edad"] = int(input("Nueva edad: "))

    while lista_clientes[posicion]["Edad"] <= 0:
        print("Error: la edad debe ser mayor a 0.")
        lista_clientes[posicion]["Edad"] = int(input("Ingrese una nueva edad: "))

    lista_clientes[posicion]["Cobertura"] = int(input("Nueva cobertura (1-Particular / 2-Obra Social): "))

    while lista_clientes[posicion]["Cobertura"] != 1 and lista_clientes[posicion]["Cobertura"] != 2:
        print("Tipo de cobertura inválida: Ingrese una de las opciones.")
        lista_clientes[posicion]["Cobertura"] = int(input("Nueva cobertura (1-Particular / 2-Obra Social): "))

    print("Cliente modificado correctamente.")
=======
    nombre = excepciones.ingresar_texto("Nuevo nombre: ")

    edad = excepciones.ingresar_entero_positivo("Nueva edad: ")

    cobertura = excepciones.ingresar_opcion("Nueva cobertura (1-Particular / 2-Obra Social): ",[1, 2])

    cliente["Nombre"] = nombre
    cliente["Edad"] = edad
    cliente["Cobertura"] = cobertura

    if guardar_clientes(lista_clientes):
        print(f"{Fore.GREEN}Cliente modificado correctamente.\n")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3


# PARA ELIMINAR UN CLIENTE
def eliminar_cliente():

<<<<<<< HEAD
    print(f"{Fore.MAGENTA}{' Eliminar cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")
    posicion = -1

    for i in range(len(lista_clientes)):
        if lista_clientes[i]["ID"] == codigo:
            posicion = i
=======
    lista_clientes = diccionario_clientes()

    if lista_clientes is None:
        return
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    print(f"{Fore.MAGENTA}{' Eliminar cliente '.center(30, '=')}")

    codigo = excepciones.ingresar_codigo("Ingrese el código del cliente: ",validaciones.validar_codigo_cliente,"C001")

    cliente = recursividad.buscar_cliente_recursivo(lista_clientes, codigo)

    if cliente is None:
        print("Cliente no encontrado.")
        return
<<<<<<< HEAD
    
    lista_clientes.pop(posicion)
    print("Cliente eliminado correctamente.")
=======

    lista_clientes.remove(cliente)

    if guardar_clientes(lista_clientes):
        print(f"{Fore.GREEN}Cliente eliminado correctamente.\n")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3


# PARA MOSTRAR LISTA DE CLIENTES
def mostrar_clientes():
<<<<<<< HEAD
=======
    dic_clientes = diccionario_clientes()
    if dic_clientes is None:
        return
    
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
    ancho_total = 70
    print()
    print(f"{Fore.MAGENTA}{' LISTADO DE CLIENTES '.center(70, '=')}")
    print(f'{"Código":<12}{"Nombre":<28}{"Edad":<10}{"Cobertura":>20}')
    print("-" * ancho_total)

    # Ordena la lista por el largo del nombre antes de mostrarla
<<<<<<< HEAD
    lista_clientes.sort(key=lambda cliente: len(cliente["Nombre"]))

    for cliente in lista_clientes:
=======
    dic_clientes.sort(key=lambda cliente: len(cliente["Nombre"]))

    for cliente in dic_clientes:
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
        if cliente["Cobertura"] == 1:
            cobertura = "Particular"
        else:
            cobertura = "Obra Social"

<<<<<<< HEAD
        print(f'{cliente["ID"]:<12}{cliente["Nombre"]:<28}{cliente["Edad"]:<10}{cobertura:>20}\n')
=======
        print(f'{cliente["ID"]:<12}{cliente["Nombre"]:<28}{cliente["Edad"]:<10}{cobertura:>20}\n')
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
