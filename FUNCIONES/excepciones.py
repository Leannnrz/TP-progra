
'''
MODULO DE MANEJO DE EXCEPCIONES
Funciones auxiliares para controlar errores de ingreso.
'''

'''INGRESAR UN NUMERO ENTERO POSITIVO'''

def ingresar_entero_positivo(msj): # msj valor que ingresa el usuario
    valido = False # la variable empiza como false

    while valido == False: # mientras la variable sea falsa entonces se ejecutara el while
        try:
            numero = int(input(msj)) # solicita el dato y lo convierte a entero.

            if numero > 0:
                valido = True   # la variable cambia a true si es numero es mayor a 0
            else:
                print("Error: el número debe ser mayor a cero.") # de no cumplirse la condicion se envia un mensaje

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return numero


'''INGRESAR UNA OPCION PERMITIDA'''

def ingresar_opcion(msj, opciones):
    valido = False

    while valido == False:
        try:
            numero = int(input(msj))

            if numero in opciones:
                valido = True
            else:
                print("Error: seleccione una opción válida.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return numero


def ingresar_texto(msj):
    valido = False

    while valido == False:
        try:
            texto = input(msj)

            if texto.strip() == "":
                raise ValueError("El texto no puede estar vacío.")

            valido = True

        except ValueError as error:
            print(f"Error: {error}")

    return texto.strip()



'''INGRESAR UN NUMERO ENTERO NO NEGATIVO'''

def ingresar_entero_no_negativo(msj):
    valido = False

    while valido == False:
        try:
            numero = int(input(msj))

            if numero >= 0:
                valido = True
            else:
                print("Error: el número no puede ser negativo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return numero


'''MODIFICAR UN TEXTO CONSERVANDO EL VALOR ANTERIOR'''

def ingresar_texto_modificado(msj, valor_actual):
    texto = input(f"{msj} (Enter para mantener): ").strip()

    if texto == "":
        return valor_actual

    return texto


'''MODIFICAR UN NUMERO ENTERO POSITIVO'''

def ingresar_entero_positivo_modificado(msj, valor_actual):
    valido = False

    while valido == False:
        try:
            entrada = input(f"{msj} (Enter para mantener): ").strip()

            if entrada == "":
                return valor_actual

            numero = int(entrada)

            if numero > 0:
                valido = True
            else:
                print("Error: el número debe ser mayor a cero.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return numero


'''MODIFICAR UN NUMERO ENTERO NO NEGATIVO'''

def ingresar_entero_no_negativo_modificado(msj, valor_actual):
    valido = False

    while valido == False:
        try:
            entrada = input(f"{msj} (Enter para mantener): ").strip()

            if entrada == "":
                return valor_actual

            numero = int(entrada)

            if numero >= 0:
                valido = True
            else:
                print("Error: el número no puede ser negativo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return numero


'''INGRESAR UN CODIGO CON FORMATO VALIDO'''

def ingresar_codigo(msj, funcion_validacion, formato):
    valido = False

    while valido == False:
        try:
            codigo = input(msj).strip()

            if codigo == "":
                raise ValueError("El código no puede estar vacío.")

            if funcion_validacion(codigo):
                valido = True
            else:
                print(f"Error: el código debe tener el formato {formato}.")

        except ValueError as error:
            print(f"Error: {error}")

    return codigo