# Matriz de medicamentos
matriz_medicamentos = [
    ["M001", "Paracetamol", "Genomma Lab", 1500, 20, 2],
    ["M002", "Ibuprofeno", "Bayer", 2200, 15, 2],
    ["M003", "Amoxicilina", "Roemmers", 3500, 6, 1],
    ["M004", "Loratadina", "Bagó", 1800, 10, 2],
    ["M005", "Omeprazol", "Gador", 2700, 25, 2],
    ["M006", "Diclofenac", "Elea", 2500, 5, 1],
    ["M007", "Metformina", "Montpellier", 4200, 12, 1],
    ["M008", "Salbutamol", "Cassará", 3900, 3, 1],
    ["M009", "Enalapril", "Bernabó", 3100, 18, 1],
    ["M010", "Azitromicina", "Pfizer", 4800, 7, 1]
]


descripcion_medicamentos = [
    ["M001", "Paracetamol", "Analgésico y antipirético indicado para aliviar dolores leves a moderados como cefaleas o molestias musculares y reducir la fiebre. Actúa inhibiendo la síntesis de prostaglandinas en el sistema nervioso central. Destaca por su buen perfil de tolerancia gástrica cuando se administra dentro de las dosis terapéuticas recomendadas.", "$1500", 20, "0", "1"],
    ["M002", "Ibuprofeno", "Antiinflamatorio no esteroideo con propiedades analgésicas y antipiréticas. Está indicado para tratar dolores de origen inflamatorio, artritis y cuadros febriles. Actúa mediante la inhibición de la enzima ciclooxigenasa, reduciendo la producción de prostaglandinas responsables de la respuesta inflamatoria y el dolor en el tejido afectado.", "$2200", 15, "0", "1"],
    ["M003", "Amoxicilina", "Antibiótico de amplio espectro perteneciente al grupo de las penicilinas. Actúa interfiriendo en la síntesis de la pared celular bacteriana, lo que provoca la lisis del microorganismo. Se utiliza frecuentemente para tratar infecciones respiratorias, otitis, sinusitis y afecciones cutáneas provocadas por diversas cepas bacterianas sensibles al fármaco.", "$3500", 6, "1", "1"],
    ["M004", "Loratadina", "Antihistamínico de segunda generación diseñado para aliviar síntomas alérgicos como rinitis, estornudos y urticaria. Inhibe de manera selectiva los receptores periféricos de la histamina. Al cruzar en mínima cantidad la barrera hematoencefálica, genera una frecuencia de somnolencia significativamente menor en comparación con los antihistamínicos clásicos de primera generación.", "$1800", 10, "0", "1"],
    ["M005", "Omeprazol", "Inhibidor de la bomba de protones que disminuye la secreción de ácido en el estómago. Bloquea el sistema enzimático hidrógeno-potasio ATPasa en las células parietales gástricas. Se prescribe habitualmente para el tratamiento del reflujo gastroesofágico, la gastritis, las úlceras pépticas y la prevención de lesiones causadas por fármacos irritantes.", "$2700", 25, "0", "1"],
    ["M006", "Diclofenac", "Antiinflamatorio no esteroideo potente indicado para aliviar el dolor, la inflamación y la hinchazón en patologías osteoarticulares como artritis o gota, así como en traumatismos musculares. Funciona bloqueando la enzima ciclooxigenasa, disminuyendo la síntesis de prostaglandinas en el sitio exacto donde se genera el proceso inflamatorio agudo.", "$2500", 5, "1", "0"],
    ["M007", "Metformina", "Antidiabético oral perteneciente a la familia de las biguanidas, considerado de primera línea para la diabetes tipo 2. Su mecanismo principal consiste en reducir la producción hepática de glucosa y mejorar la sensibilidad a la insulina en los tejidos periféricos, favoreciendo el control glucémico de manera sostenida sin provocar hipoglucemia.", "$4200", 12, "1", "1"],
    ["M008", "Salbutamol", "Broncodilatador agonista selectivo de los receptores beta-2 adrenérgicos en el músculo liso bronquial. Produce una rápida relajación de las vías respiratorias en cuestión de minutos, siendo un pilar clave en el alivio inmediato y prevención de broncoespasmos asociados al asma y a la enfermedad pulmonar obstructiva crónica.", "$3900", 3, "1", "0"],
    ["M009", "Enalapril", "Inhibidor de la enzima convertidora de angiotensina utilizado en la hipertensión arterial y la insuficiencia cardíaca. Bloquea la formación de angiotensina II, favoreciendo la dilatación de los vasos sanguíneos, reduciendo la resistencia vascular periférica y disminuyendo notablemente el esfuerzo que requiere el corazón para bombear la sangre.", "$3100", 18, "1", "1"],
    ["M010", "Azitromicina", "Antibiótico macrólido que inhibe la síntesis de proteínas bacterianas al unirse a la subunidad ribosómica 50S. Posee un espectro amplio contra bacterias grampositivas y gramnegativas. Gracias a su prolongada vida media tisular, permite esquemas de dosificación más cortos para tratar infecciones respiratorias, amigdalitis y enfermedades de transmisión sexual.", "$4800", 7, "1", "1"]
] 



'''
FUNCIONES CRUD DE MEDICAMENTOS
'''
# Para agregar un medicamento
def alta_medicamento():

    print("\n--- AGREGAR MEDICAMENTO ---\n")
    codigo = input("Ingrese el código del medicamento: ")

    cantidad = 0  # No existe el código, si existe se convierte en 1
    
    for fila in matriz_medicamentos:  # Recorremos la fila
        if fila[0] == codigo:         # El primer elemento de la fila es el código
            cantidad = cantidad + 1
    
    while cantidad > 0:
        print("Error: el medicamento ya existe.")
        codigo = input("Ingrese otro código: ")
    
        cantidad = 0
    
        for fila in matriz_medicamentos:
            if fila[0] == codigo:
                cantidad = cantidad + 1

    nombre = input("Ingrese el nombre: ")
    laboratorio = input("Ingrese el laboratorio: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese el stock: "))

    receta = int(input("Requiere receta (1- Si / 2- No): "))
    while receta != 1 and receta != 2:
        print ("Opción inválida: Ingrese una de las opciones.")
        receta = int(input("Requiere receta (1- Si / 2- No): "))

    matriz_medicamentos.append([codigo, nombre, laboratorio, precio, stock, receta])  
    print("Medicamento agregado correctamente.\n")


# Para modificar un medicamento
def modificar_medicamento():

    print("\n--- MODIFICAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(matriz_medicamentos)): #Busca la posicion del medicamento
        if matriz_medicamentos[i][0] == codigo:
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return

    matriz_medicamentos[posicion][1] = input("Ingrese el nuevo nombre del medicamento: ")
    matriz_medicamentos[posicion][2] = int(input("Nuevo precio: "))
    matriz_medicamentos[posicion][3] = int(input("Nuevo stock: "))
    matriz_medicamentos[posicion][4] = int(input("Requiere receta? (1-Si / 2-No): \n"))

    print("Medicamento modificado correctamente.")


# Para eliminar un medicamento
def eliminar_medicamento():

    print("\n--- ELIMINAR MEDICAMENTO ---")
    codigo = input("Ingrese código del medicamento: ")
    posicion = -1

    for i in range(len(matriz_medicamentos)):
        if matriz_medicamentos[i][0] == codigo:   # Busca el código en la columna 0
            posicion = i

    if posicion == -1:
        print("Medicamento no encontrado.")
        return
    '''
    for i in range(len(id_medicamento_venta)): # Verifica que el medicamento no este asociado a una venta.
        if id_medicamento_venta[i] == codigo:
            print("No se puede eliminar, el medicamento tiene ventas asociadas.")
            return'''

    matriz_medicamentos.pop(posicion)
    print("Medicamento eliminado correctamente.")


# Para mostrar lista medicamentos
def mostrar_medicamentos():
    ancho_total = 80
    print("\n---- LISTADO DE MEDICAMENTOS ----\n")
    print(f'{"Código":<8}{"Nombre":<20}{"Laboratorio":<20}{"Precio":>10}{"Stock":>8}{"Receta":>10}')
    print("-" * ancho_total)

    for medicamento in matriz_medicamentos:
        receta = lambda x: "Si" if x == 1 else "No"
        print(f'{medicamento[0]:<8}{medicamento[1]:<20}{medicamento[2]:<20}{medicamento[3]:>10}{medicamento[4]:>8}{receta(medicamento[5]):>10}')

def describir_medicamentos():
    for fila in descripcion_medicamentos:
        print("-" * 175) 
        for elemento in range(len(fila)):
            if elemento == 0:
                cad = f"| Código de Medicamento:{fila[elemento]:^15} "
            elif elemento == 1:
                cad = f"| Nombre de Medicamento:{fila[elemento]:^15} "
            elif elemento == 2:
                cad = f"| Descripción de Medicamento: {fila[elemento]:^15} "[:75] + "..."
            elif elemento == 3:
                cad = f"| Precio de Medicamento:{fila[elemento]:^15} "
            elif elemento == 4:
                cad = f"| Stock de Medicamento:{fila[elemento]:^15} "
            elif elemento == 5:
                if fila[elemento] == 1:
                    cad = f"| ¿Requiere Receta?{'Si':^15} "
                else:   
                    cad = f"| ¿Requiere Receta?{'No':^15} "
            elif elemento == 6:
                if fila[elemento] == 1:
                    cad = f"| ¿Esta Disponible?{'Si':^15} "
                else:   
                    cad = f"| ¿Esta Disponible?{'No':^15} "
            else:
                cad =f"| {fila[elemento]:^15} "[:75] + "..."
            print(f'{cad[0:75]:<90}', end="|")
            print()
        print()
        print("-" * 175) 
        print() 

med = alta_medicamento()
med_2 = modificar_medicamento()