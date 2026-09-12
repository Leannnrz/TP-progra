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


# -----------------------------
# ALTA DE MEDICAMENTO
# -----------------------------

def alta_medicamento():

    print("\n--- AGREGAR MEDICAMENTO ---")

    codigo = input("Ingrese el código del medicamento: ")

    cantidad = 0

    for fila in matriz_medicamentos:
        if fila[0] == codigo:
            cantidad = cantidad + 1

    while cantidad > 0:

        print("Error: el medicamento ya existe.")
        codigo = input("Ingrese otro código: ")

        cantidad = 0

        for fila in matriz_medicamentos:
            if fila[0] == codigo:
                cantidad = cantidad + 1

    nombre = input("Ingrese el nombre: ")

    laboratorio = input("Ingrese el laboratorio: ")

    precio = int(input("Ingrese el precio: "))

    while precio <= 0:
        print("Error: el precio debe ser mayor a 0.")
        precio = int(input("Ingrese el precio: "))

    stock = int(input("Ingrese el stock: "))

    while stock < 0:
        print("Error: el stock no puede ser negativo.")
        stock = int(input("Ingrese el stock: "))

    receta = int(input("Requiere receta (1-Si / 2-No): "))

    while receta != 1 and receta != 2:
        print("Opción inválida.")
        receta = int(input("Requiere receta (1-Si / 2-No): "))

    matriz_medicamentos.append(
        [codigo, nombre, laboratorio, precio, stock, receta]
    )

    print("Medicamento agregado correctamente.")


# -----------------------------
# MODIFICAR MEDICAMENTO
# -----------------------------

def modificar_medicamento():

    print("\n--- MODIFICAR MEDICAMENTO ---")

    codigo = input("Ingrese código del medicamento: ")

    posicion = -1

    for i in range(len(matriz_medicamentos)):
        if matriz_medicamentos[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    matriz_medicamentos[posicion][1] = input(
        "Ingrese el nuevo nombre del medicamento: "
    )

    matriz_medicamentos[posicion][2] = input(
        "Ingrese el nuevo laboratorio: "
    )

    matriz_medicamentos[posicion][3] = int(
        input("Nuevo precio: ")
    )

    while matriz_medicamentos[posicion][3] <= 0:
        print("Error: el precio debe ser mayor a 0.")
        matriz_medicamentos[posicion][3] = int(
            input("Nuevo precio: ")
        )

    matriz_medicamentos[posicion][4] = int(
        input("Nuevo stock: ")
    )

    while matriz_medicamentos[posicion][4] < 0:
        print("Error: el stock no puede ser negativo.")
        matriz_medicamentos[posicion][4] = int(
            input("Nuevo stock: ")
        )

    matriz_medicamentos[posicion][5] = int(
        input("Requiere receta (1-Si / 2-No): ")
    )

    while matriz_medicamentos[posicion][5] != 1 and matriz_medicamentos[posicion][5] != 2:
        print("Opción inválida.")
        matriz_medicamentos[posicion][5] = int(
            input("Requiere receta (1-Si / 2-No): ")
        )

    print("Medicamento modificado correctamente.")


# -----------------------------
# ELIMINAR MEDICAMENTO
# -----------------------------

def eliminar_medicamento():

    print("\n--- ELIMINAR MEDICAMENTO ---")

    codigo = input("Ingrese código del medicamento: ")

    posicion = -1

    for i in range(len(matriz_medicamentos)):
        if matriz_medicamentos[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    matriz_medicamentos.pop(posicion)

    print("Medicamento eliminado correctamente.")


# -----------------------------
# MOSTRAR MEDICAMENTOS
# -----------------------------

def mostrar_medicamentos():

    print("\n---- LISTADO DE MEDICAMENTOS ----\n")

    print(
        f'{"Código":<8}'
        f'{"Nombre":<20}'
        f'{"Laboratorio":<20}'
        f'{"Precio":>10}'
        f'{"Stock":>8}'
        f'{"Receta":>10}'
    )

    print("-" * 80)

    for medicamento in matriz_medicamentos:

        if medicamento[5] == 1:
            receta = "Si"
        else:
            receta = "No"

        print(
            f'{medicamento[0]:<8}'
            f'{medicamento[1]:<20}'
            f'{medicamento[2]:<20}'
            f'{medicamento[3]:>10.2f}'
            f'{medicamento[4]:>8}'
            f'{receta:>10}'
        )