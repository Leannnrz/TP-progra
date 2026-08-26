# Listas de clientes
id_cliente = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
nombre_cliente = ["Juan Perez", "Maria Gomez", "Carlos Lopez", "Ana Martinez", "Luis Fernandez", "Sofia Torres", "Diego Ramirez", "Valentina Castro", "Martin Rojas", "Lucia Diaz"]
edad_cliente = [25, 42, 31, 55, 19, 38, 47, 29, 61, 34]
tipo_cobertura = [1, 2, 1, 2, 1, 2, 1, 1, 2, 2]

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

#FUNCION PARA CLACULAR EL COSTO TOTAL DE CADA MEDICAMENTO
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

#FUNCION PARA VERIFICAR LA DISPONIBILIDAD DE CADA MEDICAMENTO
def verificar_disponibilidad(cantidad):
    if cantidad > 0:
        disponibilidad = "Si"
    else:
        disponibilidad = "No"

    return disponibilidad 

#FUNCION PARA MOSTRAR CADA REPORTE
def mostrar_reporte(i):
    nombre = nombre_medicamento[i]
    cantidad = stock_medicamento[i]
    precio = precio_medicamento[i]
    total = calcular_total(precio, cantidad)
    disponibilidad = verificar_disponibilidad(cantidad)

    print(nombre.ljust(20), str(cantidad).rjust(17), f"${precio:.2f}".rjust(20), f"${total:.2f}".rjust(20), disponibilidad.rjust(12))

print("PRODUCTO".ljust(20), "CANTIDAD".rjust(20), "PRECIO".rjust(16), "TOTAL".rjust(19), "DISPONIBILIDAD".rjust(20))
print("-" * 100)
for i in range(len(nombre_medicamento)):
    mostrar_reporte(i)


