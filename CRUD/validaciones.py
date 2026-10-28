import re

# VALIDAR CÓDIGO DE CLIENTE

def validar_codigo_cliente(codigo):

    patron = r"^C[0-9]{3}$"

    resultado = re.search(patron, codigo)

    if resultado:
        return True
    else:
        return False


# VALIDAR CÓDIGO DE MEDICAMENTO

def validar_codigo_medicamento(codigo):

    patron = r"^M[0-9]{3}$"

    resultado = re.search(patron, codigo)

    if resultado:
        return True
    else:
        return False


# BUSCAR TEXTO EN UN NOMBRE

def buscar_texto(texto, busqueda):

    patron = re.escape(busqueda)

    resultado = re.search(patron, texto, re.IGNORECASE)

    if resultado:
        return resultado
    else:
        return None


# OBTENER TODAS LAS COINCIDENCIAS

def encontrar_coincidencias(texto, busqueda):

    patron = re.escape(busqueda)

    resultados = re.findall(patron, texto, re.IGNORECASE)

    return resultados