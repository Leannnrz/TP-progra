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

encabezados =  ['ID', 'Nombre', 'Edad', 'Cobertura']
lista_clientes = [dict(zip(encabezados, fila)) for fila in matriz_clientes]


'''
FUNCIONES CRUD DE CLIENTES
'''
# Para agregar un cliente
def alta_cliente():

    print(f"{Fore.MAGENTA}{' Agregar Cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")

    cantidad = 0  # No existe el código, si existe se convierte en 1

    for cliente in lista_clientes:  # Recorremos la fila
        if cliente["ID"] == codigo:     # El primer elemento de la fila es el código
            cantidad = cantidad + 1

    while cantidad > 0:
        print(f"{Fore.RED}Error: el cliente ya existe.")
        codigo = input("Ingrese otro código: ")

        cantidad = 0

        for cliente in lista_clientes:
            if cliente["ID"] == codigo:
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

    nuevo_cliente = {
        "ID": codigo,
        "Nombre": nombre,
        "Edad": edad,
        "Cobertura": cobertura
    }

    lista_clientes.append(nuevo_cliente)

    print(f"{Fore.GREEN}Cliente agregado correctamente.\n")


# Para modificar un cliente
def modificar_cliente():

    print(f"{Fore.MAGENTA}{' Modificar cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")
    posicion = -1

    for i in range(len(lista_clientes)):    # Busca la posición del cliente
        if lista_clientes[i]["ID"] == codigo:
            posicion = i

    if posicion == -1:
        print("Cliente no encontrado.")
        return

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


# Para eliminar un cliente
def eliminar_cliente():

    print(f"{Fore.MAGENTA}{' Eliminar cliente '.center(30, '=')}")
    codigo = input("Ingrese el código del cliente: ")
    posicion = -1

    for i in range(len(lista_clientes)):
        if lista_clientes[i]["ID"] == codigo:
            posicion = i

    if posicion == -1:
        print("Cliente no encontrado.")
        return
    
    lista_clientes.pop(posicion)
    print("Cliente eliminado correctamente.")


# Para mostrar lista clientes
def mostrar_clientes():
    ancho_total = 70
    print()
    print(f"{Fore.MAGENTA}{' LISTADO DE CLIENTES '.center(70, '=')}")
    print(f'{"Código":<12}{"Nombre":<28}{"Edad":<10}{"Cobertura":>20}')
    print("-" * ancho_total)

    # Ordena la lista por el largo del nombre antes de mostrarla
    lista_clientes.sort(key=lambda cliente: len(cliente["Nombre"]))

    for cliente in lista_clientes:
        if cliente["Cobertura"] == 1:
            cobertura = "Particular"
        else:
            cobertura = "Obra Social"

        print(f'{cliente["ID"]:<12}{cliente["Nombre"]:<28}{cliente["Edad"]:<10}{cobertura:>20}')
