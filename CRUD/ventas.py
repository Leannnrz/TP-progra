from clientes import matriz_clientes
from medicamentos import matriz_medicamentos



# MATRIZ DE VENTAS

matriz_ventas = [
    ["V001", "C001", "M001", 2, 2],
    ["V002", "C003", "M003", 1, 1],
    ["V003", "C002", "M002", 3, 2],
    ["V004", "C001", "M005", 1, 2],
    ["V005", "C005", "M007", 2, 1],
    ["V006", "C007", "M004", 1, 2],
    ["V007", "C003", "M003", 1, 1],
    ["V008", "C008", "M010", 2, 1],
    ["V009", "C010", "M009", 1, 1],
    ["V010", "C005", "M001", 4, 2]
]


# ALTA DE VENTA

def alta_venta():

    print("\n--- AGREGAR VENTA ---")

    # Código de venta
    codigo = input("Ingrese código de venta: ")

    codigo_existe = True

    while codigo_existe:

        codigo_existe = False

        for fila in matriz_ventas:
            if fila[0] == codigo:
                codigo_existe = True

        if codigo_existe:

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
    cantidad = int(
        input("Ingrese la cantidad vendida: ")
    )

    while cantidad <= 0:

        print("Error: la cantidad debe ser mayor a 0.")

        cantidad = int(
            input("Ingrese la cantidad vendida: ")
        )

    # Receta
    receta = int(
        input("¿Presentó receta? (1-Si / 2-No): ")
    )

    while receta != 1 and receta != 2:

        print("Error: opción inválida.")

        receta = int(
            input("¿Presentó receta? (1-Si / 2-No): ")
        )

    # Verificar si el medicamento requiere receta
    if requiere_receta == 1 and receta == 2:

        print("Error: Este medicamento requiere receta.")
        return

    # Registrar venta
    matriz_ventas.append(
        [codigo, cliente, medicamento, cantidad, receta]
    )

    print("Venta agregada correctamente.")


# MODIFICAR VENTA

def modificar_venta():

    print("\n--- MODIFICAR VENTA ---")

    codigo = input("Ingrese código de venta: ")

    posicion = -1

    # Buscar venta
    for i in range(len(matriz_ventas)):

        if matriz_ventas[i][0] == codigo:
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

    # Cantidad
    cantidad = int(
        input("Ingrese nueva cantidad vendida: ")
    )

    while cantidad <= 0:

        print("Error: la cantidad debe ser mayor a 0.")

        cantidad = int(
            input("Ingrese nueva cantidad vendida: ")
        )

    # Receta
    receta = int(
        input("¿Presentó receta? (1-Si / 2-No): ")
    )

    while receta != 1 and receta != 2:

        print("Error: opción inválida.")

        receta = int(
            input("¿Presentó receta? (1-Si / 2-No): ")
        )

    # Verificar receta
    if requiere_receta == 1 and receta == 2:

        print("Error: Este medicamento requiere receta.")
        return

    # Modificar los datos de la venta
    matriz_ventas[posicion][1] = cliente
    matriz_ventas[posicion][2] = medicamento
    matriz_ventas[posicion][3] = cantidad
    matriz_ventas[posicion][4] = receta

    print("Venta modificada correctamente.")


# ELIMINAR VENTA

def eliminar_venta():

    print("\n--- ELIMINAR VENTA ---")

    codigo = input("Ingrese código de la venta: ")

    posicion = -1

    # Buscar venta
    for i in range(len(matriz_ventas)):

        if matriz_ventas[i][0] == codigo:
            posicion = i

    if posicion == -1:

        print("Venta no encontrada.")
        return

    matriz_ventas.pop(posicion)

    print("Venta eliminada correctamente.")


# MOSTRAR VENTAS

def mostrar_ventas():

    print("\n--- LISTADO DE VENTAS ---")

    for i in range(len(matriz_ventas)):

        print("Código venta:", matriz_ventas[i][0])
        print("Código cliente:", matriz_ventas[i][1])
        print("Código medicamento:", matriz_ventas[i][2])
        print("Cantidad de ventas:", matriz_ventas[i][3])

        if matriz_ventas[i][4] == 1:
            print("Presentó receta: Si")
        else:
            print("Presentó receta: No")

        print("----------------------")
