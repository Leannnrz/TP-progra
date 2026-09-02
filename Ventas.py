# Listas de ventas
id_venta = ["V001", "V002", "V003", "V004", "V005", "V006", "V007", "V008", "V009", "V010"]
id_cliente_venta = ["C001", "C003", "C002", "C001", "C005", "C007", "C003", "C008", "C010", "C005"]
id_medicamento_venta = ["M001", "M003", "M002", "M005", "M007", "M004", "M003", "M010", "M009", "M001"]
cantidad_ventas = [2, 1, 3, 1, 2, 1, 1, 2, 1, 4]
presento_receta = [2, 1, 2, 2, 1, 2, 1, 1, 1, 2]

'''
FUNCIÓN VENTAS (CRUD)
'''
# Para agregar una venta
def alta_venta():

    print("\n--- AGREGAR VENTA ---")
    codigo = input("Ingrese código de venta: ")

    while codigo in id_venta:
        print("Error: La venta ya existe.")
        codigo = input("Ingrese otro código: ")

    cliente = input("Ingrese el código del cliente: ")
    
    while cliente not in id_cliente:
        print("Error: Cliente inexistente.")
        cliente = input("Ingrese el código del cliente: ")
        
    medicamento = input("Ingrese el código del medicamento: ")
    
    while medicamento not in id_medicamento:
        print("Error: Medicamento inexistente.")
        medicamento = input("Ingrese el código del medicamento: ")

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

    for i in range(len(id_venta)):
        if id_venta[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    id_venta.pop(posicion)
    id_cliente_venta.pop(posicion)
    id_medicamento_venta.pop(posicion)
    cantidad_ventas.pop(posicion)
    presento_receta.pop(posicion)

    print("Venta eliminada correctamente.")



# Para mostrar lista de ventas
def mostrar_ventas():

    print("\n--- LISTADO DE VENTAS ORDENADAS POR CANTIDAD---")

    for i in range(len(id_cliente_venta)):

        print("Código venta:", id_venta[i])
        print("Código cliente:", id_cliente_venta[i])
        print("Código medicamento:", id_medicamento_venta[i])
        print("Cantidad de ventas:", cantidad_ventas[i])
        
        if presento_receta[i] == 1:
            print("Presento receta: Si")
        else:
            print("Presento receta: No\n")

        print("----------------------")

