
# Importamos las funciones
from FUNCIONES.validaciones import (
    validar_codigo_cliente,
    validar_codigo_medicamento,
    validar_codigo_venta,
    buscar_texto,
    encontrar_coincidencias
)


def test_validar_codigo_cliente():
    # Probamos códigos correctos.
    assert validar_codigo_cliente("C123") == True
    assert validar_codigo_cliente("C001") == True

    # Probamos códigos incorrectos.
    assert validar_codigo_cliente("A123") == False
    assert validar_codigo_cliente("C12") == False
    assert validar_codigo_cliente("C1234") == False
    assert validar_codigo_cliente("c123") == False


def test_validar_codigo_medicamento():
    # Probamos códigos correctos.
    assert validar_codigo_medicamento("M123") == True
    assert validar_codigo_medicamento("M001") == True

    # Probamos códigos incorrectos.
    assert validar_codigo_medicamento("A123") == False
    assert validar_codigo_medicamento("M12") == False
    assert validar_codigo_medicamento("M1234") == False
    assert validar_codigo_medicamento("m123") == False


def test_validar_codigo_venta():
    # Probamos códigos correctos.
    assert validar_codigo_venta("V123") == True
    assert validar_codigo_venta("V001") == True

    # Probamos códigos incorrectos.
    assert validar_codigo_venta("A123") == False
    assert validar_codigo_venta("V12") == False
    assert validar_codigo_venta("V1234") == False
    assert validar_codigo_venta("v123") == False


def test_buscar_texto():
    # Probamos una búsqueda que encuentra coincidencias.
    assert buscar_texto("Paracetamol", "Para") is not None

    # La búsqueda no distingue entre mayúsculas y minúsculas.
    assert buscar_texto("Paracetamol", "para") is not None

    # Probamos un texto que no existe.
    assert buscar_texto("Paracetamol", "Ibuprofeno") == None

    # También probamos una búsqueda dentro de otra palabra.
    assert buscar_texto("Medicamento", "camento") is not None


def test_encontrar_coincidencias():
    # Probamos encontrar varias coincidencias.
    assert encontrar_coincidencias("ana ana juan", "ana") == ["ana", "ana"]

    # La búsqueda no distingue entre mayúsculas y minúsculas.
    assert encontrar_coincidencias("Ana ANA ana", "ana") == ["Ana", "ANA", "ana"]

    # Probamos cuando no existen coincidencias.
    assert encontrar_coincidencias("Paracetamol", "Ibuprofeno") == []

    # Probamos cuando hay una sola coincidencia.
    assert encontrar_coincidencias("Hola mundo", "Hola") == ["Hola"]
