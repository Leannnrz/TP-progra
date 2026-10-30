# Importacion de módulos.
from colorama import init, Fore, Back, Style
from CRUD import clientes, medicamentos, ventas, estadisticas
from FUNCIONES import excepciones, recursividad
from login import registrar_usuario, cargar_usuarios, iniciar_sesion
import re

init(autoreset=True) # Inicialización de colorama

'''
Función de login
'''
def login(max_intentos):

    intentos = 0

    while intentos < max_intentos:
        usuario = input("Ingrese el usuario: ").lower()
        contrasenia = input("Ingrese la contraseña: ")

        if usuario == "admin" and contrasenia == "1234":
            print(f"{Fore.GREEN}Login exitoso!")
            print("Ingresó como administrador.\n")
            return "admin"
        usuarios = cargar_usuarios()

        for datos in usuarios:
            if usuario == datos[0].lower() and contrasenia == datos[1]:
                print(f"{Fore.GREEN}¡Login exitoso!")
                print("Ingresó como usuario.\n")
                return "usuario"

        intentos = intentos + 1

        print(f"{Fore.RED}Usuario o contraseña incorrectos.")
        print("Intentos restantes:", max_intentos - intentos)
        print()

    print("Ha superado el límite de intentos.")
    return None

def menu_de_acceso():

    opcion = ""

    while opcion != "3":

        print("=" * 175)
        print("Bienvenido al sistema de registro e inicio de sesión".rjust(100))
        print("=" * 175)

        print("Seleccione una opción:\n")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir del sistema\n")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":

            tipo_usuario = login(3)

            if tipo_usuario == "admin":
                mostrar_menu("admin")

            elif tipo_usuario == "usuario":
                mostrar_menu("usuario")

        elif opcion == "3":
            print("Saliendo del sistema...")

        else:
            print("\nError: Opción inválida. Por favor, seleccione una opción válida.\n")

'''
SUBMENÚS
'''
# Submenú clientes
def submenu_clientes():
    opcion_clientes = 0

    while opcion_clientes != 5:

        print(f"{Fore.CYAN}{'CLIENTES'.center(25)}\n{'-' * 25}")
        print("1- Agregar cliente")
        print("2- Modificar cliente")
        print("3- Eliminar cliente")
        print("4- Mostrar cliente")
        print("5- Volver.\n")

        opcion_clientes = excepciones.ingresar_opcion("Seleccione una opción: ",[1, 2, 3, 4, 5])
        print()

        if opcion_clientes == 1:
            clientes.alta_cliente()
        elif opcion_clientes == 2:
            clientes.modificar_cliente()
        elif opcion_clientes == 3:
            clientes.eliminar_cliente()
        elif opcion_clientes == 4:
            clientes.mostrar_clientes()
        elif opcion_clientes == 5:
            print("Volviendo al menú principal... \n")
        

# Submenú medicamentos
def submenu_medicamentos():
    opcion_medicamentos = 0

    while opcion_medicamentos != 6:

        print(f"{Fore.CYAN}{'MEDICAMENTOS'.center(25)}\n{'-' * 25}")        
        print("1- Crear medicamento")
        print("2- Modificar medicamento")
        print("3- Eliminar medicamento")
        print("4- Mostrar medicamentos")
        print("5- Buscar medicamento")
        print("6- Volver. \n")

        opcion_medicamentos = excepciones.ingresar_opcion("Seleccione una opción: ",[1, 2, 3, 4, 5])
        print()

        if opcion_medicamentos == 1:
            medicamentos.alta_medicamento()
        elif opcion_medicamentos == 2:
            medicamentos.modificar_medicamento()
        elif opcion_medicamentos == 3:
            medicamentos.eliminar_medicamento()
        elif opcion_medicamentos == 4:
            medicamentos.mostrar_medicamentos()
        elif opcion_medicamentos == 5:
            medicamentos.buscar_medicamento()
        elif opcion_medicamentos == 6:
            print("Volviendo al menú principal.\n")


# Submenú de ventas
def submenu_ventas():
    opcion_ventas = 0

    while opcion_ventas != 6:

        print(f"{Fore.CYAN}{'VENTAS'.center(20)}\n{'-' * 20}")
        print("1- Crear venta")
        print("2- Modificar venta")
        print("3- Eliminar venta")
        print("4- Mostrar ventas")
        print("5- Buscar venta")
        print("6- Volver.\n")

        opcion_ventas = excepciones.ingresar_opcion("Seleccione una opción: ",[1, 2, 3, 4, 5, 6])
        print()
        if opcion_ventas == 1:
            ventas.alta_venta()
        elif opcion_ventas == 2:
            ventas.modificar_venta()
        elif opcion_ventas == 3:
            ventas.eliminar_venta()
        elif opcion_ventas == 4:
            ventas.mostrar_ventas()
        elif opcion_ventas == 5:
            ventas.buscar_venta()
        elif opcion_ventas == 6:
            print("Volviendo al menú principal.\n")
        

#Submenú de Estadisticas
def submenu_estadisticas(): 
    opcion_estadisticas = 0
    while opcion_estadisticas != 12:
        print(f"{Fore.CYAN}{'VENTAS'.center(20)}\n{'-' * 20}")
        print("1- Ganancia Total")
        print("2- Venta Más Grande")
        print("3- Venta Más Pequeña")
        print("4- Medicamento Más Vendido")
        print("5- Buscar Ganancias por Medicamento")  
        print("6- Ver Estadisticas de Clientes") 
        print("7- Ver Reporte de Medicamentos")
        print("8- Ver Ventas con Receta")
        print("9- Ver Valor Total del Stock")
        print("10- Ver Ventas con Receta")
        print("11- Ver Cantidad Total Vendida")
        print("12- Volver.\n")  

        opcion_estadisticas = excepciones.ingresar_opcion("Seleccione una opción: ",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        if opcion_estadisticas == 1:
            estadisticas.total_recaudado()
        elif opcion_estadisticas == 2:
            estadisticas.mayor_venta()
        elif opcion_estadisticas == 3:
            estadisticas.menor_venta()
        elif opcion_estadisticas == 4:
            estadisticas.med_mas_vendido()
        elif opcion_estadisticas == 5:
            estadisticas.ganancia_x_medicamento()
        elif opcion_estadisticas == 6:
            estadisticas.stats_clientes()
        elif opcion_estadisticas == 7:
            estadisticas.reporte_medicamento()
        elif opcion_estadisticas == 8:
            estadisticas.mostrar_medicamentos_con_receta()
        elif opcion_estadisticas == 9:
            estadisticas.mostrar_valor_total_stock()
        elif opcion_estadisticas == 10:
            estadisticas.mostrar_ventas_con_receta()
        elif opcion_estadisticas == 11:
            estadisticas.mostrar_cantidad_total_vendida()
        elif opcion_estadisticas == 12:
            print("Volviendo al menú principal.\n")
        
'''
MENÚ PRINCIPAL
'''
def mostrar_menu(tipo_usuario):

    if tipo_usuario == "admin":
        opcion = 0

        while opcion != "5":

            print(f"{Style.BRIGHT}{'-' * 80}\n{'Menú Principal'.center(25)}\n{'-' * 80}")
            print(f"{Style.BRIGHT}\n1- Clientes")
            print(f"{Style.BRIGHT}2- Medicamentos")
            print(f"{Style.BRIGHT}3- Ventas")
            print(f"{Style.BRIGHT}4- Estadísticas")
            print(f"{Style.BRIGHT}5- Salir\n")

            opcion = input("Seleccione una opción: ")
        
            if opcion == "1":
                submenu_clientes()
            elif opcion == "2":
                submenu_medicamentos()
            elif opcion == "3":
                submenu_ventas()
            elif opcion == "4":
                submenu_estadisticas()
            elif opcion == "5":
                print("Cerrando sesión...")
            else:
                print(f"{Fore.RED}Opción no válida.")

    elif tipo_usuario == "usuario":

        opcion = ""

        while opcion != "4":
            print(f"{Style.BRIGHT}{'-' * 80}\n{'Menú Cliente'.center(25)}\n{'-' * 80}")
            print("1- Ver Clientes")
            print("2- Ver Medicamentos")
            print("3- Ver Ventas")
            print("4- Salir\n")

            opcion = opcion_medicamentos = excepciones.ingresar_opcion("Seleccione una opción: ",[1, 2, 3, 4])
            print()

            if opcion == 1:
                print("Mostrando clientes...")
                clientes.mostrar_clientes()
            elif opcion == 2:
                print("Mostrando medicamentos...")
                medicamentos.mostrar_medicamentos()
            elif opcion == 3:
                print("Mostrando ventas...")
                ventas.mostrar_ventas()
            elif opcion == 4:
                print("Saliendo del programa.")
            else:
                print(f"{Fore.RED}Opción no válida.")

menu_de_acceso()
# Programa principal
