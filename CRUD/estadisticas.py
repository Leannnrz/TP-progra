from .medicamentos import matriz_medicamentos
from .clientes import matriz_clientes
from .ventas import matriz_ventas

'''
FUNCIONES CRUD DE PROMEDIOS
'''
#Funcion Para Calcular El Total Recaudado
def total_recaudado():
    lista_cant_productos = []
    for i in range(len(matriz_ventas)):
        lista_cant_productos.append(matriz_ventas[i][3])

    lista_medicamentos_vendidos = []
    for j in range(len(matriz_ventas)):
        lista_medicamentos_vendidos.append(matriz_ventas[j][2]) 

    lista_id_medicamentos = []
    lista_precios_medicamento = []
    for h in range(len(matriz_medicamentos)): 
        lista_id_medicamentos.append(matriz_medicamentos[h][0])
        lista_precios_medicamento.append(matriz_medicamentos[h][3])

    lista_precio_indiv_med = []
    for k in range(len(lista_medicamentos_vendidos)):
        precio_med = lista_id_medicamentos.index(lista_medicamentos_vendidos[k])
        lista_precio_indiv_med.append(lista_precios_medicamento[precio_med])

    total_recaudado_x_venta = []
    for l in range(len(lista_precio_indiv_med)):
        ganancia_venta = lista_precio_indiv_med[l] * lista_cant_productos[l]
        total_recaudado_x_venta.append(ganancia_venta)

    ganancia_total = sum(total_recaudado_x_venta)
    ganancia_final = "$"+str(ganancia_total)

    ancho_total = 122
    print("\n---- LISTADO DE GANANCIA POR VENTAS ----\n")
    print("-" * ancho_total)
    print(f'{"Código de Venta":<25}{"Código de Medicamento Vendido":<30}{"Cantidad Vendida":>25}{"Ganancia Total Por Venta:":>35}')
    print("-" * ancho_total)
    
    for p in range(len(total_recaudado_x_venta)):
        print(f'{" ":<5}{matriz_ventas[p][0]:<32}{lista_medicamentos_vendidos[p]:<35}{lista_cant_productos[p]:<28}${total_recaudado_x_venta[p]:>}')
    print("-" * ancho_total)
    print(" "*82,"Ganancia Total: ",ganancia_final)
    print()

#Funcion Para Conocer la Mayor Venta
def mayor_venta():
    lista_cant_productos = []
    for i in range(len(matriz_ventas)):
        lista_cant_productos.append(matriz_ventas[i][3])
    
    lista_medicamentos_vendidos = []
    for j in range(len(matriz_ventas)):
        lista_medicamentos_vendidos.append(matriz_ventas[j][2]) 
    
    lista_id_medicamentos = []
    lista_precios_medicamento = []
    for h in range(len(matriz_medicamentos)): 
        lista_id_medicamentos.append(matriz_medicamentos[h][0])
        lista_precios_medicamento.append(matriz_medicamentos[h][3])
    
    lista_precio_indiv_med = []
    for k in range(len(lista_medicamentos_vendidos)):
        precio_med = lista_id_medicamentos.index(lista_medicamentos_vendidos[k])
        lista_precio_indiv_med.append(lista_precios_medicamento[precio_med])
    
    total_recaudado_x_venta = []
    for l in range(len(lista_precio_indiv_med)):
        ganancia_venta = lista_precio_indiv_med[l] * lista_cant_productos[l]
        total_recaudado_x_venta.append(ganancia_venta)

    venta_mas_grande = max(total_recaudado_x_venta)
    pos_v = total_recaudado_x_venta.index(venta_mas_grande)

    print("-" * 100)
    print("La Venta Mayor Registrada: ")
    print(" "*4, "-Id de Venta: ", matriz_ventas[pos_v][0])
    print(" "*4, "-Id de Cliente: ", matriz_ventas[pos_v][1])
    print(" "*4, "-Id de Medicamento: ", matriz_ventas[pos_v][2])
    print(" "*4, "-Cantidad Vendida: ", matriz_ventas[pos_v][3])
    print(" "*4, "-Ganancia de Venta: ", "$",venta_mas_grande)
    print("-" * 100)
    print()

#Funcion Para Conocer la Menor Venta 
def menor_venta():
    lista_cant_productos = []
    for i in range(len(matriz_ventas)):
        lista_cant_productos.append(matriz_ventas[i][3])
        
    lista_medicamentos_vendidos = []
    for j in range(len(matriz_ventas)):
            lista_medicamentos_vendidos.append(matriz_ventas[j][2]) 
        
    lista_id_medicamentos = []
    lista_precios_medicamento = []
    for h in range(len(matriz_medicamentos)): 
        lista_id_medicamentos.append(matriz_medicamentos[h][0])
        lista_precios_medicamento.append(matriz_medicamentos[h][3])
        
    lista_precio_indiv_med = []
    for k in range(len(lista_medicamentos_vendidos)):
        precio_med = lista_id_medicamentos.index(lista_medicamentos_vendidos[k])
        lista_precio_indiv_med.append(lista_precios_medicamento[precio_med])
        
    total_recaudado_x_venta = []
    for l in range(len(lista_precio_indiv_med)):
        ganancia_venta = lista_precio_indiv_med[l] * lista_cant_productos[l]
        total_recaudado_x_venta.append(ganancia_venta)
    
    venta_mas_grande = min(total_recaudado_x_venta)
    pos_v = total_recaudado_x_venta.index(venta_mas_grande)
    
    print("-" * 100)
    print("La Venta Menor Registrada: ")
    print(" "*4, "-Id de Venta: ", matriz_ventas[pos_v][0])
    print(" "*4, "-Id de Cliente: ", matriz_ventas[pos_v][1])
    print(" "*4, "-Id de Medicamento: ", matriz_ventas[pos_v][2])
    print(" "*4, "-Cantidad Vendida: ", matriz_ventas[pos_v][3])
    print(" "*4, "-Ganancia de Venta: ", "$",venta_mas_grande)
    print("-" * 100)
    print()

#Funcion Para Conocer el Medicamento Mas Vendido
def med_mas_vendido():
    lista_cant_productos = []
    for i in range(len(matriz_ventas)):
        lista_cant_productos.append(matriz_ventas[i][3])
        
    lista_medicamentos_vendidos = []
    for j in range(len(matriz_ventas)):
            lista_medicamentos_vendidos.append(matriz_ventas[j][2]) 
        
    lista_id_medicamentos = []
    lista_precios_medicamento = []
    for h in range(len(matriz_medicamentos)): 
        lista_id_medicamentos.append(matriz_medicamentos[h][0])
        lista_precios_medicamento.append(matriz_medicamentos[h][3])
        
    lista_precio_indiv_med = []
    for k in range(len(lista_medicamentos_vendidos)):
        precio_med = lista_id_medicamentos.index(lista_medicamentos_vendidos[k])
        lista_precio_indiv_med.append(lista_precios_medicamento[precio_med])
        
    total_recaudado_x_venta = []
    for l in range(len(lista_precio_indiv_med)):
        ganancia_venta = lista_precio_indiv_med[l] * lista_cant_productos[l]
        total_recaudado_x_venta.append(ganancia_venta)  

    lista_aparaciones_med = []
    for o in range(len(lista_id_medicamentos)):
        cant_apariciones = lista_medicamentos_vendidos.count(lista_id_medicamentos[o])
        lista_aparaciones_med.append(cant_apariciones)
    
    med_mas_aparariciones = max(lista_aparaciones_med)
    pos_m = lista_aparaciones_med.index(med_mas_aparariciones)

    print("Medicamento con más Ventas:")
    print("ID Medicamento: ", matriz_medicamentos[pos_m][0])
    print("Nombre Medicamento: ", matriz_medicamentos[pos_m][1])
    print()

                    
    lista_cod_medicamentos = []
    pos = 0
    for i in range(len(matriz_ventas)):
        if matriz_medicamentos[pos_m][0] == matriz_ventas[i][2]:
            lista_cod_medicamentos.append(pos)
        pos = pos + 1 
    
    ancho_total = 122
    print("\n---- LISTADO DE VENTAS RELACIONADAS AL MEDICAMENTO",matriz_medicamentos[pos_m][1],"---\n")
    print("-" * ancho_total)
    print(f'{"Código de Venta":<25}{"Código de Cliente":<25}{"Código de Medicamento":<30}{"Cantidad Vendida":>15}{"¿Presentó Receta?":>25}')
    print("-" * ancho_total)
    for j in lista_cod_medicamentos:
        receta = lambda x: "Si" if x == 1 else "No"           
        print(f'{" ":<5}{matriz_ventas[j][0]:<25}{matriz_ventas[j][1]:<25}{matriz_ventas[j][2]:<25}{matriz_ventas[j][3]:>9}{receta(matriz_ventas[j][4]):>25}')
    print("-" * ancho_total)
    print() 

#Funcion Para Conocer las Ganancias de los Medicamentos
def ganancia_x_medicamento():
    lista_cant_productos = []
    for i in range(len(matriz_ventas)):
        lista_cant_productos.append(matriz_ventas[i][3])
        
    lista_medicamentos_vendidos = []
    for j in range(len(matriz_ventas)):
            lista_medicamentos_vendidos.append(matriz_ventas[j][2]) 
        
    lista_id_medicamentos = []
    lista_precios_medicamento = []
    for h in range(len(matriz_medicamentos)): 
        lista_id_medicamentos.append(matriz_medicamentos[h][0])
        lista_precios_medicamento.append(matriz_medicamentos[h][3])
        
    lista_precio_indiv_med = []
    for k in range(len(lista_medicamentos_vendidos)):
        precio_med = lista_id_medicamentos.index(lista_medicamentos_vendidos[k])
        lista_precio_indiv_med.append(lista_precios_medicamento[precio_med])
        
    med_a_buscar = input("Ingrese el Codigo del Medicamento: ")
    pos_m = lista_id_medicamentos.index(med_a_buscar)
    print()
    print("-" * 122)
    print("Medicamento a Buscar:")
    print("Nombre Medicamento: ", matriz_medicamentos[pos_m][1])
    print("Precio Medicamento: $",lista_precios_medicamento[pos_m])
    print("-" * 122)

    total_recaudado_x_venta = []
    for s in range(len(lista_precio_indiv_med)):
        if med_a_buscar == lista_medicamentos_vendidos[s]:
            ganancia_venta = lista_precio_indiv_med[pos_m] * lista_cant_productos[s]
            total_recaudado_x_venta.append(ganancia_venta)  

    recaudacion_total = sum(total_recaudado_x_venta)
    recaudacion_total_formal = "$"+str(recaudacion_total)
    
    lista_cod_medicamentos = []
    pos = 0
    for i in range(len(matriz_ventas)):
        if med_a_buscar == matriz_ventas[i][2]:
            lista_cod_medicamentos.append(pos)
        pos = pos + 1 
    
    ancho_total = 122
    print("\n---- LISTADO DE VENTAS RELACIONADAS AL MEDICAMENTO",matriz_medicamentos[pos_m][1],"---\n")
    print("-" * ancho_total)
    print(f'{"Código de Venta":<25}{"Código de Cliente":<25}{"Código de Medicamento":<30}{"Cantidad Vendida":>15}{"¿Presentó Receta?":>25}')
    print("-" * ancho_total)
    for j in lista_cod_medicamentos:
        receta = lambda x: "Si" if x == 1 else "No"           
        print(f'{" ":<5}{matriz_ventas[j][0]:<25}{matriz_ventas[j][1]:<25}{matriz_ventas[j][2]:<25}{matriz_ventas[j][3]:>9}{receta(matriz_ventas[j][4]):>25}')
    print("-" * ancho_total)
    print("Ganancias Totales del Medicamento: ",recaudacion_total_formal)
    print("-" * ancho_total)
    print()     
