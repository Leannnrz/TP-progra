from clientes import matriz_clientes
from medicamentos import matriz_medicamentos


# Listas de ventas
id_venta = [
    "V001", "V002", "V003", "V004", "V005",
    "V006", "V007", "V008", "V009", "V010"
]

id_cliente_venta = [
    "C001", "C003", "C002", "C001", "C005",
    "C007", "C003", "C008", "C010", "C005"
]

id_medicamento_venta = [
    "M001", "M003", "M002", "M005", "M007",
    "M004", "M003", "M010", "M009", "M001"
]

cantidad_ventas = [2, 1, 3, 1, 2, 1, 1, 2, 1, 4]

presento_receta = [2, 1, 2, 2, 1, 2, 1, 1, 1, 2]


# ALTA DE VENTA

def alta_venta():

    print("\n--- AGREGAR VENTA ---")

    codigo = input("Ingrese código de venta: ")

    while codigo in id_venta:
        print("Error: La venta ya existe.")
        codigo = input("Ingrese otro código: ")

    # Buscar cliente

    cliente = input("Ingrese el código del cliente: ")

    cliente_existe = False

    for fila in matriz_clientes:
        if fila[0] == cliente:
            cliente_existe = True

    while not cliente_existe:

        print("Error: Cliente inexistente.")
        cliente = input("Ingrese el código del cliente: ")

        cliente_existe = False

        for fila in matriz_clientes:
            if fila[0] == cliente:
                cliente_existe = True

    # Buscar medicamento

    medicamento = input("Ingrese el código del medicamento: ")

    medicamento_existe = False
    requiere_receta = 0

    for fila in matriz_medicamentos:
        if fila[0] == medicamento:
            medicamento_existe = True
            requiere_receta = fila[5]

    while not medicamento_existe:

        print("Error: Medicamento inexistente.")
        medicamento = input("Ingrese el código del medicamento: ")

        medicamento_existe = False

        for fila in matriz_medicamentos:
            if fila[0] == medicamento:
                medicamento_existe = True
                requiere_receta = fila[5]

    # Cantidad

    cantidad = int(input("Ingrese la cantidad vendida: "))

    while cantidad <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        cantidad = int(input("Ingrese la cantidad vendida: "))

    # Receta

    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    while receta != 1 and receta != 2:
        print("Error: opción inválida.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    # Verificar receta

    if requiere_receta == 1 and receta == 2:

        print("Error: Este medicamento requiere receta.")
        return

    # Registrar venta

    id_venta.append(codigo)
    id_cliente_venta.append(cliente)
    id_medicamento_venta.append(medicamento)
    cantidad_ventas.append(cantidad)
    presento_receta.append(receta)

    print("Venta agregada correctamente.")


# MODIFICAR VENTA

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

    # Cliente

    cliente = input("Nuevo código de cliente: ")

    cliente_existe = False

    for fila in matriz_clientes:
        if fila[0] == cliente:
            cliente_existe = True

    while not cliente_existe:

        print("Error: Cliente inexistente.")
        cliente = input("Nuevo código de cliente: ")

        cliente_existe = False

        for fila in matriz_clientes:
            if fila[0] == cliente:
                cliente_existe = True

    # Medicamento

    medicamento = input("Nuevo código de medicamento: ")

    medicamento_existe = False
    requiere_receta = 0

    for fila in matriz_medicamentos:
        if fila[0] == medicamento:
            medicamento_existe = True
            requiere_receta = fila[5]

    while not medicamento_existe:

        print("Error: Medicamento inexistente.")
        medicamento = input("Nuevo código de medicamento: ")

        medicamento_existe = False

        for fila in matriz_medicamentos:
            if fila[0] == medicamento:
                medicamento_existe = True
                requiere_receta = fila[5]

    # Receta

    receta = int(
        input("¿Presentó receta? (1-Si / 2-No): ")
    )

    while receta != 1 and receta != 2:

        print("Error: Ingrese una de las opciones.")

        receta = int(
            input("¿Presentó receta? (1-Si / 2-No): ")
        )

    # Cantidad

    cantidad = int(
        input("Ingrese nueva cantidad vendida: ")
    )

    while cantidad <= 0:

        print("Error: la cantidad debe ser mayor a 0.")

        cantidad = int(
            input("Ingrese nueva cantidad vendida: ")
        )

    # Verificar receta

    if requiere_receta == 1 and receta == 2:

        print("Error: Este medicamento requiere receta.")
        return

    # Modificar

    id_cliente_venta[posicion] = cliente
    id_medicamento_venta[posicion] = medicamento
    cantidad_ventas[posicion] = cantidad
    presento_receta[posicion] = receta

    print("Venta modificada correctamente.")


# ELIMINAR VENTA

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


# MOSTRAR VENTAS

def mostrar_ventas():

    print("\n--- LISTADO DE VENTAS ---")

    for i in range(len(id_venta)):

        print("Código venta:", id_venta[i])
        print("Código cliente:", id_cliente_venta[i])
        print("Código medicamento:", id_medicamento_venta[i])
        print("Cantidad de ventas:", cantidad_ventas[i])

        if presento_receta[i] == 1:
            print("Presentó receta: Si")
        else:
            print("Presentó receta: No")

        print("----------------------")