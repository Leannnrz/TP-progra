# Importacion de módulos.
from colorama import init, Fore, Back, Style
from CRUD import clientes, medicamentos, ventas, estadisticas
import re

init(autoreset=True) # Inicialización de colorama

'''
Función de login
'''
def login(max_intentos):
    usuario_admin = "admin"
    contrasenia_admin = "1234"

    usuario_normal = "usuario"
    contrasenia_normal = "4321"

    intentos = 0

    while intentos < max_intentos:
        usuario = input("Ingrese el usuario: ").lower()
        contrasenia = input("Ingrese la contraseña: ")

        if usuario == usuario_admin and contrasenia == contrasenia_admin:
            print(f"{Fore.GREEN}¡Login exitoso!")
            print("Ingresó como administrador.\n")
            return usuario_admin

        elif usuario == usuario_normal and contrasenia == contrasenia_normal:
            print(f"{Fore.GREEN}¡Login exitoso!")
            print("Ingresó como usuario.\n")
            return usuario_normal

        else:
            intentos += 1
            print(f"{Fore.RED}Usuario o contraseña incorrectos.")
            print("Intentos restantes:", max_intentos - intentos)
            print()

    print("Ha superado el límite de intentos.")
    return


'''
SUBMENÚS
'''
# Submenú clientes
def submenu_clientes():
    opcion_clientes = ""

    while opcion_clientes != "5":

        print(f"{Fore.CYAN}{'CLIENTES'.center(25)}\n{'-' * 25}")
        print("1- Agregar cliente")
        print("2- Modificar cliente")
        print("3- Eliminar cliente")
        print("4- Mostrar cliente")
        print("5- Volver.\n")

        opcion_clientes = input("Seleccione una opción: ")
        print()

        if opcion_clientes == "1":
            clientes.alta_cliente()
        elif opcion_clientes == "2":
            clientes.modificar_cliente()
        elif opcion_clientes == "3":
            clientes.eliminar_cliente()
        elif opcion_clientes == "4":
            clientes.mostrar_clientes()
        elif opcion_clientes == "5":
            print("Volviendo al menú principal... \n")
        else:
            print(f"{Fore.RED}Opción no válida.")


# Submenú medicamentos
def submenu_medicamentos():
    opcion_medicamentos = ""

    while opcion_medicamentos != "5":

        print(f"{Fore.CYAN}{'MEDICAMENTOS'.center(25)}\n{'-' * 25}")        
        print("1- Crear medicamento")
        print("2- Modificar medicamento")
        print("3- Eliminar medicamento")
        print("4- Mostrar medicamentos")
        print("5- Volver. \n")

        opcion_medicamentos = input("Seleccione una opción: ")
        print()

        if opcion_medicamentos == "1":
            medicamentos.alta_medicamento()
        elif opcion_medicamentos == "2":
            medicamentos.modificar_medicamento()
        elif opcion_medicamentos == "3":
            medicamentos.eliminar_medicamento()
        elif opcion_medicamentos == "4":
            medicamentos.mostrar_medicamentos()
        elif opcion_medicamentos == "5":
            print("Volviendo al menú principal.\n")
        else:
            print(f"{Fore.RED}Opción no válida.")


# Submenú de ventas
def submenu_ventas():
    opcion_ventas = ""

    while opcion_ventas != "6":

        print(f"{Fore.CYAN}{'VENTAS'.center(20)}\n{'-' * 20}")
        print("1- Crear venta")
        print("2- Modificar venta")
        print("3- Eliminar venta")
        print("4- Mostrar ventas")
        print("5- Buscar venta")
        print("6- Volver.\n")

        opcion_ventas = input("Seleccione una opción: ")
        print()

        if opcion_ventas == "1":
            ventas.alta_venta()
        elif opcion_ventas == "2":
            ventas.modificar_venta()
        elif opcion_ventas == "3":
            ventas.eliminar_venta()
        elif opcion_ventas == "4":
            ventas.mostrar_ventas()
        elif opcion_ventas == "5":
            ventas.buscar_venta()
        elif opcion_ventas == "6":
            print("Volviendo al menú principal.\n")
        else:
            print(f"{Fore.RED}Opción no válida.")

#Submenú de Estadisticas
def submenu_estadisticas(): 
    opcion_estadisticas = ""

    while opcion_estadisticas != "6":

        print(f"{Fore.CYAN}{'VENTAS'.center(20)}\n{'-' * 20}")
        print("1- Ganancia Total")
        print("2- Venta Más Grande")
        print("3- Venta Más Pequeña")
        print("4- Medicamento Más Vendido")
        print("5- Buscar Ganancias por Medicamento")  
        print("6- Ver Estadisticas de Clientes")  
        print("7- Volver.\n")

        opcion_estadisticas = input("Seleccione una opción: ")

        if opcion_estadisticas == "1":
            estadisticas.total_recaudado()
        elif opcion_estadisticas == "2":
            estadisticas.mayor_venta()
        elif opcion_estadisticas == "3":
            estadisticas.menor_venta()
        elif opcion_estadisticas == "4":
            estadisticas.med_mas_vendido()
        elif opcion_estadisticas == "5":
            estadisticas.ganancia_x_medicamento()
        elif opcion_estadisticas == "6":
            estadisticas.stats_clientes()
        elif opcion_estadisticas == "7":
            print("Volviendo al menú principal.\n")
        else:
            print(f"{Fore.RED}Opción no válida.")



'''
MENÚ PRINCIPAL
'''
def mostrar_menu(tipo_usuario):

    if tipo_usuario == "admin":
        opcion = ""

        while opcion != "5":
            print(f"{Fore.BLUE}{Style.BRIGHT}{'-' * 25}\n{'Menú Principal'.center(25)}\n{'-' * 25}")
            print(f"{Fore.BLUE}{Style.BRIGHT}\n1- Clientes")
            print(f"{Fore.BLUE}{Style.BRIGHT}2- Medicamentos")
            print(f"{Fore.BLUE}{Style.BRIGHT}3- Ventas")
            print(f"{Fore.BLUE}{Style.BRIGHT}4- Estadísticas")
            print(f"{Fore.BLUE}{Style.BRIGHT}5- Salir\n")

            opcion = input("Seleccione una opción: ")
            print()

            if opcion == "1":
                submenu_clientes()
            elif opcion == "2":
                submenu_medicamentos()
            elif opcion == "3":
                submenu_ventas()
            elif opcion == "4":
                ...
            elif opcion == "5":
                print("Saliendo del programa.")
            else:
                print(f"{Fore.RED}Opción no válida.")

    elif tipo_usuario == "usuario":
        opcion = ""

        while opcion != "4":
            print("\n-----------------------")
            print("Menú Usuario")
            print("-----------------------")
            print("1- Ver Clientes")
            print("2- Ver Medicamentos")
            print("3- Ver Ventas")
            print("4- Salir\n")

            opcion = input("Seleccione una opción: ")
            print()

            if opcion == "1":
                print("Mostrando clientes...")
            elif opcion == "2":
                print("Mostrando medicamentos...")
            elif opcion == "3":
                print("Mostrando ventas...")
            elif opcion == "4":
                print("Saliendo del programa.")
            else:
                print(f"{Fore.RED}Opción no válida.")

    else:
        print(f"{Fore.RED}Acceso denegado.")




# Programa principal
tipo_usuario = login(3)
mostrar_menu(tipo_usuario)