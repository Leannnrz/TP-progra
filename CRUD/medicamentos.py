from colorama import Fore, Style
from CRUD import validaciones

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

    cantidad = 0  # No existe el código, si existe se convierte en 1
    
    for fila in matriz_medicamentos:  # Recorremos la fila
        if fila[0] == codigo:         # El primer elemento de la fila es el código
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
    stock = int(input("Ingrese el stock: "))

    receta = int(input("Requiere receta (1- Si / 2- No): "))
    while receta != 1 and receta != 2:
        print ("Opción no válida: Ingrese una de las opciones.")
        receta = int(input("Requiere receta (1- Si / 2- No): "))

    matriz_medicamentos.append([codigo, nombre, laboratorio, precio, stock, receta])  
    print("Medicamento agregado correctamente.\n")

# Para modificar un medicamento
def modificar_medicamento():

    print(f"{Fore.MAGENTA}{' Modificar Medicamento '.center(30, '=')}")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(matriz_medicamentos)): #Busca la posicion del medicamento
        if matriz_medicamentos[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    matriz_medicamentos[posicion][1] = input("Ingrese el nuevo nombre del medicamento: ")
    matriz_medicamentos[posicion][2] = input("Nuevo laboratorio: ")
    matriz_medicamentos[posicion][3] = int(input("Nuevo precio: "))
    matriz_medicamentos[posicion][4] = int(input("Nuevo stock: "))

    receta = int(input("Requiere receta? (1-Si / 2-No): "))
    while receta != 1 and receta != 2:
        print("Opción no válida: Ingrese una de las opciones.")

        receta = int(input("Requiere receta? (1-Si / 2-No): "))

    matriz_medicamentos[posicion][5] = receta

    print("Medicamento modificado correctamente.")

# Para eliminar un medicamento
def eliminar_medicamento():

    print(f"{Fore.MAGENTA}{' Eliminar Medicamento '.center(30, '=')}")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(matriz_medicamentos)):
        if matriz_medicamentos[i][0] == codigo:   # Busca el código en la columna 0
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    matriz_medicamentos.pop(posicion)
    print("Medicamento eliminado correctamente.")

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
