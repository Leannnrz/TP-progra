from colorama import Fore, Style
from CRUD import validaciones
from FUNCIONES import excepciones
import os

'''
FUNCIONES CRUD DE MEDICAMENTOS
'''
# Para agregar un medicamento
def alta_medicamento():
    print(f"{Fore.MAGENTA}{' Agregar Medicamento '.center(30, '=')}")

    codigo = input("Ingrese el código del medicamento: ")
    valido = validaciones.validar_codigo_medicamento(codigo)

    while valido == False:
        print("Error: el código debe tener el formato M001.")
        codigo = input("Ingrese el código del medicamento: ")
        valido = validaciones.validar_codigo_medicamento(codigo)

    codigos = []

    try:
        with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                if len(datos) == 6:
                    codigos.append(datos[0])

    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo.")

    except OSError as error:
        print("Error al leer el archivo:", error)
        return

    nombre = excepciones.ingresar_texto("Ingrese el nombre: ")
    laboratorio = excepciones.ingresar_texto("Ingrese el laboratorio: ")
    precio = excepciones.ingresar_entero_positivo("Ingrese el precio: ")
    stock = excepciones.ingresar_entero_no_negativo("Ingrese el stock: ")
    receta = excepciones.ingresar_opcion("Requiere receta (1- Si / 2- No): ",[1, 2])
    print("¿Se quiere agregar una descripción del medicamento? (1- Si / 2- No): ")
    opcion_descripcion = int(input())
    if opcion_descripcion == 1:
        descripcion = input("Ingrese la descripción del medicamento: ")
    else:
        descripcion = "No hay descripción disponible."
    while receta != 1 and receta != 2:
        print ("Opción no válida: Ingrese una de las opciones.")
        receta = int(input("Requiere receta (1- Si / 2- No): "))
    
    try:
        with open("medicamentos.txt", "at", encoding="UTF-8") as arch:
            nuevo_medicamento = (
                f"{codigo};{nombre};{laboratorio};"
                f"{precio};{stock};{receta}\n"
            )

            nuevo_medicamento= f'{codigo};{nombre};{laboratorio};{precio};{stock};{receta};{descripcion}\n'
            arch.write(nuevo_medicamento)

        print("Se ha agregado el siguiente medicamento:")
        print(f"{codigo}: {nombre} - $ {precio}")

    except OSError as error:
        print("No se puede grabar el archivo:", error)


# Para modificar un medicamento
def modificar_medicamento():
    print(f"{Fore.MAGENTA}{' Modificar Medicamento '.center(30, '=')}")

    codigo = input("Ingrese código del medicamento: ")
    valido = validaciones.validar_codigo_medicamento(codigo)

    while valido == False:
        print("Error: el código debe tener el formato M001.")
        codigo = input("Ingrese el código del medicamento: ")
        valido = validaciones.validar_codigo_medicamento(codigo)

    temp = "temp.txt"
    encontrado = False

    try:
        with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            lineas = arch.readlines()

        with open(temp, "wt", encoding="UTF-8") as aux:
            for linea in lineas:
                datos = linea.strip().split(";")

                if len(datos) != 6:
                    print("Error: hay un registro inválido en el archivo.")
                    return

                codigo_viejo = datos[0]

                if codigo == codigo_viejo:
                    encontrado = True

                    nombre = datos[1]
                    laboratorio = datos[2]
                    precio = datos[3]
                    stock = datos[4]

                    try:
                        receta_actual = int(datos[5])

                        if receta_actual not in [1, 2]:
                            raise ValueError

                    except ValueError:
                        print("Error: el valor de receta del archivo es inválido.")
                        return

                    print(
                        f"Producto encontrado: {codigo} - "
                        f"{nombre} - ${precio}"
                    )

                    nuevo_nombre = excepciones.ingresar_texto_modificado("Nuevo nombre",nombre)

                    nuevo_laboratorio = excepciones.ingresar_texto_modificado("Nuevo laboratorio",laboratorio)

                    nuevo_precio = excepciones.ingresar_entero_positivo_modificado("Nuevo precio",int(precio))

                    nuevo_stock = excepciones.ingresar_entero_no_negativo_modificado("Nuevo stock",int(stock))

                    receta = excepciones.ingresar_opcion("Requiere receta (1-Sí / 2-No): ",[1, 2])

                    nueva_linea = (
                        f"{codigo};{nuevo_nombre};{nuevo_laboratorio};"
                        f"{nuevo_precio};{nuevo_stock};{receta}\n"
                    )

                    aux.write(nueva_linea)
                    print(f"Producto {codigo} modificado.")

                else:
                    aux.write(linea)

    except FileNotFoundError:
        print("El archivo medicamentos.txt no existe.")
        return

    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return

    if encontrado:
        try:
            os.replace(temp, "medicamentos.txt")
            print("Archivo actualizado correctamente.")

        except OSError as error:
            print("Error al reemplazar el archivo:", error)

    else:
        if os.path.exists(temp):
            os.remove(temp)

        print(f"No se encontró el producto {codigo}.")

    
# Para eliminar un medicamento
def eliminar_medicamento():

    print(f"{Fore.MAGENTA}{' Eliminar Medicamento '.center(30, '=')}")

    codigo = input("Ingrese código del medicamento: ")
    valido = validaciones.validar_codigo_medicamento(codigo)

    while valido == False:
        print("Error: el código debe tener el formato M001.")
        codigo = input("Ingrese código del medicamento: ")
        valido = validaciones.validar_codigo_medicamento(codigo)

    temp = "temp.txt"
    encontrado = False

    try:
        with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            lineas = arch.readlines()

        with open(temp, "wt", encoding="UTF-8") as aux:
            for linea in lineas:
                datos = linea.strip().split(";")

                if len(datos) != 6:
                    print("Error: hay un registro inválido en el archivo.")
                    return

                if codigo != datos[0]:
                    aux.write(linea)
                else:
                    encontrado = True

        if encontrado:
            os.replace(temp, "medicamentos.txt")
            print(f"Producto {codigo} eliminado correctamente.")
        else:
            os.remove(temp)
            print(f"No se encontró el producto {codigo}.")

    except FileNotFoundError:
        print("El archivo medicamentos.txt no existe.")

        if os.path.exists(temp):
            os.remove(temp)

    except OSError as error:
        print("Error en el acceso al archivo:", error)

        if os.path.exists(temp):
            os.remove(temp)


# Para mostrar lista medicamentos
def mostrar_medicamentos():
    try: 
        arch = open("medicamentos.txt", "r", encoding="UTF-8")
        linea = arch.readline().strip()
        ancho_total = 82
        print(f"{Fore.MAGENTA}{' Listado de Medicamentos '.center(80, '=')}")
        print(f'{"Código":<10}{"Nombre":<20}{"Laboratorio":<21}{"Precio":>10}{"Stock":>10}{"Receta":>10}')
        print("-" * ancho_total)

        while linea:
                codigo, nombre, laboratorio, precio, stock, receta = linea.split(";")
                if int(receta) == 1:
                    receta = "Si"
                else:
                    receta = "No"
                print(f'{codigo:10}{nombre:20}{laboratorio:20}{precio:>10}{stock:>10}{receta:>10}')
                linea = arch.readline().strip() # Leemos la línea siguiente
        print("-" * ancho_total)
        print()
    
    except OSError:
            print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

# Para obtener información de un medicamento por código
def buscar_medicamento():
    print(f"{Fore.MAGENTA}{' Buscar Medicamento '.center(30, '=')}")
    codigo = input("Ingrese código del medicamento: ")
    valido = validaciones.validar_codigo_medicamento(codigo)
    
    while valido == False:
        print("Error: el código debe tener el formato M001.")
        codigo = input("Ingrese el código del medicamento: ")
        valido = validaciones.validar_codigo_medicamento(codigo)

    with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            matriz_medicamentos = []
            for linea in arch:
                datos = linea.strip().split(";")
                datos[3] = float(datos[3])  # Convertir el precio a float
                datos[4] = int(datos[4])    # Convertir la cantidad a int
                datos[5] = int(datos[5])    # Convertir la categoría a int
                matriz_medicamentos.append(datos)

    pos = -1
    for j in range(len(matriz_medicamentos)):
        if matriz_medicamentos[j][0] == codigo:
            pos = j

    if pos == -1:
        print("Medicamento no Encontrado")
        print()
        return

    lista_receta_medicamentos = []
    for i in range(len(matriz_medicamentos)):
        lista_receta_medicamentos.append(matriz_medicamentos[i][5])

    list_recetas_med_traducidas = list(map(lambda x: "Si" if x == 1 else "No", lista_receta_medicamentos))

    descripcion_med = str(matriz_medicamentos[pos][6]) 
    if len(descripcion_med) > 100:
        descripcion_med = descripcion_med[:100] + "..."
    print("-" * 130)
    print(f'{"Código":<10}{"Nombre":<20}{"Laboratorio":<21}{"Precio":>10}{"Stock":>10}{"Receta":>10}')
    print("-" * 130)
    print(f'{matriz_medicamentos[pos][0]:10}{matriz_medicamentos[pos][1]:20}{matriz_medicamentos[pos][2]:22}{matriz_medicamentos[pos][3]:>7.2f}{matriz_medicamentos[pos][4]:>10}{list_recetas_med_traducidas[pos]:>10}')
    print("-" * 130)
    print()
    print("-" * 130)
    print(f'{"Descripcion:":<20}{descripcion_med}')
    print("-" * 130)
    print()