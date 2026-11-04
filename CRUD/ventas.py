from CRUD.clientes import matriz_clientes
from CRUD import validaciones
from FUNCIONES import excepciones, recursividad
from colorama import Fore, Style
import re

#Matriz ventas
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

'''
FUNCIÓN VENTAS (CRUD)
'''
#-------------------------
# Agregar una venta
#-------------------------
def alta_venta():

    print(f"{Fore.MAGENTA}{' Agregar Venta '.center(30, '=')}")

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

    print(f"{Fore.GREEN}Venta agregada correctamente.")



#-------------------------
# Modificar una venta
#-------------------------
def modificar_venta():

    print(f"{Fore.MAGENTA}{' Modificar Venta '.center(30, '=')}")

    # Código de venta
    codigo = excepciones.ingresar_codigo("Ingrese código de venta: ",validaciones.validar_codigo_venta,"V001")

    # Verificar que la venta exista
    venta_encontrada = recursividad.buscar_por_codigo_recursivo(matriz_ventas, codigo)

    if venta_encontrada is None:
        print(f"{Fore.RED}Error: Venta no encontrada.")
        return

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

#-------------------------
# Eliminar una venta
#-------------------------
def eliminar_venta():

    print(f"{Fore.MAGENTA}{' Eliminar Venta '.center(30, '=')}")

    # Código de venta
    codigo = excepciones.ingresar_codigo("Ingrese código de la venta: ",validaciones.validar_codigo_venta,"V001")

    # Verificar que la venta exista
    venta_encontrada = recursividad.buscar_por_codigo_recursivo(matriz_ventas, codigo)

    if venta_encontrada is None:
        print(f"{Fore.RED}Error: Venta no encontrada.")
        return

    # Obtener la posición de la venta
    posicion = matriz_ventas.index(venta_encontrada)

    # Eliminar venta
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
