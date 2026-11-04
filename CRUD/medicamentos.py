from colorama import Fore, Style
<<<<<<< HEAD

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


=======
from CRUD import validaciones
from FUNCIONES import excepciones, recursividad
import os
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

'''
FUNCIONES CRUD DE MEDICAMENTOS
'''
# Para agregar un medicamento
def alta_medicamento():
    print(f"{Fore.MAGENTA}{' Agregar Medicamento '.center(30, '=')}")

<<<<<<< HEAD
    print(f"{Fore.MAGENTA}{' Agregar Medicamento '.center(30, '=')}")
    codigo = input("Ingrese el código del medicamento: ")
=======
    codigo = excepciones.ingresar_codigo("Ingrese el código del medicamento: ",validaciones.validar_codigo_medicamento,"M001")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

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
    
    
<<<<<<< HEAD
    while cantidad > 0:
        print("Error: el medicamento ya existe.")
        codigo = input("Ingrese otro código: ")
    
        cantidad = 0
    
        for fila in matriz_medicamentos:
            if fila[0] == codigo:
                cantidad = cantidad + 1
=======
    try:
        with open("medicamentos.txt", "at", encoding="UTF-8") as arch:
            nuevo_medicamento = (
                f"{codigo};{nombre};{laboratorio};"
                f"{precio};{stock};{receta}\n"
            )
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

            nuevo_medicamento= f'{codigo};{nombre};{laboratorio};{precio};{stock};{receta};{descripcion}\n'
            arch.write(nuevo_medicamento)

<<<<<<< HEAD
    nombre = input("Ingrese el nombre: ")
    laboratorio = input("Ingrese el laboratorio: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese el stock: "))

    receta = int(input("Requiere receta (1- Si / 2- No): "))
    while receta != 1 and receta != 2:
        print ("Opción no válida: Ingrese una de las opciones.")
        receta = int(input("Requiere receta (1- Si / 2- No): "))

    matriz_medicamentos.append([codigo, nombre, laboratorio, precio, stock, receta])  
    print("Medicamento agregado correctamente.\n")
=======
        print("Se ha agregado el siguiente medicamento:")
        print(f"{codigo}: {nombre} - $ {precio}")

    except OSError as error:
        print("No se puede grabar el archivo:", error)
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3


# Para modificar un medicamento
def modificar_medicamento():
    print(f"{Fore.MAGENTA}{' Modificar Medicamento '.center(30, '=')}")

<<<<<<< HEAD
    print(f"{Fore.MAGENTA}{' Modificar Medicamento '.center(30, '=')}")
=======
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
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

<<<<<<< HEAD
    matriz_medicamentos[posicion][1] = input("Ingrese el nuevo nombre del medicamento: ")
    matriz_medicamentos[posicion][2] = int(input("Nuevo laboratorio: "))
    matriz_medicamentos[posicion][3] = int(input("Nuevo precio: "))
    matriz_medicamentos[posicion][4] = int(input("Nuevo stock: "))

    receta = int(input("Requiere receta? (1-Si / 2-No): "))
    while receta != 1 and receta != 2:
        print("Opción no válida: Ingrese una de las opciones.")

        receta = int(input("Requiere receta? (1-Si / 2-No): "))

    matriz_medicamentos[posicion][5] = receta
=======
    except OSError as error:
        print("Error en el acceso al archivo:", error)
        return
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

    if encontrado:
        try:
            os.replace(temp, "medicamentos.txt")
            print("Archivo actualizado correctamente.")

        except OSError as error:
            print("Error al reemplazar el archivo:", error)

<<<<<<< HEAD

=======
    else:
        if os.path.exists(temp):
            os.remove(temp)

        print(f"No se encontró el producto {codigo}.")

    
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
# Para eliminar un medicamento
def eliminar_medicamento():

    print(f"{Fore.MAGENTA}{' Eliminar Medicamento '.center(30, '=')}")
<<<<<<< HEAD
=======

>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
    codigo = input("Ingrese código del medicamento: ")
    valido = validaciones.validar_codigo_medicamento(codigo)

    while valido == False:
        print("Error: el código debe tener el formato M001.")
        codigo = input("Ingrese código del medicamento: ")
        valido = validaciones.validar_codigo_medicamento(codigo)

<<<<<<< HEAD
    if posicion == -1:
        print("Medicamento no encontrado.")
        return
=======
    temp = "temp.txt"
    encontrado = False
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

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
<<<<<<< HEAD
    ancho_total = 80
    print("\n---- LISTADO DE MEDICAMENTOS ----\n")
    print(f"{Fore.MAGENTA}{' Listado de Medicamentos '.center(70, '=')}")
    print(f'{"Código":<10}{"Nombre":<20}{"Laboratorio":<20}{"Precio":>10}{"Stock":>5}{"Receta":>5}')
    print("-" * ancho_total)
=======
    try: 
        arch = open("medicamentos.txt", "r", encoding="UTF-8")
        linea = arch.readline().strip()
        ancho_total = 82
        print(f"{Fore.MAGENTA}{' Listado de Medicamentos '.center(80, '=')}")
        print(f'{"Código":<10}{"Nombre":<20}{"Laboratorio":<21}{"Precio":>10}{"Stock":>10}{"Receta":>10}')
        print("-" * ancho_total)
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3

        while linea:
                codigo, nombre, laboratorio, precio, stock, receta, descripcion = linea.split(";")
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

    codigo = excepciones.ingresar_codigo("Ingrese codigo del medicamento: ",validaciones.validar_codigo_medicamento,"M001")

    try:
        with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
            lineas = arch.readlines()

        medicamento = recursividad.buscar_medicamento_recursivo(lineas, codigo)

        if medicamento is None:
            print("Medicamento no encontrado.")
            print()
            return

        precio = float(medicamento[3])
        stock = int(medicamento[4])
        receta = int(medicamento[5])

        if receta == 1:
            receta_traducida = "Si"
        else:
            receta_traducida = "No"

<<<<<<< HEAD
        print(f'{medicamento[0]:<8}{medicamento[1]:<20}{medicamento[2]:<20}{medicamento[3]:>10.2f}{medicamento[4]:>8}{receta:>10}\n')
    
=======
        descripcion = medicamento[6]

        if len(descripcion) > 100:
            descripcion = descripcion[:100] + "..."

        print("-" * 130)
        print(f'{"Codigo":<10}{"Nombre":<20}{"Laboratorio":<21}' f'{"Precio":>10}{"Stock":>10}{"Receta":>10}')
        print("-" * 130)

        print(
            f'{medicamento[0]:10}'
            f'{medicamento[1]:20}'
            f'{medicamento[2]:22}'
            f'{precio:>7.2f}'
            f'{stock:>10}'
            f'{receta_traducida:>10}'
        )

        print("-" * 130)
        print(f'{"Descripcion:":<20}{descripcion}')
        print("-" * 130)
        print()

    except FileNotFoundError:
        print("El archivo medicamentos.txt no existe.")

    except (OSError, IndexError, ValueError) as error:
        print(f"Error al consultar el medicamento: {error}")
>>>>>>> 3342944e362e354625de69fd10e0c28c5f00ded3
