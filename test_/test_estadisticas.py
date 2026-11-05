

from CRUD.estadisticas import (
    calcular_total,
    verificar_disponibilidad,
    medicamentos_con_receta,
    valor_total_stock,
    ventas_con_receta,
    cantidad_total_vendida,
    calcular_importes_ventas,
    promedio_general_ventas,
    promedio_ventas_con_receta,
    promedio_ventas_sin_receta
)


def test_calcular_total():
    # Probamos calcular el total correctamente.
    assert calcular_total(100, 2) == 200
    assert calcular_total(50, 3) == 150

    # Probamos cuando la cantidad es cero.
    assert calcular_total(100, 0) == 0


def test_verificar_disponibilidad():
    # Probamos cuando hay medicamentos disponibles.
    assert verificar_disponibilidad(10) == "Si"
    assert verificar_disponibilidad(1) == "Si"

    # Probamos cuando no hay medicamentos disponibles.
    assert verificar_disponibilidad(0) == "No"


def test_medicamentos_con_receta():
    # Creamos una matriz de medicamentos de prueba.
    matriz_medicamentos = [
        ["M001", "Paracetamol", "Lab1", 100.0, 20, 1],
        ["M002", "Ibuprofeno", "Lab2", 200.0, 15, 2],
        ["M003", "Amoxicilina", "Lab3", 300.0, 10, 1]
    ]

    # Probamos que filtre solamente medicamentos con receta.
    resultado = medicamentos_con_receta(matriz_medicamentos)

    assert resultado == [
        ["M001", "Paracetamol", "Lab1", 100.0, 20, 1],
        ["M003", "Amoxicilina", "Lab3", 300.0, 10, 1]
    ]

    # Probamos cuando no hay medicamentos con receta.
    matriz_sin_receta = [
        ["M002", "Ibuprofeno", "Lab2", 200.0, 15, 2]
    ]

    assert medicamentos_con_receta(matriz_sin_receta) == []


def test_valor_total_stock():
    # Creamos una matriz de medicamentos de prueba.
    matriz_medicamentos = [
        ["M001", "Paracetamol", "Lab1", 100.0, 20, 1],
        ["M002", "Ibuprofeno", "Lab2", 200.0, 15, 2]
    ]

    # Probamos calcular el valor total del stock.
    assert valor_total_stock(matriz_medicamentos) == 5000

    # Probamos cuando la matriz está vacía.
    assert valor_total_stock([]) == 0


def test_ventas_con_receta():
    # Creamos una matriz de ventas de prueba.
    matriz_ventas = [
        ["V001", "C001", "M001", 2, 1],
        ["V002", "C002", "M002", 3, 2],
        ["V003", "C003", "M003", 1, 1]
    ]

    # Probamos que filtre solamente ventas con receta.
    resultado = ventas_con_receta(matriz_ventas)

    assert resultado == [
        ["V001", "C001", "M001", 2, 1],
        ["V003", "C003", "M003", 1, 1]
    ]

    # Probamos cuando no hay ventas con receta.
    matriz_sin_receta = [
        ["V002", "C002", "M002", 3, 2]
    ]

    assert ventas_con_receta(matriz_sin_receta) == []


def test_cantidad_total_vendida():
    # Creamos una matriz de ventas de prueba.
    matriz_ventas = [
        ["V001", "C001", "M001", 2, 1],
        ["V002", "C002", "M002", 3, 2],
        ["V003", "C003", "M003", 5, 1]
    ]

    # Probamos calcular la cantidad total vendida.
    assert cantidad_total_vendida(matriz_ventas) == 10

    # Probamos cuando no hay ventas.
    assert cantidad_total_vendida([]) == 0


def test_calcular_importes_ventas(monkeypatch):
    # Creamos una matriz de medicamentos de prueba.
    matriz_medicamentos = [
        ["M001", "Paracetamol", "Lab1", 100.0, 20, 1],
        ["M002", "Ibuprofeno", "Lab2", 200.0, 15, 2]
    ]

    # Creamos una matriz de ventas de prueba.
    ventas_prueba = [
        ["V001", "C001", "M001", 2, 1],
        ["V002", "C002", "M002", 3, 2]
    ]

    # Reemplazamos los datos originales por los datos de prueba.
    import CRUD.estadisticas as estadisticas

    monkeypatch.setattr(
        estadisticas,
        "convertir_a_matriz",
        lambda: matriz_medicamentos
    )

    monkeypatch.setattr(
        estadisticas,
        "matriz_ventas",
        ventas_prueba
    )

    # Probamos calcular los importes de cada venta.
    assert estadisticas.calcular_importes_ventas() == [200.0, 600.0]


def test_promedio_general_ventas(monkeypatch):
    # Creamos importes de ventas de prueba.
    import CRUD.estadisticas as estadisticas

    monkeypatch.setattr(
        estadisticas,
        "calcular_importes_ventas",
        lambda: [200.0, 600.0, 400.0]
    )

    # Probamos calcular el promedio general.
    assert estadisticas.promedio_general_ventas() == 400.0

    # Probamos cuando no hay ventas.
    monkeypatch.setattr(
        estadisticas,
        "calcular_importes_ventas",
        lambda: []
    )

    assert estadisticas.promedio_general_ventas() == 0


def test_promedio_ventas_con_receta(monkeypatch):
    # Creamos ventas de prueba.
    import CRUD.estadisticas as estadisticas

    ventas_prueba = [
        ["V001", "C001", "M001", 2, 1],
        ["V002", "C002", "M002", 3, 2],
        ["V003", "C003", "M003", 1, 1]
    ]

    monkeypatch.setattr(
        estadisticas,
        "matriz_ventas",
        ventas_prueba
    )

    monkeypatch.setattr(
        estadisticas,
        "calcular_importes_ventas",
        lambda: [200.0, 600.0, 300.0]
    )

    # Probamos el promedio de ventas con receta.
    assert estadisticas.promedio_ventas_con_receta() == 250.0


def test_promedio_ventas_sin_receta(monkeypatch):
    # Creamos ventas de prueba.
    import CRUD.estadisticas as estadisticas

    ventas_prueba = [
        ["V001", "C001", "M001", 2, 1],
        ["V002", "C002", "M002", 3, 2],
        ["V003", "C003", "M003", 1, 2]
    ]

    monkeypatch.setattr(
        estadisticas,
        "matriz_ventas",
        ventas_prueba
    )

    monkeypatch.setattr(
        estadisticas,
        "calcular_importes_ventas",
        lambda: [200.0, 600.0, 300.0]
    )

    # Probamos el promedio de ventas sin receta.
    assert estadisticas.promedio_ventas_sin_receta() == 450.0
