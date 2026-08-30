'''
LISTAS
'''
# Listas de clientes
id_cliente = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
nombre_cliente = ["Juan Perez", "Maria Gomez", "Carlos Lopez", "Ana Martinez", "Luis Fernandez", "Sofia Torres", "Diego Ramirez", "Valentina Castro", "Martin Rojas", "Lucia Diaz"]
edad_cliente = [25, 42, 31, 55, 19, 38, 47, 29, 61, 34]
tipo_cobertura = [1, 2, 1, 2, 1, 2, 1, 2, 2, 2]


# Listas de medicamentos
id_medicamento = ["M001", "M002", "M003", "M004", "M005", "M006", "M007", "M008", "M009", "M010"]
nombre_medicamento = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Loratadina", "Omeprazol", "Diclofenac", "Metformina", "Salbutamol", "Enalapril", "Azitromicina"]
precio_medicamento = [1500, 2200, 3500, 1800, 2700, 2500, 4200, 3900, 3100, 4800]
stock_medicamento = [20, 15, 6, 10, 25, 5, 12, 3, 18, 7]
requiere_receta = [2, 2, 1, 2, 2, 1, 1, 1, 1, 1]


# Listas de ventas
id_venta = ["V001", "V002", "V003", "V004", "V005", "V006", "V007", "V008", "V009", "V010"]
id_cliente_venta = ["C001", "C003", "C002", "C001", "C005", "C007", "C003", "C008", "C010", "C005"]
id_medicamento_venta = ["M001", "M003", "M002", "M005", "M007", "M004", "M003", "M010", "M009", "M001"]
cantidad_ventas = [2, 1, 3, 1, 2, 1, 1, 2, 1, 4]
presento_receta = [2, 1, 2, 2, 1, 2, 1, 1, 1, 2]



'''
Función de login
'''
def login(max_intentos):
    usuario_admin = "admin"
    contrasenia_admin = "1234"

    usuario_normal = "usuario"
    contrasenia_normal = "abcd"

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




'''
FUNCIÓN CLIENTE (CRUD)
'''
#? Para agregar un cliente
def alta_cliente():

    print("\n--- AGREGAR CLIENTE ---")
    codigo = input("Ingrese código del cliente: ")

    while codigo in id_cliente:
        print("Error: el cliente ya existe.")
        codigo = input("Ingrese otro código: ")

    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    
    while edad <= 0:
        print("Error: la edad debe ser mayor a 0.")
        edad = int(input("Ingrese edad: "))
    
    cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): "))
    
    while cobertura != 1 and cobertura != 2:
        print ("Tipo de cobertura inválida: Ingrese una de las opciones.")
        cobertura = int(input("Tipo de cobertura (1-Particular / 2-Obra Social): \n"))
    
    id_cliente.append(codigo)
    nombre_cliente.append(nombre)
    edad_cliente.append(edad)
    tipo_cobertura.append(cobertura)

    print("Cliente agregado correctamente.")



# Para modificar un cliente
def modificar_cliente():

    print("\n--- MODIFICAR CLIENTE ---")
    codigo = input("Ingrese código del cliente: ")
    posicion = -1

    for i in range(len(id_cliente)): #busca la posicion del cliente
        if id_cliente[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Cliente no encontrado.")
        return

    nombre_cliente[posicion] = input("Nuevo nombre: ")
    edad_cliente[posicion] = int(input("Nueva edad: "))
    
    while edad_cliente[posicion] <= 0:
        print("Error: la edad debe ser mayor a 0.")
        edad_cliente[posicion] = int(input("Ingrese una nueva edad: "))
        
    tipo_cobertura[posicion] = int(input("Nueva cobertura (1-Particular / 2-Obra Social): "))
    
    while tipo_cobertura[posicion] != 1 and tipo_cobertura[posicion] != 2:
        print("Tipo de cobertura inválida: Ingrese una de las opciones.")
        tipo_cobertura[posicion] = int(input("Nueva cobertura (1-Particular / 2-Obra Social): "))

    print("Cliente modificado correctamente.")
    


# Para eliminar un cliente
def eliminar_cliente():

    print("\n--- ELIMINAR CLIENTE ---")
    codigo = input("Ingrese código del cliente: ")
    posicion = -1

    for i in range(len(id_cliente)):
        if id_cliente[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Cliente no encontrado.")
        return
    
    for i in range(len(id_cliente_venta)):  # Verifica que el cliente no tenga ventas
        if id_cliente_venta[i] == codigo:
            print("No se puede eliminar, el cliente tiene ventas registradas.")
            return
        
    id_cliente.pop(posicion)
    nombre_cliente.pop(posicion)
    edad_cliente.pop(posicion)
    tipo_cobertura.pop(posicion)

    print("Cliente eliminado correctamente.")
    


# Para mostrar lista clientes
def mostrar_clientes():
    ordenamiento_seleccion_clientes()

    print("\n--- LISTADO DE CLIENTES ORDENADOS POR EDAD ---\n")

    for i in range(len(id_cliente)):

        print("Código:", id_cliente[i])
        print("Nombre:", nombre_cliente[i])
        print("Edad:", edad_cliente[i])
        
        if tipo_cobertura[i] == 1:
            print("Cobertura: Particular")
        else:
            print("Cobertura: Obra Social\n")

        print("----------------------")



'''
ORDENAMIENTO DE CLIENTES
'''
def ordenamiento_seleccion_clientes():

    for destinoDelMayor in range(len(edad_cliente) - 1, 0, -1):
        posicDelMayor = 0

        for posElem in range(1, destinoDelMayor + 1):

            if edad_cliente[posElem] > edad_cliente[posicDelMayor]:
                posicDelMayor = posElem

        edad_cliente[posicDelMayor], edad_cliente[destinoDelMayor] = edad_cliente[destinoDelMayor], edad_cliente[posicDelMayor]
        id_cliente[posicDelMayor], id_cliente[destinoDelMayor] = id_cliente[destinoDelMayor], id_cliente[posicDelMayor]
        nombre_cliente[posicDelMayor], nombre_cliente[destinoDelMayor] = nombre_cliente[destinoDelMayor], nombre_cliente[posicDelMayor]
        tipo_cobertura[posicDelMayor], tipo_cobertura[destinoDelMayor] = tipo_cobertura[destinoDelMayor], tipo_cobertura[posicDelMayor]



'''
BUSQUEDA DE CLIENTES
'''
def buscar_clientes():
    
    num = 0
    
    while num != 4:
        print()
        print("¿Que tipo de cliente busca?")
        print("1- Por edad")
        print("2- Según su tipo de cobertura")
        print("3- Por código de cliente")
        print("4- Volver \n")
        
        num = int(input("Ingrese el número: "))
        
        if num == 1:
            ordenamiento_seleccion_clientes()
            edad = int(input("Ingrese la edad a buscar: "))
            print()
            izq = 0
            der = len(edad_cliente) - 1
            pos = -1
            
            while izq <= der and pos == -1:
                medio = (izq + der) // 2
                if edad_cliente[medio] == edad:
                    pos = medio
                elif edad_cliente[medio] < edad:
                    izq = medio + 1
                else:
                    der = medio - 1
                    
            posiciones = []
            if pos != -1:
                i = pos
                while i >= 0 and edad_cliente[i] == edad:    
                    i = i - 1
                i = i + 1                                   
                while i < len(edad_cliente) and edad_cliente[i] == edad: 
                    posiciones.append(i)
                    i = i + 1
                    
            if len(posiciones) > 0:
                posi = 0
                while posi != len(posiciones):
                    print("Cliente:", nombre_cliente[posiciones[posi]], "- ID:", id_cliente[posiciones[posi]])
                    posi = posi + 1
                print()
            else:
                print("No existen clientes con esa edad.")
             
    
        elif num == 2:
            print("1- Particular")
            print("2- Obra Social")
            cober = int(input("Ingrese la cobertura a buscar: "))
            while cober != 1 and cober != 2:
                print("El número ingresado no es válido")
                cober = int(input("Ingrese la cobertura a buscar: "))
            print()
            posiciones = []
            pos = 0
            cant_cober = len(tipo_cobertura)
            while pos < cant_cober:
                if tipo_cobertura[pos] == cober:
                    posiciones.append(pos)
                pos = pos + 1
            posi = 0
            while posi != len(posiciones):
                print("Cliente:", nombre_cliente[posiciones[posi]], "- ID:", id_cliente[posiciones[posi]])
                posi = posi + 1
            print()
           
        
        elif num == 3:
            codi_cliente = input("Ingrese el código del cliente a buscar: ")
            posiciones = []
            pos = 0
            cant_codi = len(id_cliente)
            while pos < cant_codi:
                if id_cliente[pos] == codi_cliente:
                    posiciones.append(pos)
                pos = pos + 1
            if len(posiciones) > 0:
                print("Cliente:", nombre_cliente[posiciones[0]], "- Edad:", edad_cliente[posiciones[0]])
            else:
                print("No existe ningun cliente con ese ID.")
            print()
            
        elif num == 4:
            print("Volviendo...")
    
    
        else:
            print("El numero no es válido.")
            num = int(input("¿Qué tipo de cliente se  busca? "))






'''
FUNCIÓN MEDICAMENTOS (CRUD)
'''
# Para agregar un medicamento
def alta_medicamento():

    print("\n--- AGREGAR MEDICAMENTO ---\n")
    codigo = input("Ingrese el código del medicamento: ")

    while codigo in id_medicamento:
        print("Error: el medicamento ya existe.")
        codigo = input("Ingrese otro código: ")

    nombre = input("Ingrese el nombre: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese el stock: "))
    receta = int(input("Requiere receta (1- Si / 2- No): "))

    id_medicamento.append(codigo)
    nombre_medicamento.append(nombre)
    precio_medicamento.append(precio)
    stock_medicamento.append(stock)
    requiere_receta.append(receta)

    print("Medicamento agregado correctamente.\n")


# Para modificar un medicamento
def modificar_medicamento():

    print("\n--- MODIFICAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(id_medicamento)): #busca la posicion del medicamento
        if id_medicamento[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    nombre_medicamento[posicion] = input("Nuevo medicamento: ")
    precio_medicamento[posicion] = int(input("Nuevo precio: "))
    stock_medicamento[posicion] = int(input("Nuevo stock: "))
    requiere_receta[posicion] = int(input("Requiere receta? (1-Si / 2-No): "))

    print("Medicamento modificado correctamente.")
    
    

# Para eliminar un medicamento
def eliminar_medicamento():

    print("\n--- ELIMINAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(id_medicamento)):
        if id_medicamento[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    for i in range(len(id_medicamento_venta)): # Verifica que el medicamento no este asociado a una venta.
        if id_medicamento_venta[i] == codigo:
            print("No se puede eliminar, el medicamento tiene ventas asociadas.")
            return

    id_medicamento.pop(posicion)
    nombre_medicamento.pop(posicion)
    precio_medicamento.pop(posicion)
    stock_medicamento.pop(posicion)
    requiere_receta.pop(posicion)

    print("Medicamento eliminado correctamente.")



# Para mostrar lista medicamentos
def mostrar_medicamentos():
    ordenamiento_insercion_medicamentos()

    print("\n--- LISTADO DE MEDICAMENTOS ORDENADOS POR PRECIO ---\n")

    for i in range(len(id_medicamento)):

        print("Código:", id_medicamento[i])
        print("Nombre:", nombre_medicamento[i])
        print("Precio:", precio_medicamento[i])
        print("Stock:", stock_medicamento[i])
        
        if requiere_receta[i] == 1:
            print("Requiere receta: Si.")
        else:
            print("Requiere receta: No\n")

        print("--------------------")



'''
Ordenamiento Medicamentos
'''
def ordenamiento_insercion_medicamentos():

    for posActual in range(1, len(precio_medicamento)):

        precio = precio_medicamento[posActual]
        codigo = id_medicamento[posActual]
        nombre = nombre_medicamento[posActual]
        stock = stock_medicamento[posActual]
        receta = requiere_receta[posActual]

        posElem = posActual

        while posElem > 0 and precio_medicamento[posElem - 1] > precio:

            precio_medicamento[posElem] = precio_medicamento[posElem - 1]
            id_medicamento[posElem] = id_medicamento[posElem - 1]
            nombre_medicamento[posElem] = nombre_medicamento[posElem - 1]
            stock_medicamento[posElem] = stock_medicamento[posElem - 1]
            requiere_receta[posElem] = requiere_receta[posElem - 1]

            posElem = posElem - 1

        precio_medicamento[posElem] = precio
        id_medicamento[posElem] = codigo
        nombre_medicamento[posElem] = nombre
        stock_medicamento[posElem] = stock
        requiere_receta[posElem] = receta



'''
FUNCION VENTAS (CRUD)
'''
# Para agregar una venta
def alta_venta():

    print("\n--- AGREGAR VENTA ---")
    codigo = input("Ingrese código de venta: ")

    while codigo in id_venta:
        print("Error: La venta ya existe.")
        codigo = input("Ingrese otro código: ")

    cliente = input("Ingrese el código del cliente: ")
    
    while cliente not in id_cliente:
        print("Error: Cliente inexistente.")
        cliente = input("Ingrese el código del cliente: ")
        
    medicamento = input("Ingrese el código del medicamento: ")
    
    while medicamento not in id_medicamento:
        print("Error: Medicamento inexistente.")
        medicamento = input("Ingrese el código del medicamento: ")

    ventas = int(input("Ingrese la cantidad de ventas: "))
    
    while ventas <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
        ventas = int(input("Ingrese la cantidad de ventas: "))
        
    receta = int(input("¿Presentó receta? (1-Si / 2-No): "))
    

    permitido = 1  # 1= la venta se puede realizar, 0= la venta no se permite

    for i in range(len(id_medicamento)):
        if id_medicamento[i] == medicamento:

            if requiere_receta[i] == 1 and receta == 2:  #Para revisar si la receta es obligatoria y no se presento
                print("Error: Este medicamento requiere receta.")
                permitido = 0

    if permitido == 1:
        id_venta.append(codigo)
        id_cliente_venta.append(cliente)
        id_medicamento_venta.append(medicamento)
        cantidad_ventas.append(ventas)
        presento_receta.append(receta)

        print("Venta agregada correctamente.")



# Para modificar una venta
def modificar_venta():

    print("\n--- MODIFICAR VENTA ---")
    codigo = input("Ingrese código de venta: ")
    posicion = -1

    for i in range(len(id_venta)):
        if id_venta[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    cliente = input("Nuevo código de cliente: ")

    while cliente not in id_cliente:
        print("Error: Cliente inexistente.")
        cliente = input("Nuevo código de cliente: ")

    medicamento = input("Nuevo código de medicamento: ")

    while medicamento not in id_medicamento:
        print("Error: Medicamento inexistente.")
        medicamento = input("Nuevo código de medicamento: ")

    receta = int(input("¿Presentó receta? (1-Si / 2-No)"))
    
    while receta != 1 and receta != 2:
        print("Error: Ingrese una de las opciones.")
        receta = int(input("¿Presentó receta? (1-Si / 2-No): "))
        
    cantidad = int(input("Ingrese nueva cantidad vendida: "))
    while cantidad <= 0:
        print("Error: la cantidad debe ser mayor a 0.")
    
    permitido = 1
    
    for i in range(len(id_medicamento)):
        if id_medicamento[i] == medicamento:
            if requiere_receta[i] == 1 and receta == 2:
                print("Error: Este medicamento requiere receta.")
                permitido = 0

    if permitido == 0:
        return


    id_cliente_venta[posicion] = cliente
    id_medicamento_venta[posicion] = medicamento
    cantidad_ventas[posicion] = cantidad
    presento_receta[posicion] = receta

    print("Venta modificada correctamente.")



# Para eliminar una venta
def eliminar_venta():

    print("\n--- ELIMINAR VENTA ---")
    codigo = input("Ingrese código de la venta: ")
    posicion = -1

    for i in range(len(id_venta)):
        if id_venta[i] == codigo:
            posicion = i

    if posicion == -1:
        print("Venta no encontrada.")
        return

    id_venta.pop(posicion)
    id_cliente_venta.pop(posicion)
    id_medicamento_venta.pop(posicion)
    cantidad_ventas.pop(posicion)
    presento_receta.pop(posicion)

    print("Venta eliminada correctamente.")



# Para mostrar lista de ventas
def mostrar_ventas():
    ordenamiento_intercambio_ventas()

    print("\n--- LISTADO DE VENTAS ORDENADAS POR CANTIDAD---")

    for i in range(len(id_cliente_venta)):

        print("Código venta:", id_venta[i])
        print("Código cliente:", id_cliente_venta[i])
        print("Código medicamento:", id_medicamento_venta[i])
        print("Cantidad de ventas:", cantidad_ventas[i])
        
        if presento_receta[i] == 1:
            print("Presento receta: Si")
        else:
            print("Presento receta: No\n")

        print("----------------------")



'''
Ordenamiento Ventas
'''
def ordenamiento_intercambio_ventas():

    for comparaciones in range(len(cantidad_ventas) - 1, 0, -1):

        for posElem in range(comparaciones):
            if cantidad_ventas[posElem] > cantidad_ventas[posElem + 1]:

                cantidad_ventas[posElem], cantidad_ventas[posElem + 1] = cantidad_ventas[posElem + 1], cantidad_ventas[posElem]
                id_venta[posElem], id_venta[posElem + 1] = id_venta[posElem + 1], id_venta[posElem]
                id_cliente_venta[posElem], id_cliente_venta[posElem + 1] = id_cliente_venta[posElem + 1], id_cliente_venta[posElem]
                id_medicamento_venta[posElem], id_medicamento_venta[posElem + 1] = id_medicamento_venta[posElem + 1], id_medicamento_venta[posElem]
                presento_receta[posElem], presento_receta[posElem + 1] = presento_receta[posElem + 1], presento_receta[posElem]



'''
SUBMENUS
'''
# Submenu clientes
def submenu_clientes():
    opcion_clientes = ""

    while opcion_clientes != "6":

        print("\n--- CLIENTES ---")
        print("1- Agregar cliente")
        print("2- Modificar cliente")
        print("3- Eliminar cliente")
        print("4- Mostrar cliente")
        print("5- Buscar cliente")
        print("6- Volver.\n")

        opcion_clientes = input("Seleccione una opción: ")

        if opcion_clientes == "1":
            alta_cliente()
        elif opcion_clientes == "2":
            modificar_cliente()
        elif opcion_clientes == "3":
            eliminar_cliente()
        elif opcion_clientes == "4":
            mostrar_clientes()
        elif opcion_clientes == "5":
            buscar_clientes()
        elif opcion_clientes == "6":
            print("Volviendo al menú principal. \n")
        else:
            print("Opción inválida.")


# Submenu medicamentos
def submenu_medicamentos():
    opcion_medicamentos = ""

    while opcion_medicamentos != "5":

        print("\n--- MEDICAMENTOS ---")
        print("1- Crear medicamento")
        print("2- Modificar medicamento")
        print("3- Eliminar medicamento")
        print("4- Mostrar medicamentos")
        print("5- Volver. \n")

        opcion_medicamentos = input("Seleccione una opción: ")

        if opcion_medicamentos == "1":
            alta_medicamento()
        elif opcion_medicamentos == "2":
            modificar_medicamento()
        elif opcion_medicamentos == "3":
            eliminar_medicamento()
        elif opcion_medicamentos == "4":
            mostrar_medicamentos()
        elif opcion_medicamentos == "5":
            print("Volviendo al menú principal.\n")
        else:
            print("Opción inválida.")
            


# Submenu de ventas
def submenu_ventas():
    opcion_ventas = ""

    while opcion_ventas != "5":

        print("\n--- VENTAS ---")
        print("1- Crear venta")
        print("2- Modificar venta")
        print("3- Eliminar venta")
        print("4- Mostrar ventas")
        print("5- Volver.\n")

        opcion_ventas = input("Seleccione una opción: ")

        if opcion_ventas == "1":
            alta_venta()
        elif opcion_ventas == "2":
            modificar_venta()
        elif opcion_ventas == "3":
            eliminar_venta()
        elif opcion_ventas == "4":
            mostrar_ventas()
        elif opcion_ventas == "5":
            print("Volviendo al menú principal.\n")
        else:
            print("Opción inválida.")



#Submenú de Estadisticas
def matriz_estadisticas():

    matriz = [
        [0, 0],  # Particular
        [0, 0]   # Obra Social
    ]

    for i in range(len(id_venta)):

        # buscar posición del cliente
        posicion_cliente = -1

        for i_cliente in range(len(id_cliente)):
            if id_cliente[i_cliente] == id_cliente_venta[i]:
                posicion_cliente = i_cliente

        # fila = cobertura 
        fila = tipo_cobertura[posicion_cliente] - 1

        # columna = receta 
        columna = presento_receta[i] - 1

        matriz[fila][columna] += 1

    return matriz


def mostrar_estadistica(matriz):

    print("\nVENTAS POR COBERTURA Y RECETA\n")

    print("              Con receta   Sin receta")
    print("Particular    ", matriz[0][0], "          ", matriz[0][1])
    print("Obra Social   ", matriz[1][0], "          ", matriz[1][1])
        


'''
MENÚ PRINCIPAL
'''
def mostrar_menu(tipo_usuario):

    if tipo_usuario == "admin":
        
        opcion = ""

        while opcion != "5":
            print("\n----------------------- \nMenú Principal\n-----------------------")
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
                matriz = matriz_estadisticas()
                mostrar_estadistica(matriz)
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
                print("Mostrando clientes...")

            elif opcion == "2":
                print("Mostrando medicamentos...")

            elif opcion == "3":
                print("Mostrando ventas...")

            elif opcion == "4":
                print("Saliendo del programa.")

            else:
                print("Opción no válida.")

    else:
        print("Acceso denegado.")

    


# Programa principal
tipo_usuario = login(3)
mostrar_menu(tipo_usuario)
