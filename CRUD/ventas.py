from clientes import matriz_clientes
from medicamentos import matriz_medicamentos
import re



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
#-------------------------
# Agregar una venta
#-------------------------
def alta_venta():

    print("\n--- AGREGAR VENTA ---")

    codigo = input("Ingrese código de venta: ")
    patron = "^V[0-9]{3}$"
    resultado = re.search(patron, codigo)
    valido = 0 # Suponiendo que el codigo no es correcto

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato V001.")
        codigo = input("Ingrese código de venta: ")

        resultado = re.search(patron, codigo)

        if resultado:
            valido = 1

    # Verifica que el código de venta no exista
    cantidad = 0

    for fila in matriz_ventas:
        if fila[0] == codigo:
            cantidad = cantidad + 1

    while cantidad > 0:
        print("Error: la venta ya existe.")
        codigo = input("Ingrese otro código de venta: ")

        # Verifica nuevamente el formato
        resultado = re.search(patron, codigo)

        if resultado:
            cantidad = 0

            for fila in matriz_ventas:
                if fila[0] == codigo:
                    cantidad = cantidad + 1

        else:
            print("Error: el código debe tener el formato V001.")


    # Código de cliente
    cliente = input("Ingrese código de cliente: ")
    patron = "^C[0-9]{3}$"
    resultado = re.search(patron, cliente)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato C001.")
        cliente = input("Ingrese código de cliente: ")

        resultado = re.search(patron, cliente)

        if resultado:
            valido = 1

    # Verifica que el cliente exista
    cantidad = 0

    for fila in matriz_clientes:
        if fila[0] == cliente:
            cantidad = cantidad + 1

    if cantidad == 0:
        print("Error: Cliente inexistente.")
        return

    # Código de medicamento
    medicamento = input("Ingrese el código del medicamento: ")
    patron = "^M[0-9]{3}$"
    resultado = re.search(patron, medicamento)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato M001.")
        medicamento = input("Ingrese el código del medicamento: ")

        resultado = re.search(patron, medicamento)
        if resultado:
            valido = 1

    # Verifica que el medicamento exista
    cantidad = 0
    requiere_receta = 0

    for fila in matriz_medicamentos:
        if fila[0] == medicamento:
            cantidad = cantidad + 1
            requiere_receta = fila[5]

    if cantidad == 0:
        print("Error: Medicamento inexistente.")
        return

    # Cantidad de ventas
    ventas = int(input("Ingrese la cantidad de ventas: "))

    while ventas <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        ventas = int(input("Ingrese la cantidad de ventas: "))

    # Verifica receta
    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))
    while receta != 1 and receta != 2:
        print("Opción inválida: Ingrese una de las opciones.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    # Verificar si el medicamento requiere receta
    if requiere_receta == 1 and receta == 2:
        print("Error: Este medicamento requiere receta.")
        return

    matriz_ventas.append([codigo, cliente, medicamento, ventas, receta])
    print("Venta agregada correctamente.")



#-------------------------
# Modificar una venta
#-------------------------
def modificar_venta():

    print("\n--- MODIFICAR VENTA ---")

    # Código de venta
    codigo = input("Ingrese código de venta: ")
    patron = "^V[0-9]{3}$"
    resultado = re.search(patron, codigo)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato V001.")
        codigo = input("Ingrese código de venta: ")
        resultado = re.search(patron, codigo)

        if resultado:
            valido = 1

    posicion = -1

    for i in range(len(matriz_ventas)):
        if matriz_ventas[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    # Código de cliente
    cliente = input("Nuevo código de cliente: ")
    patron = "^C[0-9]{3}$"
    resultado = re.search(patron, cliente)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato C001.")
        cliente = input("Nuevo código de cliente: ")

        resultado = re.search(patron, cliente)

        if resultado:
            valido = 1

    # Verifica que el cliente exista
    cantidad = 0

    for fila in matriz_clientes:
        if fila[0] == cliente:
            cantidad = cantidad + 1

    if cantidad == 0:
        print("Error: Cliente inexistente.")
        return

    # Código de medicamento
    medicamento = input("Nuevo código de medicamento: ")
    patron = "^M[0-9]{3}$"
    resultado = re.search(patron, medicamento)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato M001.")
        medicamento = input("Nuevo código de medicamento: ")
        resultado = re.search(patron, medicamento)

        if resultado:
            valido = 1

    # Verifica que el medicamento exista
    cantidad = 0
    requiere_receta = 0

    for fila in matriz_medicamentos:
        if fila[0] == medicamento:
            cantidad = cantidad + 1
            requiere_receta = fila[5]

    if cantidad == 0:
        print("Error: Medicamento inexistente.")
        return

    # Nueva cantidad
    cantidad_venta = int(input("Ingrese nueva cantidad: "))

    while cantidad_venta <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        cantidad_venta = int(input("Ingrese nueva cantidad vendida: "))

    # Verificar receta
    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    while receta != 1 and receta != 2:
        print("Opción inválida: Ingrese una de las opciones.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    # Verificar si el medicamento requiere receta
    if requiere_receta == 1 and receta == 2:
        print("Error: Este medicamento requiere receta.")
        return

    matriz_ventas[posicion][1] = cliente
    matriz_ventas[posicion][2] = medicamento
    matriz_ventas[posicion][3] = cantidad_venta
    matriz_ventas[posicion][4] = receta
    print("Venta modificada correctamente.")



#-------------------------
# Eliminar una venta
#-------------------------
def eliminar_venta():

    print("\n--- ELIMINAR VENTA ---")

    codigo = input("Ingrese código de la venta: ")
    patron = "^V[0-9]{3}$"
    resultado = re.search(patron, codigo)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print("Error: el código debe tener el formato V001.")
        codigo = input("Ingrese código de la venta: ")

        resultado = re.search(patron, codigo)

        if resultado:
            valido = 1

    posicion = -1

    for i in range(len(matriz_ventas)):
        if matriz_ventas[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    matriz_ventas.pop(posicion)

    print("Venta eliminada correctamente.")


#-------------------------
# Mostrar lista de ventas
#-------------------------
def mostrar_ventas():

    print("\n--- LISTADO DE VENTAS ---")
    print(f'{"Código":<8}{"Cliente":<20}{"Medicamento":<20}{"Cantidad":>10}{"Receta":>8}')
    print("-" * 66)

    for venta in matriz_ventas:
        if venta[4] == 1:
            receta = "Si"
        else:
            receta = "No"
        
            print(f'{venta[0]:<8}{venta[1]:<20}{venta[2]:<20}{venta[3]:>10.2f}{receta[4]:>8}')
            

    print("----------------------")

