
'''
MODULO DE MANEJO DE EXCEPCIONES
Funciones auxiliares para controlar errores de ingreso.
'''

# INGRESAR UN NUMERO ENTERO POSITIVO

def ingresar_entero_positivo(msj):
    valido = False

    while valido == False:
        try:
            numero = int(input(msj))

            if numero > 0:
                valido = True
            else:
                print("Error: el número debe ser mayor a cero.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return numero


# INGRESAR UNA OPCION PERMITIDA

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



# INGRESAR UN NUMERO ENTERO NO NEGATIVO

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
