# Matriz de medicamentos
matriz_medicamentos = [
    ["M001", "Paracetamol", "Genomma Lab", 1500, 20, 2],
    ["M002", "Ibuprofeno", "Bayer", 2200, 15, 2],
    ["M003", "Amoxicilina", "Roemmers", 3500, 6, 1],
    ["M004", "Loratadina", "Bagó", 1800, 10, 2],
    ["M005", "Omeprazol", "Gador", 2700, 25, 2],
    ["M006", "Diclofenac", "Elea", 2500, 5, 1],
    ["M007", "Metformina", "Montpellier", 4200, 12, 1],
    ["M008", "Salbutamol", "Cassará", 3900, 3, 1],
    ["M009", "Enalapril", "Bernabó", 3100, 18, 1],
    ["M010", "Azitromicina", "Pfizer", 4800, 7, 1]
]



'''
FUNCIONES CRUD DE MEDICAMENTOS
'''
# Para agregar un medicamento
def alta_medicamento():

    print("\n--- AGREGAR MEDICAMENTO ---\n")
    codigo = input("Ingrese el código del medicamento: ")

    cantidad = 0  # No existe el código, si existe se convierte en 1
    
    for fila in matriz_medicamentos:  # Recorremos la fila
        if fila[0] == codigo:         # El primer elemento de la fila es el código
            cantidad = cantidad + 1
    
    while cantidad > 0:
        print("Error: el cliente ya existe.")
        codigo = input("Ingrese otro código: ")
    
        cantidad = 0
    
        for fila in matriz_medicamentos:
            if fila[0] == codigo:
                cantidad = cantidad + 1

    '''while codigo in id_medicamento:
        print("Error: el medicamento ya existe.")
        codigo = input("Ingrese otro código: ")'''

    nombre = input("Ingrese el nombre: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese el stock: "))

    receta = int(input("Requiere receta (1- Si / 2- No): "))
    while receta != 1 and receta != 2:
        print ("Opción inválida: Ingrese una de las opciones.")
        receta = int(input("Requiere receta (1- Si / 2- No): "))

    matriz_medicamentos.append([codigo, nombre, precio, stock, receta])  
    print("Medicamento agregado correctamente.\n")


# Para modificar un medicamento
def modificar_medicamento():

    print("\n--- MODIFICAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(matriz_medicamentos)): #Busca la posicion del medicamento
        if matriz_medicamentos[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    matriz_medicamentos[posicion][1] = input("Ingrese el nuevo nombre del medicamento: ")
    matriz_medicamentos[posicion][2] = int(input("Nuevo precio: "))
    matriz_medicamentos[posicion][3] = int(input("Nuevo stock: "))
    matriz_medicamentos[posicion][4] = int(input("Requiere receta? (1-Si / 2-No): \n"))

    print("Medicamento modificado correctamente.")
    
    

# Para eliminar un medicamento
def eliminar_medicamento():

    print("\n--- ELIMINAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(matriz_medicamentos)):
        if matriz_medicamentos[i][0] == codigo:   # Busca el código en la columna 0
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return
    '''
    for i in range(len(id_medicamento_venta)): # Verifica que el medicamento no este asociado a una venta.
        if id_medicamento_venta[i] == codigo:
            print("No se puede eliminar, el medicamento tiene ventas asociadas.")
            return'''

    matriz_medicamentos.pop(posicion)
    print("Medicamento eliminado correctamente.")


# Para mostrar lista medicamentos
def mostrar_medicamentos():
    
    print("\n---- LISTADO DE MEDICAMENTOS ----\n")

    for i in range(len(matriz_medicamentos)):

        print("Código:", matriz_medicamentos[i][0])
        print("Nombre:", matriz_medicamentos[i][1])
        print("Precio:", matriz_medicamentos[i][2])
        print("Stock:", matriz_medicamentos[i][3])
        
        if matriz_medicamentos[i][4] == 1:
            print("Requiere receta: Si.")
        else:
            print("Requiere receta: No\n")

        print("--------------------")

