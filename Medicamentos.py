# Listas de medicamentos
id_medicamento = ["M001", "M002", "M003", "M004", "M005", "M006", "M007", "M008", "M009", "M010"]
nombre_medicamento = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Loratadina", "Omeprazol", "Diclofenac", "Metformina", "Salbutamol", "Enalapril", "Azitromicina"]
precio_medicamento = [1500, 2200, 3500, 1800, 2700, 2500, 4200, 3900, 3100, 4800]
stock_medicamento = [20, 15, 6, 10, 25, 5, 12, 3, 18, 7]
requiere_receta = [2, 2, 1, 2, 2, 1, 1, 1, 1, 1]

'''
FUNCIÓN MEDICAMENTOS (CRUD)
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

    for i in range(len(id_medicamento)): #busca la posicion del medicamento
        if id_medicamento[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    nombre_medicamento[posicion] = input("Nuevo medicamento: ")
    precio_medicamento[posicion] = int(input("Nuevo precio: "))
    stock_medicamento[posicion] = int(input("Nuevo stock: "))
    requiere_receta[posicion] = int(input("Requiere receta? (1-Si / 2-No): "))

    print("Medicamento modificado correctamente.")
    
    

# Para eliminar un medicamento
def eliminar_medicamento():

    print("\n--- ELIMINAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(id_medicamento)):
        if id_medicamento[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    for i in range(len(id_medicamento_venta)): # Verifica que el medicamento no este asociado a una venta.
        if id_medicamento_venta[i] == codigo:
            print("No se puede eliminar, el medicamento tiene ventas asociadas.")
            return

    id_medicamento.pop(posicion)
    nombre_medicamento.pop(posicion)
    precio_medicamento.pop(posicion)
    stock_medicamento.pop(posicion)
    requiere_receta.pop(posicion)

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

