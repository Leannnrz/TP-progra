# IMPORTACIÓN DE MÓDULOS

from colorama import init, Fore, Style
from CRUD import clientes, medicamentos, ventas
from FUNCIONES import estadisticas

init(autoreset=True)


# LOGIN

def login(max_intentos):

    usuario_admin = "admin"
    contrasenia_admin = "1234"

    usuario_normal = "usuario"
    contrasenia_normal = "4321"

    intentos = 0

    while intentos < max_intentos:

        usuario = input("Ingrese el usuario: ")
        contrasenia = input("Ingrese la contraseña: ")

        if usuario == usuario_admin and contrasenia == contrasenia_admin:

            print("Login exitoso!")
            print("Ingresó como administrador.\n")

            return usuario_admin

        elif usuario == usuario_normal and contrasenia == contrasenia_normal:

            print("Login exitoso!")
            print("Ingresó como usuario.\n")

            return usuario_normal

        else:

            intentos += 1

            print("Usuario o contraseña incorrectos.")
            print("Intentos restantes:", max_intentos - intentos)

    print("Ha superado el límite de intentos.")

    return None


# SUBMENÚ CLIENTES

def submenu_clientes():

    opcion_clientes = ""

    while opcion_clientes != "6":

        print("\n--- CLIENTES ---")
        print("1- Agregar cliente")
        print("2- Modificar cliente")
        print("3- Eliminar cliente")
        print("4- Mostrar clientes")
        print("5- Mostrar clientes")
        print("6- Volver\n")

        opcion_clientes = input("Seleccione una opción: ")

        if opcion_clientes == "1":

            clientes.alta_cliente()

        elif opcion_clientes == "2":

            clientes.modificar_cliente()

        elif opcion_clientes == "3":

            clientes.eliminar_cliente()

        elif opcion_clientes == "4":

            clientes.mostrar_clientes()

        elif opcion_clientes == "5":
        
            clientes.buscar_clientes()

        elif opcion_clientes == "6":

            print("Volviendo al menú principal.\n")

        else:

            print("Opción inválida.")


# SUBMENÚ MEDICAMENTOS

def submenu_medicamentos():

    opcion_medicamentos = ""

    while opcion_medicamentos != "6":

        print("\n--- MEDICAMENTOS ---")
        print("1- Crear medicamento")
        print("2- Modificar medicamento")
        print("3- Eliminar medicamento")
        print("4- Mostrar medicamentos")
        print("5- Mostrar medicamentos")
        print("6- Volver\n")

        opcion_medicamentos = input("Seleccione una opción: ")

        if opcion_medicamentos == "1":

            medicamentos.alta_medicamento()

        elif opcion_medicamentos == "2":

            medicamentos.modificar_medicamento()

        elif opcion_medicamentos == "3":

            medicamentos.eliminar_medicamento()

        elif opcion_medicamentos == "4":

            medicamentos.mostrar_medicamentos()

        elif opcion_medicamentos == "5":

            medicamentos.buscar_medicamentos()    

        elif opcion_medicamentos == "6":

            print("Volviendo al menú principal.\n")

        else:

            print("Opción inválida.")


# SUBMENÚ VENTAS

def submenu_ventas():

    opcion_ventas = ""

    while opcion_ventas != "5":

        print("\n--- VENTAS ---")
        print("1- Crear venta")
        print("2- Modificar venta")
        print("3- Eliminar venta")
        print("4- Mostrar ventas")
        print("5- Volver\n")

        opcion_ventas = input("Seleccione una opción: ")

        if opcion_ventas == "1":

            ventas.alta_venta()

        elif opcion_ventas == "2":

            ventas.modificar_venta()

        elif opcion_ventas == "3":

            ventas.eliminar_venta()

        elif opcion_ventas == "4":

            ventas.mostrar_ventas()

        elif opcion_ventas == "5":

            print("Volviendo al menú principal.\n")

        else:

            print("Opción inválida.")


# SUBMENÚ ESTADÍSTICAS

def submenu_estadisticas():

    opcion = ""

    while opcion != "7":

        print("\n--- ESTADÍSTICAS ---")
        print("1- Mostrar clientes con obra social")
        print("2- Mostrar cantidad total de clientes")
        print("3- Mostrar medicamentos que requieren receta")
        print("4- Mostrar valor total del stock")
        print("5- Mostrar ventas con receta")
        print("6- Mostrar cantidad total vendida")
        print("7- Volver\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            estadisticas.mostrar_clientes_obra_social(
                clientes.matriz_clientes
            )

        elif opcion == "2":

            estadisticas.mostrar_cantidad_clientes(
                clientes.matriz_clientes
            )

        elif opcion == "3":

            estadisticas.mostrar_medicamentos_con_receta(
                medicamentos.matriz_medicamentos
            )

        elif opcion == "4":

            estadisticas.mostrar_valor_total_stock(
                medicamentos.matriz_medicamentos
            )

        elif opcion == "5":

            estadisticas.mostrar_ventas_con_receta(
                ventas.matriz_ventas
            )

        elif opcion == "6":

            estadisticas.mostrar_cantidad_total_vendida(
                ventas.matriz_ventas
            )

        elif opcion == "7":

            print("Volviendo al menú principal.\n")

        else:

            print("Opción inválida.")


# MENÚ PRINCIPAL

def mostrar_menu(tipo_usuario):

    if tipo_usuario == "admin":

        opcion = ""

        while opcion != "5":

            print(
                f"{Fore.BLUE}{Style.BRIGHT}"
                "\n-----------------------"
                "\nMenú Principal"
                "\n-----------------------"
            )

            print("\n1- Clientes")
            print("2- Medicamentos")
            print("3- Ventas")
            print("4- Estadísticas")
            print("5- Salir\n")

            opcion = input("Seleccione una opción: ")

            print()

            if opcion == "1":

                submenu_clientes()

            elif opcion == "2":

                submenu_medicamentos()

            elif opcion == "3":

                submenu_ventas()

            elif opcion == "4":

                submenu_estadisticas()

            elif opcion == "5":

                print("Saliendo del programa.")

            else:

                print("Opción no válida.")

    elif tipo_usuario == "usuario":

        opcion = ""

        while opcion != "4":

            print("\n-----------------------")
            print("Menú Usuario")
            print("-----------------------")
            print("1- Ver Clientes")
            print("2- Ver Medicamentos")
            print("3- Ver Ventas")
            print("4- Salir")

            opcion = input("\nSeleccione una opción: ")

            print()

            if opcion == "1":

                clientes.mostrar_clientes()

            elif opcion == "2":

                medicamentos.mostrar_medicamentos()

            elif opcion == "3":

                ventas.mostrar_ventas()

            elif opcion == "4":

                print("Saliendo del programa.")

            else:

                print("Opción no válida.")

    else:

        print("Acceso denegado.")


# PROGRAMA PRINCIPAL

tipo_usuario = login(3)

if tipo_usuario is not None:

    mostrar_menu(tipo_usuario)
