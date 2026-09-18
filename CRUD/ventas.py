#Matriz ventas
matriz_ventas = [
    ("V001", "C001", "M001", 2, 2),
    ("V002", "C003", "M003", 1, 1),
    ("V003", "C002", "M002", 3, 2),
    ("V004", "C001", "M005", 1, 2),
    ("V005", "C005", "M007", 2, 1),
    ("V006", "C007", "M004", 1, 2),
    ("V007", "C003", "M003", 1, 1),
    ("V008", "C008", "M010", 2, 1),
    ("V009", "C010", "M009", 1, 1),
    ("V010", "C005", "M001", 4, 2)
]



'''
FUNCIÓN VENTAS (CRUD)
'''
# Para agregar una venta
def alta_venta():

    print("\n--- AGREGAR VENTA ---")
    codigo = input("Ingrese código de venta: ")

    cantidad = 0  # No existe el código, si existe se convierte en 1
        
    for fila in matriz_ventas:  # Recorremos la fila
            if fila[0] == codigo:         # El primer elemento de la fila es el código
                cantidad = cantidad + 1

    while cantidad > 0:
            print("Error: la venta ya existe.")
            codigo = input("Ingrese otro código: ")
        
            cantidad = 0

            for fila in matriz_ventas:
                        if fila[0] == codigo:
                            cantidad = cantidad + 1



    ventas = int(input("Ingrese la cantidad de ventas: "))
    
    while ventas <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        ventas = int(input("Ingrese la cantidad de ventas: "))
        
    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))
    

    permitido = 1  # 1= la venta se puede realizar, 0= la venta no se permite

    for i in range(len(id_medicamento)):
        if id_medicamento[i] == medicamento:

            if requiere_receta[i] == 1 and receta == 2:  #Para revisar si la receta es obligatoria y no se presento
                print("Error: Este medicamento requiere receta.")
                permitido = 0

    if permitido == 1:
        id_venta.append(codigo)
        id_cliente_venta.append(cliente)
        id_medicamento_venta.append(medicamento)
        cantidad_ventas.append(ventas)
        presento_receta.append(receta)

        print("Venta agregada correctamente.")



# Para modificar una venta
def modificar_venta():

    print("\n--- MODIFICAR VENTA ---")
    codigo = input("Ingrese código de venta: ")
    posicion = -1

    for i in range(len(id_venta)):
        if id_venta[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    cliente = input("Nuevo código de cliente: ")

    while cliente not in id_cliente:
        print("Error: Cliente inexistente.")
        cliente = input("Nuevo código de cliente: ")

    medicamento = input("Nuevo código de medicamento: ")

    while medicamento not in id_medicamento:
        print("Error: Medicamento inexistente.")
        medicamento = input("Nuevo código de medicamento: ")

    receta = int(input("¿Presentó receta? (1-Si / 2-No)"))
    
    while receta != 1 and receta != 2:
        print("Error: Ingrese una de las opciones.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))
        
    cantidad = int(input("Ingrese nueva cantidad vendida: "))
    while cantidad <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
    
    permitido = 1
    
    for i in range(len(id_medicamento)):
        if id_medicamento[i] == medicamento:
            if requiere_receta[i] == 1 and receta == 2:
                print("Error: Este medicamento requiere receta.")
                permitido = 0

    if permitido == 0:
        return


    id_cliente_venta[posicion] = cliente
    id_medicamento_venta[posicion] = medicamento
    cantidad_ventas[posicion] = cantidad
    presento_receta[posicion] = receta

    print("Venta modificada correctamente.")



# Para eliminar una venta
def eliminar_venta():

    print("\n--- ELIMINAR VENTA ---")
    codigo = input("Ingrese código de la venta: ")
    posicion = -1

    for i in range(len(matriz_ventas)):
        if matriz_ventas[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    matriz_ventas.pop(posicion)
    print("Venta eliminada correctamente.")


# Para mostrar lista de ventas
def mostrar_ventas():

    print("\n--- LISTADO DE VENTAS ---")

    for venta in matriz_ventas:
        if venta[4] == 1:
            receta = "Si"
        else:
            receta = "No"
        
            print(f'{venta[0]:<8}{venta[1]:<20}{venta[2]:<20}{venta[3]:>10.2f}{venta[4]:>8}')
            

        print("----------------------")

