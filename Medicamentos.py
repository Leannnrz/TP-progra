# Matriz de medicamentos
matriz_medicamentos = [
    ["M001", "Paracetamol", 1500, 20, 2],
    ["M002", "Ibuprofeno", 2200, 15, 2],
    ["M003", "Amoxicilina", 3500, 6, 1],
    ["M004", "Loratadina", 1800, 10, 2],
    ["M005", "Omeprazol", 2700, 25, 2],
    ["M006", "Diclofenac", 2500, 5, 1],
    ["M007", "Metformina", 4200, 12, 1],
    ["M008", "Salbutamol", 3900, 3, 1],
    ["M009", "Enalapril", 3100, 18, 1],
    ["M010", "Azitromicina", 4800, 7, 1]
]


'''
FUNCIONES CRUD DE MEDICAMENTOS
'''
# Para agregar un medicamento
def alta_medicamento():

    print("\n--- AGREGAR MEDICAMENTO ---\n")
    codigo = input("Ingrese el código del medicamento: ")

    while codigo in id_medicamento:
        print("Error: el medicamento ya existe.")
        codigo = input("Ingrese otro código: ")

    nombre = input("Ingrese el nombre: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese el stock: "))
    receta = int(input("Requiere receta (1- Si / 2- No): "))

    id_medicamento.append(codigo)
    nombre_medicamento.append(nombre)
    precio_medicamento.append(precio)
    stock_medicamento.append(stock)
    requiere_receta.append(receta)

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
    matriz_medicamentos[posicion][4] = int(input("Requiere receta? (1-Si / 2-No): "))

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
    
    print("\n--- LISTADO DE MEDICAMENTOS ORDENADOS POR PRECIO ---\n")

    for i in range(len(id_medicamento)):

        print("Código:", id_medicamento[i])
        print("Nombre:", nombre_medicamento[i])
        print("Precio:", precio_medicamento[i])
        print("Stock:", stock_medicamento[i])
        
        if requiere_receta[i] == 1:
            print("Requiere receta: Si.")
        else:
            print("Requiere receta: No\n")

        print("--------------------")

