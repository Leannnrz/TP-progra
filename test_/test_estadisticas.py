
from CRUD.estadisticas import (
    calcular_importes_ventas,
    promedio_general_ventas,
    mayor_importe_venta,
    menor_importe_venta,
    ventas_con_receta,
    ventas_sin_receta,
    contar_ventas_por_receta,
    porcentaje_ventas_receta,
    promedio_por_presentacion,
    medicamentos_con_receta,
    valor_total_stock,
    cantidad_total_vendida
)


# MATRICES DE PRUEBA

medicamentos = [
    ["M001", "Paracetamol", "Lab A", 100.0, 10, 1],
    ["M002", "Ibuprofeno", "Lab B", 50.0, 20, 2]
]

ventas = [
    ["V001", "C001", "M001", 2, 1],
    ["V002", "C002", "M002", 3, 0],
    ["V003", "C003", "M001", 1, 0]
]


def test_calcular_importes_ventas():
    # Probamos el cálculo de los importes de cada venta.
    assert calcular_importes_ventas(ventas, medicamentos) == [200.0, 150.0, 100.0]

    # Probamos cuando no existen ventas.
    assert calcular_importes_ventas([], medicamentos) == []


def test_promedio_general_ventas():
    # Probamos el promedio de varias ventas.
    assert promedio_general_ventas([200, 150, 100]) == 150

    # Probamos una lista con un solo elemento.
    assert promedio_general_ventas([80]) == 80

    # Probamos cuando no existen ventas.
    assert promedio_general_ventas([]) == 0


def test_mayor_importe_venta():
    # Probamos encontrar el importe máximo.
    assert mayor_importe_venta([200, 150, 100]) == 200

    # Probamos una lista con un solo elemento.
    assert mayor_importe_venta([80]) == 80


def test_menor_importe_venta():
    # Probamos encontrar el importe mínimo.
    assert menor_importe_venta([200, 150, 100]) == 100

    # Probamos una lista con un solo elemento.
    assert menor_importe_venta([80]) == 80


def test_ventas_con_receta():
    # Probamos filtrar las ventas que presentaron receta.
    resultado = ventas_con_receta(ventas)

    assert resultado == [
        ["V001", "C001", "M001", 2, 1]
    ]

    # Probamos cuando no existen ventas.
    assert ventas_con_receta([]) == []


def test_ventas_sin_receta():
    # Probamos filtrar las ventas que no presentaron receta.
    resultado = ventas_sin_receta(ventas)

    assert resultado == [
        ["V002", "C002", "M002", 3, 0],
        ["V003", "C003", "M001", 1, 0]
    ]

    # Probamos cuando no existen ventas.
    assert ventas_sin_receta([]) == []


def test_contar_ventas_por_receta():
    # Probamos contar las ventas con receta.
    assert contar_ventas_por_receta(ventas, 1) == 1

    # Probamos contar las ventas sin receta.
    assert contar_ventas_por_receta(ventas, 0) == 2

    # Probamos una categoría sin registros.
    assert contar_ventas_por_receta(ventas, 2) == 0


def test_porcentaje_ventas_receta():
    # Probamos calcular el porcentaje de ventas con receta.
    assert porcentaje_ventas_receta(ventas) == 100 / 3

    # Probamos cuando no existen ventas.
    assert porcentaje_ventas_receta([]) == 0


def test_promedio_por_presentacion():
    # Calculamos los importes de las ventas.
    importes = calcular_importes_ventas(ventas, medicamentos)

    # Probamos el promedio de ventas con receta.
    assert promedio_por_presentacion(importes, ventas, 1) == 200

    # Probamos el promedio de ventas sin receta.
    assert promedio_por_presentacion(importes, ventas, 0) == 125

    # Probamos una categoría sin ventas.
    assert promedio_por_presentacion(importes, ventas, 2) == 0


def test_medicamentos_con_receta():
    # Probamos filtrar medicamentos que requieren receta.
    resultado = medicamentos_con_receta(medicamentos)

    assert resultado == [
        ["M001", "Paracetamol", "Lab A", 100.0, 10, 1]
    ]

    # Probamos cuando no existen medicamentos.
    assert medicamentos_con_receta([]) == []


def test_valor_total_stock():
    # Probamos calcular el valor total del stock.
    assert valor_total_stock(medicamentos) == 2000

    # Probamos cuando no existen medicamentos.
    assert valor_total_stock([]) == 0


def test_cantidad_total_vendida():
    # Probamos sumar las cantidades vendidas.
    assert cantidad_total_vendida(ventas) == 6

    # Probamos cuando no existen ventas.
    assert cantidad_total_vendida([]) == 0
