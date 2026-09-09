# MATRIZ CLIENTES
clientes = [
    ["C001", "Juan Perez", 25, 1],
    ["C002", "Maria Gomez", 42, 2],
    ["C003", "Carlos Lopez", 31, 1],
    ["C004", "Ana Martinez", 55, 2],
    ["C005", "Luis Fernandez", 19, 1],
    ["C006", "Sofia Torres", 38, 2],
    ["C007", "Diego Ramirez", 47, 1],
    ["C008", "Valentina Castro", 29, 1],
    ["C009", "Martin Rojas", 61, 2],
    ["C010", "Lucia Diaz", 34, 2]
]

# MATRIZ MEDICAMENTOS
medicamentos = [
    ["M001", "Paracetamol", 1500, 20, 2],
    ["M002", "Ibuprofeno", 2200, 15, 2],
    ["M003", "Amoxicilina", 3500, 6, 1],
    ["M004", "Loratadina", 1800, 10, 2],
    ["M005", "Omeprazol", 2700, 25, 2],
    ["M006", "Diclofenac", 2500, 5, 1],
    ["M007", "Metformina", 4200, 12, 1],
    ["M008", "Salbutamol", 3900, 3, 1],
    ["M009", "Enalapril", 3100, 18, 1],
    ["M010", "Azitromicina", 4800, 7, 1]
]
#MATRIZ VENTAS
ventas = [
    ["V001", "C001", "M001", 2, 2],
    ["V002", "C003", "M003", 1, 1],
    ["V003", "C002", "M002", 3, 2],
    ["V004", "C001", "M005", 1, 2],
    ["V005", "C005", "M007", 2, 1],
    ["V006", "C007", "M004", 1, 2],
    ["V007", "C003", "M003", 1, 1],
    ["V008", "C008", "M010", 2, 1],
    ["V009", "C010", "M009", 1, 1],
    ["V010", "C005", "M001", 4, 2]
]
#FUNCION PARA CALCULAR EL COSTO TOTAL DE CADA MEDICAMENTO
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
    nombre = medicamentos[i][1]
    cantidad = medicamentos[i][3]
    precio = medicamentos[i][2]
    total = calcular_total(precio, cantidad)
    disponibilidad = verificar_disponibilidad(cantidad)

    print(nombre.ljust(20), str(cantidad).rjust(17), f"${precio:.2f}".rjust(20), f"${total:.2f}".rjust(20), disponibilidad.rjust(12))

print("PRODUCTO".ljust(20), "CANTIDAD".rjust(20), "PRECIO".rjust(16), "TOTAL".rjust(19), "DISPONIBILIDAD".rjust(20))
print("-" * 100)
for i in range(len(medicamentos)):
    mostrar_reporte(i)


