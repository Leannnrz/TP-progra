from CRUD.clientes import matriz_clientes
<<<<<<< HEAD
from CRUD.medicamentos import matriz_medicamentos
from colorama import Fore, Style

=======
from CRUD import validaciones
from FUNCIONES import excepciones, recursividad
from colorama import Fore, Style
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
import re

#Matriz ventas
matriz_ventas = [
<<<<<<< HEAD
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


=======
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
    ["V014", "C009", "M003", 2, 1],
    ["V015", "C001", "M010", 4, 1],
    ["V016", "C003", "M001", 2, 2],
    ["V017", "C007", "M007", 1, 1],
    ["V018", "C005", "M009", 3, 1],
    ["V019", "C008", "M004", 5, 1],
    ["V020", "C010", "M001", 2, 2],
    ["V021", "C004", "M007", 1, 1],
    ["V022", "C001", "M003", 4, 1],
    ["V023", "C006", "M009", 2, 1],
    ["V024", "C010", "M001", 5, 2],
    ["V025", "C002", "M005", 3, 2],
    ["V026", "C007", "M001", 1, 2],
    ["V027", "C003", "M008", 2, 1],
    ["V028", "C005", "M004", 4, 1],
    ["V029", "C009", "M010", 3, 1],
    ["V030", "C008", "M006", 1, 1], ]
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

'''
FUNCIÓN VENTAS (CRUD)
'''
#-------------------------
# Agregar una venta
#-------------------------
def alta_venta():

    print(f"{Fore.MAGENTA}{' Agregar Venta '.center(30, '=')}")
<<<<<<< HEAD
    codigo = input("Ingrese código de venta: ")
    patron = "^V[0-9]{3}$"
    resultado = re.search(patron, codigo)
    valido = 0 # Suponiendo que el codigo no es correcto

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato V001.")
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
        print(f"{Fore.RED}Error: la venta ya existe.")
        codigo = input("Ingrese otro código de venta: ")

        # Verifica nuevamente el formato
        resultado = re.search(patron, codigo)

        if resultado:
            cantidad = 0

            for fila in matriz_ventas:
                if fila[0] == codigo:
                    cantidad = cantidad + 1

        else:
            print(f"{Fore.RED}Error: el código debe tener el formato V001.")

    # Código de cliente
    cliente = input("Ingrese código de cliente: ")
    patron = "^C[0-9]{3}$"
    resultado = re.search(patron, cliente)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato C001.")
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
        print(f"{Fore.RED}Error: Cliente inexistente.")
        return

    # Código de medicamento
    medicamento = input("Ingrese el código del medicamento: ")
    patron = "^M[0-9]{3}$"
    resultado = re.search(patron, medicamento)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato M001.")
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
        print(f"{Fore.RED}Error: Medicamento inexistente.")
        return

    # Cantidad de ventas
    ventas = int(input("Ingrese la cantidad de ventas: "))

    while ventas <= 0:
        print(f"{Fore.RED}Error: la cantidad debe ser mayor a 0.")
        ventas = int(input("Ingrese la cantidad de ventas: "))

    # Verifica receta
    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))
    while receta != 1 and receta != 2:
        print(f"{Fore.RED}Opción inválida: Ingrese una de las opciones.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    # Verificar si el medicamento requiere receta
    if requiere_receta == 1 and receta == 2:
        print(f"{Fore.RED}Error: Este medicamento requiere receta.")
        return

    matriz_ventas.append([codigo, cliente, medicamento, ventas, receta])
=======

    # Código de venta
    codigo = excepciones.ingresar_codigo("Ingrese código de venta: ",validaciones.validar_codigo_venta,"V001")

    # Verificar que el código no exista
    venta = recursividad.buscar_por_codigo_recursivo(matriz_ventas, codigo, 0)

    while venta is not None:
        print(f"{Fore.RED}Error: la venta ya existe.")

        codigo = excepciones.ingresar_codigo("Ingrese otro código de venta: ",validaciones.validar_codigo_venta,"V001")

        venta = recursividad.buscar_por_codigo_recursivo(matriz_ventas, codigo, 0)

    # Código de cliente
    cliente = excepciones.ingresar_codigo("Ingrese código de cliente: ",validaciones.validar_codigo_cliente,"C001")

    # Verificar que el cliente exista
    lista_clientes = matriz_clientes()

    if lista_clientes is None:
        print(f"{Fore.RED}Error: no se pudo obtener la lista de clientes.")
        return

    cliente_encontrado = recursividad.buscar_por_codigo_recursivo(lista_clientes, cliente, 0)

    if cliente_encontrado is None:
        print(f"{Fore.RED}Error: Cliente inexistente.")
        return

    # Código de medicamento
    medicamento = excepciones.ingresar_codigo("Ingrese el código del medicamento: ",validaciones.validar_codigo_medicamento,"M001")

    # Verificar que el medicamento exista
    try:
        with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            lineas = arch.readlines()

        medicamento_encontrado = recursividad.buscar_medicamento_recursivo(lineas, medicamento)

    except FileNotFoundError:
        print(f"{Fore.RED}Error: no existe el archivo medicamentos.txt.")
        return

    except OSError as error:
        print(f"{Fore.RED}Error al leer el archivo: {error}")
        return

    if medicamento_encontrado is None:
        print(f"{Fore.RED}Error: Medicamento inexistente.")
        return

    # Cantidad de unidades vendidas
    ventas = excepciones.ingresar_entero_positivo("Ingrese la cantidad de unidades vendidas: ")

    # Verificar receta
    receta = excepciones.ingresar_opcion("¿Presentó receta? (1-Sí / 2-No): ",[1, 2])

    # Registrar venta
    matriz_ventas.append([codigo, cliente, medicamento, ventas, receta])

>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
    print(f"{Fore.GREEN}Venta agregada correctamente.")



#-------------------------
# Modificar una venta
#-------------------------
def modificar_venta():

    print(f"{Fore.MAGENTA}{' Modificar Venta '.center(30, '=')}")
<<<<<<< HEAD

    # Código de venta
    codigo = input("Ingrese código de venta: ")
    patron = "^V[0-9]{3}$"
    resultado = re.search(patron, codigo)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato V001.")
        codigo = input("Ingrese código de venta: ")
        resultado = re.search(patron, codigo)

        if resultado:
            valido = 1

    posicion = -1

    for i in range(len(matriz_ventas)):
        if matriz_ventas[i][0] == codigo:
            posicion = i
=======

    # Código de venta
    codigo = excepciones.ingresar_codigo("Ingrese código de venta: ",validaciones.validar_codigo_venta,"V001")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    # Verificar que la venta exista
    venta_encontrada = recursividad.buscar_por_codigo_recursivo(matriz_ventas, codigo)

    if venta_encontrada is None:
        print(f"{Fore.RED}Error: Venta no encontrada.")
        return

<<<<<<< HEAD
    # Código de cliente
    cliente = input("Nuevo código de cliente: ")
    patron = "^C[0-9]{3}$"
    resultado = re.search(patron, cliente)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato C001.")
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
        print(f"{Fore.RED}Error: Cliente inexistente.")
        return

    # Código de medicamento
    medicamento = input("Nuevo código de medicamento: ")
    patron = "^M[0-9]{3}$"
    resultado = re.search(patron, medicamento)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato M001.")
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
        print(f"{Fore.RED}Error: Medicamento inexistente.")
        return

    # Nueva cantidad
    cantidad_venta = int(input("Ingrese nueva cantidad: "))

    while cantidad_venta <= 0:
        print(f"{Fore.RED}Error: la cantidad debe ser mayor a 0.")
        cantidad_venta = int(input("Ingrese nueva cantidad vendida: "))

    # Verificar receta
    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    while receta != 1 and receta != 2:
        print(f"{Fore.RED}Opción inválida: Ingrese una de las opciones.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))

    # Verificar si el medicamento requiere receta
    if requiere_receta == 1 and receta == 2:
        print(f"{Fore.RED}Error: Este medicamento requiere receta.")
        return

    matriz_ventas[posicion][1] = cliente
    matriz_ventas[posicion][2] = medicamento
    matriz_ventas[posicion][3] = cantidad_venta
    matriz_ventas[posicion][4] = receta
    print(f"{Fore.GREEN}Venta modificada correctamente.")
=======
    posicion = matriz_ventas.index(venta_encontrada)

    # Código de cliente
    cliente = excepciones.ingresar_codigo("Nuevo código de cliente: ",validaciones.validar_codigo_cliente,"C001")

    # Verificar que el cliente exista
    lista_clientes = matriz_clientes()

    if lista_clientes is None:
        print(f"{Fore.RED}Error: no se pudo obtener la lista de clientes.")
        return

    cliente_encontrado = recursividad.buscar_por_codigo_recursivo(lista_clientes, cliente)

    if cliente_encontrado is None:
        print(f"{Fore.RED}Error: Cliente inexistente.")
        return

    # Código de medicamento
    medicamento = excepciones.ingresar_codigo("Nuevo código de medicamento: ",validaciones.validar_codigo_medicamento,"M001")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    # Verificar que el medicamento exista
    try:
        with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            lineas = arch.readlines()

        medicamento_encontrado = recursividad.buscar_medicamento_recursivo(lineas, medicamento)

<<<<<<< HEAD
=======
    except FileNotFoundError:
        print(f"{Fore.RED}Error: no existe el archivo medicamentos.txt.")
        return

    except OSError as error:
        print(f"{Fore.RED}Error al leer el archivo: {error}")
        return

    if medicamento_encontrado is None:
        print(f"{Fore.RED}Error: Medicamento inexistente.")
        return

    # Nueva cantidad
    cantidad_venta = excepciones.ingresar_entero_positivo("Ingrese nueva cantidad: ")

    # Verificar receta
    receta = excepciones.ingresar_opcion("¿Presentó receta? (1-Sí / 2-No): ",[1, 2])

    # Actualizar venta
    matriz_ventas[posicion][1] = cliente
    matriz_ventas[posicion][2] = medicamento
    matriz_ventas[posicion][3] = cantidad_venta
    matriz_ventas[posicion][4] = receta

    print(f"{Fore.GREEN}Venta modificada correctamente.")

>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
#-------------------------
# Eliminar una venta
#-------------------------
def eliminar_venta():

    print(f"{Fore.MAGENTA}{' Eliminar Venta '.center(30, '=')}")
<<<<<<< HEAD
    codigo = input("Ingrese código de la venta: ")
    patron = "^V[0-9]{3}$"
    resultado = re.search(patron, codigo)
    valido = 0

    if resultado:
        valido = 1

    while valido == 0:
        print(f"{Fore.RED}Error: el código debe tener el formato V001.")
        codigo = input("Ingrese código de la venta: ")

        resultado = re.search(patron, codigo)

        if resultado:
            valido = 1

    posicion = -1

    for i in range(len(matriz_ventas)):
        if matriz_ventas[i][0] == codigo:
            posicion = i
=======

    # Código de venta
    codigo = excepciones.ingresar_codigo("Ingrese código de la venta: ",validaciones.validar_codigo_venta,"V001")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    # Verificar que la venta exista
    venta_encontrada = recursividad.buscar_por_codigo_recursivo(matriz_ventas, codigo)

    if venta_encontrada is None:
        print(f"{Fore.RED}Error: Venta no encontrada.")
        return

<<<<<<< HEAD
    matriz_ventas.pop(posicion)

    print(f"{Fore.GREEN}Venta eliminada correctamente.")


=======
    # Obtener la posición de la venta
    posicion = matriz_ventas.index(venta_encontrada)

    # Eliminar venta
    matriz_ventas.pop(posicion)

    print(f"{Fore.GREEN}Venta eliminada correctamente.")



>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
#-------------------------
# Mostrar lista de ventas
#-------------------------
def mostrar_ventas():

    print("\n--- LISTADO DE VENTAS ---")
    print(f"{Fore.MAGENTA}{' Listado de Ventas '.center(66, '=')}")
    print(f'{"Código":<8}{"Cliente":<20}{"Medicamento":<20}{"Cantidad":>10}{"Receta":>8}')
    print("-" * 66)

    for venta in matriz_ventas:
        if venta[4] == 1:
            receta = "Si"
        else:
            receta = "No"
        
<<<<<<< HEAD
            print(f'{venta[0]:<8}{venta[1]:<20}{venta[2]:<20}{venta[3]:>10.2f}{receta:>8}\n')
            


#-------------------------
# Buscar ventas
#-------------------------
def buscar_venta():
    print(f"{Fore.MAGENTA}{' Buscar Venta '.center(30, '=')}")
    print("¿Cómo desea buscar la venta?")   
    print("1- Por Codigo")
    print("2- Por Cliente ")
    print("3- Por Medicamento")   
    print("4- Salir. \n")

    opcion = input("Ingrese la opción: ")  
    if opcion == "1":
        codigo = input("Ingrese código de venta: ")
        cantidad_v = 0 

        for fila in matriz_ventas: 
            if fila[0] == codigo:
                cantidad_v = cantidad_v + 1
        
        if cantidad_v == 0:
            print(f"{Fore.RED}Error: Venta inexistente.")
            pregunta = input("¿Desea buscar otra venta? (1-Si / 2-No): ")
            if pregunta == "1":
                buscar_venta()
            else:  
                return
        
        lista_cod_ventas = []
        for i in range(len(matriz_ventas)):
            lista_cod_ventas.append(matriz_ventas[i][0])
        pos_v = lista_cod_ventas.index(codigo)

        print("Venta Encontrada")
        ancho_total = 122
        print("-" * ancho_total)
        print(f'{"Código de Venta":<25}{"Código de Cliente":<25}{"Código de Medicamento":<30}{"Cantidad Vendida":>15}{"¿Presentó Receta?":>25}')
        print("-" * ancho_total)
        receta = matriz_ventas[pos_v][4]
        receta = lambda x: "Si" if x == 1 else "No"
        print(f'{" ":<5}{matriz_ventas[pos_v][0]:<25}{matriz_ventas[pos_v][1]:<25}{matriz_ventas[pos_v][2]:<25}{matriz_ventas[pos_v][3]:>9}{matriz_ventas[pos_v][4]:>25}')
        print("-" * ancho_total)
        print()

    
    elif opcion == "2":
        codigo = input("Ingrese el codigo del Cliente para buscar sus Compras: ") 
        cantidad_c = 0
        for fila in matriz_clientes:
            if fila[0] == codigo:
                cantidad_c = cantidad_c + 1
                        
        while cantidad_c == 0:
            print("Error: Cliente inexistente.")
            codigo = input("Ingrese el código del medicamento: ")
            cantidad_c = 0
            for fila in matriz_clientes:
                if fila[0] == codigo:
                    cantidad_c = cantidad_c + 1
                        
        lista_cod_clientes = []
        pos = 0
        for i in range(len(matriz_ventas)):
            if codigo == matriz_ventas[i][1]:
                lista_cod_clientes.append(pos)
            pos = pos + 1 
        
        ancho_total = 122
        print("\n---- LISTADO DE VENTAS RELACIONADAS AL CLIENTE",codigo,"---\n")
        print("-" * ancho_total)
        print(f'{"Código de Venta":<25}{"Código de Cliente":<25}{"Código de Medicamento":<30}{"Cantidad Vendida":>15}{"¿Presentó Receta?":>25}')
        print("-" * ancho_total)
        for j in lista_cod_clientes:
            receta = lambda x: "Si" if x == 1 else "No"           
            print(f'{" ":<5}{matriz_ventas[j][0]:<25}{matriz_ventas[j][1]:<25}{matriz_ventas[j][2]:<25}{matriz_ventas[j][3]:>9}{receta(matriz_ventas[j][4]):>25}')
        print("-" * ancho_total)
        print() 

    elif opcion == "3":
        codigo = input("Ingrese el codigo del Medicamento para Buscar sus Ventas: ")
        cantidad_m = 0
        for fila in matriz_medicamentos:
            if fila[0] == codigo:
                cantidad_m = cantidad_m + 1
                
        while cantidad_m == 0:
            print("Error: Medicamento inexistente.")
            medicamento = input("Ingrese el código del medicamento: ")
            cantidad_m = 0
            for fila in matriz_medicamentos:
                if fila[0] == medicamento:
                    cantidad_m = cantidad_m + 1
                
        lista_cod_medicamentos = []
        pos = 0
        for i in range(len(matriz_ventas)):
            if codigo == matriz_ventas[i][2]:
                lista_cod_medicamentos.append(pos)
            pos = pos + 1 

        ancho_total = 122
        print("\n---- LISTADO DE VENTAS RELACIONADAS AL MEDICAMENTO",codigo,"---\n")
        print("-" * ancho_total)
        print(f'{"Código de Venta":<25}{"Código de Cliente":<25}{"Código de Medicamento":<30}{"Cantidad Vendida":>15}{"¿Presentó Receta?":>25}')
        print("-" * ancho_total)
        for j in lista_cod_medicamentos:
            receta = lambda x: "Si" if x == 1 else "No"           
            print(f'{" ":<5}{matriz_ventas[j][0]:<25}{matriz_ventas[j][1]:<25}{matriz_ventas[j][2]:<25}{matriz_ventas[j][3]:>9}{receta(matriz_ventas[j][4]):>25}')
        print("-" * ancho_total)
        print() 
        

    else:
        print("Regresando al Menu")
        return
=======
        print(f'{venta[0]:<8}{venta[1]:<20}{venta[2]:<20}{venta[3]:>10.2f}{receta:>8}\n')
            
#-------------------------
# Buscar ventas
#-------------------------
def buscar_venta():
    print(f"{Fore.MAGENTA}{' Buscar Venta '.center(30, '=')}")
    print("¿Cómo desea buscar la venta?")
    print("1- Por Código")
    print("2- Por Cliente")
    print("3- Por Medicamento")
    print("4- Salir.\n")

    opcion = excepciones.ingresar_opcion("Ingrese la opción: ",[1, 2, 3, 4])

    # Buscar por código de venta
    if opcion == 1:

        codigo = excepciones.ingresar_codigo("Ingrese código de venta: ",validaciones.validar_codigo_venta,"V001")

        posicion = -1

        for i in range(len(matriz_ventas)):
            if matriz_ventas[i][0] == codigo:
                posicion = i

        if posicion == -1:
            print(f"{Fore.RED}Error: Venta inexistente.")

            pregunta = excepciones.ingresar_opcion("¿Desea buscar otra venta? (1-Sí / 2-No): ",[1, 2])

            if pregunta == 1:
                buscar_venta()

            return

        print("Venta encontrada")

        ancho_total = 122
        print("-" * ancho_total)
        print(f'{"Código de Venta":<25}'f'{"Código de Cliente":<25}'f'{"Código de Medicamento":<30}'f'{"Cantidad Vendida":>15}'f'{"¿Presentó Receta?":>25}')
        print("-" * ancho_total)

        receta = "Sí" if matriz_ventas[posicion][4] == 1 else "No"

        print(f'{matriz_ventas[posicion][0]:<25}'f'{matriz_ventas[posicion][1]:<25}'f'{matriz_ventas[posicion][2]:<30}'f'{matriz_ventas[posicion][3]:>15}'f'{receta:>25}')

        print("-" * ancho_total)
        print()

    # Buscar por cliente
    elif opcion == 2:

        codigo = excepciones.ingresar_codigo("Ingrese el código del cliente para buscar sus compras: ",validaciones.validar_codigo_cliente,"C001")

        cantidad_c = 0

        for fila in matriz_clientes:
            if fila[0] == codigo:
                cantidad_c = cantidad_c + 1

        while cantidad_c == 0:
            print(f"{Fore.RED}Error: Cliente inexistente.")

            codigo = excepciones.ingresar_codigo("Ingrese el código del cliente: ",validaciones.validar_codigo_cliente,"C001")

            cantidad_c = 0

            for fila in matriz_clientes:
                if fila[0] == codigo:
                    cantidad_c = cantidad_c + 1

        lista_cod_ventas = []

        for i in range(len(matriz_ventas)):
            if codigo == matriz_ventas[i][1]:
                lista_cod_ventas.append(i)

        ancho_total = 122

        print("\n---- LISTADO DE VENTAS RELACIONADAS AL CLIENTE",codigo,"---\n")
        print("-" * ancho_total)
        print(f'{"Código de Venta":<25}'f'{"Código de Cliente":<25}'f'{"Código de Medicamento":<30}'f'{"Cantidad Vendida":>15}'f'{"¿Presentó Receta?":>25}')
        print("-" * ancho_total)

        if len(lista_cod_ventas) == 0:
            print("El cliente no tiene ventas registradas.")

        for j in lista_cod_ventas:
            receta = "Sí" if matriz_ventas[j][4] == 1 else "No"

            print(f'{matriz_ventas[j][0]:<25}'f'{matriz_ventas[j][1]:<25}'f'{matriz_ventas[j][2]:<30}'f'{matriz_ventas[j][3]:>15}'f'{receta:>25}')

        print("-" * ancho_total)
        print()

    # Buscar por medicamento
    elif opcion == 3:

        codigo = excepciones.ingresar_codigo("Ingrese el código del medicamento para buscar sus ventas: ",validaciones.validar_codigo_medicamento,"M001")

        codigos_medicamentos = []

        try:
            with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
                for linea in arch:
                    datos = linea.strip().split(";")

                    if len(datos) != 6:
                        print(f"{Fore.RED}Error: hay un registro inválido en medicamentos.txt.")
                        return

                    codigos_medicamentos.append(datos[0])

        except FileNotFoundError:
            print(f"{Fore.RED}Error: no existe el archivo medicamentos.txt.")
            return

        except OSError as error:
            print(f"{Fore.RED}Error al leer el archivo: {error}")
            return

        if codigo not in codigos_medicamentos:
            print(f"{Fore.RED}Error: Medicamento inexistente.")
            return

        lista_cod_ventas = []

        for i in range(len(matriz_ventas)):
            if codigo == matriz_ventas[i][2]:
                lista_cod_ventas.append(i)

        ancho_total = 122

        print("\n---- LISTADO DE VENTAS RELACIONADAS AL MEDICAMENTO",codigo,"---\n")
        print("-" * ancho_total)
        print(f'{"Código de Venta":<25}'f'{"Código de Cliente":<25}'f'{"Código de Medicamento":<30}'f'{"Cantidad Vendida":>15}'f'{"¿Presentó Receta?":>25}')
        print("-" * ancho_total)

        if len(lista_cod_ventas) == 0:
            print("No hay ventas registradas para este medicamento.")

        for j in lista_cod_ventas:
            receta = "Sí" if matriz_ventas[j][4] == 1 else "No"

            print(f'{matriz_ventas[j][0]:<25}'f'{matriz_ventas[j][1]:<25}'f'{matriz_ventas[j][2]:<30}'f'{matriz_ventas[j][3]:>15}'f'{receta:>25}')

        print("-" * ancho_total)
        print()

    # Salir
    elif opcion == 4:
        print("Regresando al menú.")
        return
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
