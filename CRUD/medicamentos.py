from colorama import Fore, Style
from CRUD import validaciones
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

    nombre = input("Ingrese el nombre: ")
    laboratorio = input("Ingrese el laboratorio: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese el stock: "))
    receta = int(input("Requiere receta (1- Si / 2- No): "))
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
        try:
            with open("medicamentos.txt", "rt", encoding="UTF-8") as arch:
                for linea in arch:
                    datos = linea.strip().split(";")
                    ultimo_codigo = datos[0]
                    while ultimo_codigo == codigo:
                        print(f"{Fore.RED}Error: El código del medicamento ya existe.")
                        codigo = input("Ingrese un nuevo código del medicamento: ")
                        valido = validaciones.validar_codigo_medicamento(codigo)
        except FileNotFoundError:
            print("El archivo no existe. Se creará uno nuevo.")
        with open("medicamentos.txt", "at", encoding="UTF-8") as arch:
            nuevo_medicamento= f'{codigo};{nombre};{laboratorio};{precio};{stock};{receta};{descripcion}\n'
            arch.write(nuevo_medicamento)
            print("Se ha agregado el siguiente medicamento:")
            print(f'{codigo}: {nombre} - $ {precio}')
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

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
        arch = open("medicamentos.txt", "rt", encoding="UTF-8")
        aux = open("temp.txt", "wt", encoding="UTF-8")

        for linea in arch:
            datos = linea.strip().split(";")
            codigo_viejo = datos[0]

            if codigo == codigo_viejo:
                encontrado = True
                nombre = datos[1]
                precio = float(datos[3])
                print(f"Producto encontrado: {codigo} - {nombre} - ${precio:.2f}")

                nuevo_nombre = input("Nuevo nombre (Enter para mantener): ").strip()
                if nuevo_nombre == "":
                    nuevo_nombre = nombre

                nuevo_precio = input("Nuevo precio (Enter para mantener): ").strip()
                if nuevo_precio == "":
                    nuevo_precio = precio
                else:
                    nuevo_precio = float(nuevo_precio)

                nuevo_stock = input("Nuevo stock (Enter para mantener): ").strip()
                if nuevo_stock == "":
                    nuevo_stock = datos[4]

                nuevo_laboratorio = input("Nuevo laboratorio (Enter para mantener): ").strip()
                if nuevo_laboratorio == "":
                    nuevo_laboratorio = datos[2]
                
                receta = int(input("Requiere receta? (1-Si / 2-No): "))
                while receta != 1 and receta != 2:
                    print("Opción no válida: Ingrese una de las opciones.")
                    receta = int(input("Requiere receta? (1-Si / 2-No): "))

                
                nueva_linea = f"{codigo};{nuevo_nombre};{nuevo_laboratorio};{nuevo_precio};{nuevo_stock};{receta}\n"
                aux.write(nueva_linea)
                print(f"Producto {codigo} modificado.")
            else:
                aux.write(linea)
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove("medicamentos.txt")
            os.rename("temp.txt", "medicamentos.txt")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove("temp.txt")
        print(f"No se encontró el producto {codigo}.")
    
# Para eliminar un medicamento
def eliminar_medicamento():

    print(f"{Fore.MAGENTA}{' Eliminar Medicamento '.center(30, '=')}")
    codigo = input("Ingrese código del medicamento: ")
    temp = "temp.txt"
    encontrado = False

    try:
        arch = open("medicamentos.txt", "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = linea.strip().split(";")
            codigo_1 = datos[0]
            if codigo != codigo_1:
                aux.write(linea)
            else:
                encontrado = True

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove("medicamentos.txt")  
            os.rename("temp.txt", "medicamentos.txt") 
            print(f"Producto {codigo} eliminado correctamente.")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)  
        print(f"No se encontró el producto {codigo}.")

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