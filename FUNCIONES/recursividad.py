
# ============================================================
# FUNCIONES RECURSIVAS
# TP: Sistema de gestion de ventas y recetas en una farmacia
# ============================================================


# ============================================================
# CLIENTES
# ============================================================

def buscar_cliente_recursivo(lista_clientes, codigo, posicion=0):
    """
    Busca un cliente por su codigo en una lista de diccionarios.
    Devuelve el cliente encontrado o None si no existe.
    """
    if posicion == len(lista_clientes):
        return None

    if lista_clientes[posicion]["ID"] == codigo:
        return lista_clientes[posicion]

    return buscar_cliente_recursivo(
        lista_clientes, codigo, posicion + 1
    )


def crear_matriz_clientes_recursivo(
    lista_clientes, posicion=0, matriz=None
):
    """
    Convierte una lista de diccionarios de clientes en una matriz.
    """
    if matriz is None:
        matriz = []

    if posicion == len(lista_clientes):
        return matriz

    cliente = lista_clientes[posicion]

    fila = [
        cliente["ID"],
        cliente["Nombre"],
        cliente["Edad"],
        cliente["Cobertura"]
    ]

    matriz.append(fila)

    return crear_matriz_clientes_recursivo(
        lista_clientes, posicion + 1, matriz
    )


# ============================================================
# LISTAS Y MATRICES
# ============================================================

def mostrar_lista_recursivo(lista, posicion=0):
    """
    Muestra los elementos de una lista de forma recursiva.
    Puede utilizarse con listas de clientes, medicamentos o ventas
    cuando se desea mostrar cada elemento sin un formato especial.
    """
    if posicion == len(lista):
        return

    print(lista[posicion])

    mostrar_lista_recursivo(lista, posicion + 1)


def sumar_elementos_recursivo(lista, posicion=0):
    """
    Suma los elementos numericos de una lista.
    """
    if posicion == len(lista):
        return 0

    return lista[posicion] + sumar_elementos_recursivo(
        lista, posicion + 1
    )


def buscar_por_codigo_recursivo(
    matriz, codigo, indice_codigo=0, posicion=0
):
    """
    Busca una fila de una matriz por el codigo indicado.
    Devuelve la fila encontrada o None si no existe.
    """
    if posicion == len(matriz):
        return None

    if matriz[posicion][indice_codigo] == codigo:
        return matriz[posicion]

    return buscar_por_codigo_recursivo(
        matriz, codigo, indice_codigo, posicion + 1
    )


def contar_fila_recursivo(fila, valor, columna=0):
    """
    Cuenta las apariciones de un valor en una fila.
    """
    if columna == len(fila):
        return 0

    if fila[columna] == valor:
        return 1 + contar_fila_recursivo(
            fila, valor, columna + 1
        )

    return contar_fila_recursivo(
        fila, valor, columna + 1
    )


def contar_matriz_recursivo(matriz, valor, fila=0):
    """
    Cuenta las apariciones de un valor en toda una matriz.
    Utiliza contar_fila_recursivo para analizar cada fila.
    """
    if fila == len(matriz):
        return 0

    apariciones = contar_fila_recursivo(matriz[fila], valor)

    return apariciones + contar_matriz_recursivo(
        matriz, valor, fila + 1
    )


# ============================================================
# CADENAS DE CARACTERES
# ============================================================

def contar_caracter_recursivo(cadena, caracter, posicion=0):
    """
    Cuenta las apariciones exactas de un caracter en una cadena.
    """
    if posicion == len(cadena):
        return 0

    if cadena[posicion] == caracter:
        return 1 + contar_caracter_recursivo(
            cadena, caracter, posicion + 1
        )

    return contar_caracter_recursivo(
        cadena, caracter, posicion + 1
    )


def mostrar_cadena_recursivo(cadena, posicion=0):
    """
    Muestra los caracteres de una cadena, uno por linea.
    """
    if posicion == len(cadena):
        return

    print(cadena[posicion])

    mostrar_cadena_recursivo(cadena, posicion + 1)


# ============================================================
# MEDICAMENTOS ALMACENADOS EN ARCHIVO DE TEXTO
# ============================================================

def buscar_medicamento_recursivo(lineas, codigo, posicion=0):
    """
    Busca un medicamento por codigo en lineas separadas por punto
    y coma. Devuelve sus campos o None si no existe.
    """
    if posicion == len(lineas):
        return None

    campos = lineas[posicion].strip().split(";")

    if len(campos) > 0 and campos[0] == codigo:
        return campos

    return buscar_medicamento_recursivo(
        lineas, codigo, posicion + 1
    )


# ============================================================
# VENTAS
# ============================================================

def filtrar_ventas_por_codigo_recursivo(
    matriz_ventas, codigo, indice_codigo, posicion=0, resultados=None
):
    """
    Devuelve todas las ventas cuyo campo indicado coincide
    con el codigo recibido.
    """
    if resultados is None:
        resultados = []

    if posicion == len(matriz_ventas):
        return resultados

    if matriz_ventas[posicion][indice_codigo] == codigo:
        resultados.append(matriz_ventas[posicion])

    return filtrar_ventas_por_codigo_recursivo(
        matriz_ventas,
        codigo,
        indice_codigo,
        posicion + 1,
        resultados
    )
