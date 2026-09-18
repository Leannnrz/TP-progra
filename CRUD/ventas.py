from CRUD.clientes import matriz_clientes
from CRUD.medicamentos import matriz_medicamentos
from colorama import Fore, Style

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

    print(f"{Fore.MAGENTA}{' Agregar Venta '.center(30, '=')}")
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
    print(f"{Fore.GREEN}Venta agregada correctamente.")



#-------------------------
# Modificar una venta
#-------------------------
def modificar_venta():

    print(f"{Fore.MAGENTA}{' Modificar Venta '.center(30, '=')}")

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



#-------------------------
# Eliminar una venta
#-------------------------
def eliminar_venta():

    print(f"{Fore.MAGENTA}{' Eliminar Venta '.center(30, '=')}")
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

    if posicion == -1:
        print("Venta no encontrada.")
        return

    matriz_ventas.pop(posicion)

    print(f"{Fore.GREEN}Venta eliminada correctamente.")


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
        
            print(f'{venta[0]:<8}{venta[1]:<20}{venta[2]:<20}{venta[3]:>10.2f}{receta[4]:>8}')
            

    print("----------------------")

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