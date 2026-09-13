from functools import reduce

# CLIENTES

def clientes_obra_social(matriz): #FILTRAR CLIENTE POR OBRA SOCIAL

    return list(
        filter(lambda cliente: cliente[3] == 2, matriz)
    )


def cantidad_clientes(matriz):

    return reduce(lambda total, cliente: total + 1, matriz, 0)


def cantidad_clientes_obra_social(matriz):

    clientes = clientes_obra_social(matriz)

    return reduce(lambda total, cliente: total + 1, clientes, 0)


# MEDICAMENTOS

def medicamentos_con_receta(matriz): #FILTRAR MEDICAMENTOS QUE REQUIEREN RECETA

    return list(filter(lambda medicamento: medicamento[5] == 1, matriz))


def valor_total_stock(matriz):

    return reduce( lambda total, medicamento: total + medicamento[3] * medicamento[4], matriz, 0)


# VENTAS

def ventas_con_receta(matriz): #FILTRAR VENTAS POR RECETA

    return list(filter(lambda venta: venta[4] == 1, matriz))


def cantidad_total_vendida(matriz):

    return reduce(lambda total, venta: total + venta[3], matriz, 0)


# MOSTRAR ESTADÍSTICAS

def mostrar_clientes_obra_social(matriz):

    clientes = clientes_obra_social(matriz)

    print("\n--- CLIENTES CON OBRA SOCIAL ---")

    if len(clientes) == 0:

        print("No hay clientes con obra social.")

    else:

        for cliente in clientes:

            print(
                cliente[0],
                "-",
                cliente[1],
                "- Edad:",
                cliente[2]
            )


def mostrar_cantidad_clientes(matriz):

    cantidad = cantidad_clientes(matriz)

    print("\n--- CANTIDAD DE CLIENTES ---")
    print("Cantidad total de clientes:", cantidad)


def mostrar_medicamentos_con_receta(matriz):

    medicamentos = medicamentos_con_receta(matriz)

    print("\n--- MEDICAMENTOS QUE REQUIEREN RECETA ---")

    if len(medicamentos) == 0:

        print("No hay medicamentos que requieran receta.")

    else:

        for medicamento in medicamentos:

            print(
                medicamento[0],
                "-",
                medicamento[1],
                "- Laboratorio:",
                medicamento[2]
            )


def mostrar_valor_total_stock(matriz):

    total = valor_total_stock(matriz)

    print("\n--- VALOR TOTAL DEL STOCK ---")
    print("Valor total del stock: $", total)


def mostrar_ventas_con_receta(matriz):

    ventas = ventas_con_receta(matriz)

    print("\n--- VENTAS CON RECETA ---")

    if len(ventas) == 0:

        print("No hay ventas con receta.")

    else:

        for venta in ventas:

            print(
                venta[0],
                "- Cliente:",
                venta[1],
                "- Medicamento:",
                venta[2],
                "- Cantidad:",
                venta[3]
            )


def mostrar_cantidad_total_vendida(matriz):

    cantidad = cantidad_total_vendida(matriz)

    print("\n--- CANTIDAD TOTAL VENDIDA ---")
    print("Cantidad total de medicamentos vendidos:", cantidad)
