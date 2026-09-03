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

'''
FUNCIONES CRUD DE CLIENTES
'''
# Para agregar un cliente
def alta_cliente():

    print("\n--- AGREGAR CLIENTE ---")
    codigo = input("Ingrese el código del cliente: ")

    cantidad = 0  # No existe el código, si existe se convierte en 1

    for fila in matriz_clientes:  # Recorremos la fila
        if fila[0] == codigo:     # El primer elemento de la fila es el código
            cantidad = cantidad + 1

    while cantidad > 0:
        print("Error: el cliente ya existe.")
        codigo = input("Ingrese otro código: ")

        cantidad = 0

        for fila in matriz_clientes:
            if fila[0] == codigo:
                cantidad = cantidad + 1

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
        
    while edad <= 0:
        print("Error: la edad debe ser mayor a 0.")
        edad = int(input("Ingrese la edad: "))
        
    cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): "))
        
    while cobertura != 1 and cobertura != 2:
        print ("Tipo de cobertura inválida: Ingrese una de las opciones.")
        cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): \n"))
        
    matriz_clientes.append([codigo, nombre, edad, cobertura])
    print("Cliente agregado correctamente.")


# Para modificar un cliente
def modificar_cliente():

    print("\n--- MODIFICAR CLIENTE ---")
    codigo = input("Ingrese el código del cliente: ")
    posicion = -1

    for i in range(len(matriz_clientes)):    # Busca la posición del cliente
        if matriz_clientes[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Cliente no encontrado.")
        return

    matriz_clientes[posicion][1] = input("Nuevo nombre: ")
    matriz_clientes[posicion][2] = int(input("Nueva edad: "))

    while matriz_clientes[posicion][2] <= 0:
        print("Error: la edad debe ser mayor a 0.")
        matriz_clientes[posicion][2] = int(input("Ingrese una nueva edad: "))

    matriz_clientes[posicion][3] = int(input("Nueva cobertura (1-Particular / 2-Obra Social): "))

    while matriz_clientes[posicion][3] != 1 and matriz_clientes[posicion][3] != 2:
        print("Tipo de cobertura inválida: Ingrese una de las opciones.")
        matriz_clientes[posicion][3] = int(input("Nueva cobertura (1-Particular / 2-Obra Social): "))

    print("Cliente modificado correctamente.")
    


# Para eliminar un cliente
def eliminar_cliente():

    print("\n--- ELIMINAR CLIENTE ---")
    codigo = input("Ingrese el código del cliente: ")
    posicion = -1

    for i in range(len(matriz_clientes)):
        if matriz_clientes[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Cliente no encontrado.")
        return
    '''
    for i in range(len(id_cliente_venta)):  # Verifica que el cliente no tenga ventas
        if id_cliente_venta[i] == codigo:
            print("No se puede eliminar, el cliente tiene ventas registradas.")
            return'''

    
    matriz_clientes.pop(posicion)
    print("Cliente eliminado correctamente.")
    


# Para mostrar lista clientes
def mostrar_clientes():
    ordenamiento_seleccion_clientes()

    print("\n--- LISTADO DE CLIENTES ORDENADOS POR EDAD ---\n")

    for i in range(len(id_cliente)):

        print("Código:", id_cliente[i])
        print("Nombre:", nombre_cliente[i])
        print("Edad:", edad_cliente[i])
        
        if tipo_cobertura[i] == 1:
            print("Cobertura: Particular")
        else:
            print("Cobertura: Obra Social\n")

        print("----------------------")