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
    ["V010", "C005", "M001", 4, 2],
    ["V011", "C002", "M006", 3, 1],
    ["V012", "C004", "M002", 5, 2],
    ["V013", "C006", "M008", 1, 1],
    ["V014", "C009", "M003", 2, 2],
    ["V015", "C001", "M010", 4, 1],
    ["V016", "C003", "M005", 2, 2],
    ["V017", "C007", "M007", 1, 1],
    ["V018", "C005", "M009", 3, 2],
    ["V019", "C008", "M004", 5, 1],
    ["V020", "C010", "M001", 2, 2],
    ["V021", "C004", "M007", 1, 2],
    ["V022", "C001", "M003", 4, 1],
    ["V023", "C006", "M009", 2, 2],
    ["V024", "C010", "M002", 5, 1],
    ["V025", "C002", "M005", 3, 2],
    ["V026", "C007", "M001", 1, 1],
    ["V027", "C003", "M008", 2, 2],
    ["V028", "C005", "M004", 4, 1],
    ["V029", "C009", "M010", 3, 2],
    ["V030", "C008", "M006", 1, 1], ]

#FUNCIONES RELACIONADAS A VENTAS

# Para agregar una venta
def alta_venta():

    print("\n--- AGREGAR VENTA ---")
    codigo = input("Ingrese código de venta: ")

    cantidad = 0 # No existe el código, si existe se convierte en 1

    for fila in matriz_ventas:  # Recorremos la fila
        if fila[0] == codigo:  # El primer elemento de la fila es el código
            cantidad = cantidad + 1
    
    while cantidad > 0:
        print("Error: la venta ya existe.")
        codigo = input("Ingrese otro código: ")

        cantidad = 0

        for fila in matriz_ventas:
            if fila[0] == codigo:
                cantidad = cantidad + 1
    
    cliente = input("Ingrese el código del cliente: ")
    cantidad_c = 0 

    for fila in matriz_clientes: 
        if fila[0] == cliente:
            cantidad_c = cantidad_c + 1

    while cantidad_c == 0:
        print("Error: Cliente inexistente.")
        cliente = input("Ingrese el código del cliente: ")
        cantidad_c = 0

        for fila in matriz_clientes:
            if fila[0] == cliente:
                cantidad_c = cantidad_c + 1


    medicamento = input("Ingrese el código del medicamento: ")
    cantidad_m = 0

    for fila in matriz_medicamentos:
        if fila[0] == medicamento:
            cantidad_m = cantidad_m + 1

    while cantidad_m == 0:
        print("Error: Medicamento inexistente.")
        medicamento = input("Ingrese el código del medicamento: ")
        cantidad_m = 0

        for fila in matriz_medicamentos:
            if fila[0] == medicamento:
                cantidad_m = cantidad_m + 1

    lista_cod_medicamentos = []
    for i in range(len(matriz_medicamentos)):
        lista_cod_medicamentos.append(matriz_medicamentos[i][0])

    pos_m = lista_cod_medicamentos.index(medicamento)

    ventas = int(input("Ingrese la cantidad de unidades vendidas: "))
    
    while ventas <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        ventas = int(input("Ingrese la cantidad de unidades vendidas: "))

    while matriz_medicamentos[pos_m][4] < ventas:
        print("Error: No hay suficiente stock.")
        ventas = int(input("Ingrese la cantidad de unidades vendidas: "))

    matriz_medicamentos[pos_m][4] = matriz_medicamentos[pos_m][4] - ventas

    receta = input("¿Presentó receta? (1-Si / 2-No): ")
    if matriz_medicamentos[pos_m][5] == 1 and receta == 2:
        print("Error: Este medicamento requiere receta.")
        print("Venta no registrada.")
    else:
        matriz_ventas.append([codigo, cliente, medicamento, ventas, receta])
        print("Venta registrada correctamente.")

    return 

# Para modificar una venta
def modificar_venta():

    print("\n--- MODIFICAR VENTA ---")
    codigo = input("Ingrese código de venta: ")
    cantidad_v = 0 
  
    for fila in matriz_ventas: 
        if fila[0] == codigo:
            cantidad_v = cantidad_v + 1

    if cantidad_v == 0:
        print("Error: Venta inexistente.")
        pregunta = input("¿Desea buscar otra venta? (1-Si / 2-No): ")
        if pregunta == "1":
            modificar_venta()
        else:  
            return

    lista_cod_ventas = []
    for i in range(len(matriz_ventas)):
        lista_cod_ventas.append(matriz_ventas[i][0])

    pos_v = lista_cod_ventas.index(codigo)
    print("Venta encontrada.")
    print()
    print("¿Cómo desea modificar la venta?")
    print("1- Modificar cliente")
    print("2- Modificar medicamento")
    print("3- Modificar cantidad")
    print("4- Salir. \n")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Ingresando a Modificar cliente...")
        nuevo_cliente = input("Ingrese el nuevo código de cliente: ")

        while nuevo_cliente == matriz_ventas[pos_v][1]:
            print("Error: El cliente ingresado es el mismo que el actual.")
            nuevo_cliente = input("Ingrese el nuevo código de cliente: ")

        cantidad_c = 0
        for fila in matriz_clientes: 
            if fila[0] == nuevo_cliente:
                cantidad_c = cantidad_c + 1
        
        while cantidad_c == 0:
            print("Error: Cliente inexistente.")
            nuevo_cliente = input("Ingrese el código del cliente: ")
            cantidad_c = 0
        
            for fila in matriz_clientes:
                if fila[0] == nuevo_cliente:
                    cantidad_c = cantidad_c + 1

        while nuevo_cliente == matriz_ventas[pos_v][1]:
                    print("Error: El cliente ingresado es el mismo que el actual.")
                    nuevo_cliente = input("Ingrese el nuevo código de cliente: ")

        matriz_ventas[pos_v][1] = nuevo_cliente
        print("Cliente modificado correctamente.")

        print(matriz_ventas[pos_v][1])
    elif opcion == "2":
        print("Ingresando a Modificar medicamento...")
    elif opcion == "3":
        print("Ingresando a Modificar cantidad...")
    else:  
        print("Volviendo al menú principal.\n")
        return

    if opcion == "2":
        nuevo_medicamento = input("Ingrese el nuevo código de medicamento: ")

        while nuevo_medicamento == matriz_ventas[pos_v][2]:
            print("Error: El medicamento ingresado es el mismo que el actual.")
            nuevo_medicamento = input("Ingrese el nuevo código de medicamento: ")

        cantidad_m = 0
        for fila in matriz_medicamentos:
            if fila[0] == nuevo_medicamento:
                cantidad_m = cantidad_m + 1

        while cantidad_m == 0:
            print("Error: Medicamento inexistente.")
            nuevo_medicamento = input("Ingrese el código del medicamento: ")
            cantidad_m = 0

            for fila in matriz_medicamentos:
                if fila[0] == nuevo_medicamento:
                    cantidad_m = cantidad_m + 1

        while nuevo_medicamento == matriz_ventas[pos_v][2]:
                    print("Error: El medicamento ingresado es el mismo que el actual.")
                    nuevo_medicamento = input("Ingrese el nuevo código de medicamento: ")

        matriz_ventas[pos_v][2] = nuevo_medicamento
        print("Medicamento modificado correctamente.")

    if opcion == "3":
        nueva_cantidad = int(input("Ingrese la nueva cantidad de unidades vendidas: "))
        cantidad_vieja = matriz_ventas[pos_v][3]

        while nueva_cantidad <= 0:
            print("Error: la cantidad debe ser mayor a 0.")
            nueva_cantidad = int(input("Ingrese la nueva cantidad de unidades vendidas: "))

        lista_cod_medicamentos = []
        for i in range(len(matriz_medicamentos)):
            lista_cod_medicamentos.append(matriz_medicamentos[i][0])

        pos_m = lista_cod_medicamentos.index(matriz_ventas[pos_v][2])

        while matriz_medicamentos[pos_m][4] < nueva_cantidad:
            print("Error: No hay suficiente stock.")
            nueva_cantidad = int(input("Ingrese la nueva cantidad de unidades vendidas: "))

        cantidad_diferencia = cantidad_vieja - nueva_cantidad
        matriz_medicamentos[pos_m][4] = matriz_medicamentos[pos_m][4] + cantidad_diferencia
        matriz_ventas[pos_v][3] = nueva_cantidad
        print("Cantidad modificada correctamente.")
    
# Para eliminar una venta
def eliminar_venta(usuario):

    print("\n--- ELIMINAR VENTA ---")
    codigo = input("Ingrese código de la venta: ")
    cantidad_v = 0 
      
    for fila in matriz_ventas: 
        if fila[0] == codigo:
            cantidad_v = cantidad_v + 1
    
        if cantidad_v == 0:
            print("Error: Venta inexistente.")
            pregunta = input("¿Desea buscar otra venta? (1-Si / 2-No): ")
            if pregunta == "1":
                eliminar_venta()
            else:  
                return
    
    lista_cod_ventas = []
    for i in range(len(matriz_ventas)):
        lista_cod_ventas.append(matriz_ventas[i][0])

    print("Se encontro la venta")
    if usuario == "admin":
        seguro = input("¿Está seguro que desea eliminar la venta? (1-Si / 2-No): ")
        if seguro == "1":
            pos_v = lista_cod_ventas.index(codigo)
            cantidad_vendida = matriz_ventas[pos_v][3]
            matriz_medicamentos[pos_v][4] = matriz_medicamentos[pos_v][4] + cantidad_vendida
            matriz_ventas.pop(pos_v)
        print("Venta eliminada correctamente.")
    else:
        print("No tiene permisos para eliminar la venta.")
        return

# Para mostrar lista de ventas
def mostrar_ventas():
    ancho_total = 122
    print("\n---- LISTADO DE VENTAS ----\n")
    print("-" * ancho_total)
    print(f'{"Código de Venta":<25}{"Código de Cliente":<25}{"Código de Medicamento":<30}{"Cantidad Vendida":>15}{"¿Presentó Receta?":>25}')
    print("-" * ancho_total)

    for venta in matriz_ventas:
        receta = lambda x: "Si" if x == 1 else "No"
        print(f'{" ":<5}{venta[0]:<25}{venta[1]:<25}{venta[2]:<25}{venta[3]:>9}{receta(venta[4]):>25}')
    print("-" * ancho_total)
    print()

def promedio_ventas():
    ventas = 0

#Funciones a Realizar: Promedio general y por categoria, resumen estadistico: total promedio, ventas mas grandes y pequeñas, conteos. 

