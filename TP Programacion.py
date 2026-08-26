# Listas de clientes
id_cliente = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
nombre_cliente = ["Juan Perez", "Maria Gomez", "Carlos Lopez", "Ana Martinez", "Luis Fernandez", "Sofia Torres", "Diego Ramirez", "Valentina Castro", "Martin Rojas", "Lucia Diaz"]
edad_cliente = [25, 42, 31, 55, 19, 38, 47, 29, 61, 34]
tipo_cobertura = [1, 2, 1, 2, 1, 2, 1, 1, 2, 2]

# Listas de medicamentos
id_medicamento = ["M001", "M002", "M003", "M004", "M005", "M006", "M007", "M008", "M009", "M010"]
nombre_medicamento = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Loratadina", "Omeprazol", "Diclofenac", "Metformina", "Salbutamol", "Enalapril", "Azitromicina"]
descripcion_medicamento = ["Analgésico y antipirético indicado para aliviar dolores leves a moderados como cefaleas o molestias musculares y reducir la fiebre. Actúa inhibiendo la síntesis de prostaglandinas en el sistema nervioso central. Destaca por su buen perfil de tolerancia gástrica cuando se administra dentro de las dosis terapéuticas recomendadas.", "Antiinflamatorio no esteroideo con propiedades analgésicas y antipiréticas. Está indicado para tratar dolores de origen inflamatorio, artritis y cuadros febriles. Actúa mediante la inhibición de la enzima ciclooxigenasa, reduciendo la producción de prostaglandinas responsables de la respuesta inflamatoria y el dolor en el tejido afectado.", "Antibiótico de amplio espectro perteneciente al grupo de las penicilinas. Actúa interfiriendo en la síntesis de la pared celular bacteriana, lo que provoca la lisis del microorganismo. Se utiliza frecuentemente para tratar infecciones respiratorias, otitis, sinusitis y afecciones cutáneas provocadas por diversas cepas bacterianas sensibles al fármaco.", "Antihistamínico de segunda generación diseñado para aliviar síntomas alérgicos como rinitis, estornudos y urticaria. Inhibe de manera selectiva los receptores periféricos de la histamina. Al cruzar en mínima cantidad la barrera hematoencefálica, genera una frecuencia de somnolencia significativamente menor en comparación con los antihistamínicos clásicos de primera generación.", "Inhibidor de la bomba de protones que disminuye la secreción de ácido en el estómago. Bloquea el sistema enzimático hidrógeno-potasio ATPasa en las células parietales gástricas. Se prescribe habitualmente para el tratamiento del reflujo gastroesofágico, la gastritis, las úlceras pépticas y la prevención de lesiones causadas por fármacos irritantes.", "Antiinflamatorio no esteroideo potente indicado para aliviar el dolor, la inflamación y la hinchazón en patologías osteoarticulares como artritis o gota, así como en traumatismos musculares. Funciona bloqueando la enzima ciclooxigenasa, disminuyendo la síntesis de prostaglandinas en el sitio exacto donde se genera el proceso inflamatorio agudo.", "Antidiabético oral perteneciente a la familia de las biguanidas, considerado de primera línea para la diabetes tipo 2. Su mecanismo principal consiste en reducir la producción hepática de glucosa y mejorar la sensibilidad a la insulina en los tejidos periféricos, favoreciendo el control glucémico de manera sostenida sin provocar hipoglucemia.", "Broncodilatador agonista selectivo de los receptores beta-2 adrenérgicos en el músculo liso bronquial. Produce una rápida relajación de las vías respiratorias en cuestión de minutos, siendo un pilar clave en el alivio inmediato y prevención de broncoespasmos asociados al asma y a la enfermedad pulmonar obstructiva crónica.", "Inhibidor de la enzima convertidora de angiotensina utilizado en la hipertensión arterial y la insuficiencia cardíaca. Bloquea la formación de angiotensina II, favoreciendo la dilatación de los vasos sanguíneos, reduciendo la resistencia vascular periférica y disminuyendo notablemente el esfuerzo que requiere el corazón para bombear la sangre.", "Antibiótico macrólido que inhibe la síntesis de proteínas bacterianas al unirse a la subunidad ribosómica 50S. Posee un espectro amplio contra bacterias grampositivas y gramnegativas. Gracias a su prolongada vida media tisular, permite esquemas de dosificación más cortos para tratar infecciones respiratorias, amigdalitis y enfermedades de transmisión sexual."]
precio_medicamento = [1500, 2200, 3500, 1800, 2700, 2500, 4200, 3900, 3100, 4800]
stock_medicamento = [20, 15, 6, 10, 25, 5, 12, 3, 18, 7]
requiere_receta = [2, 2, 1, 2, 2, 1, 1, 1, 1, 1]
disponibilidad_medicamento = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1]

for i in range(len(id_medicamento)):
    reporte_medicamentos = f"Medicamento: {nombre_medicamento[i]} | Precio: ${precio_medicamento[i]}"
    reporte_medicamentos_dos = f"Descripción: {descripcion_medicamento[i][1:100]}..." 
    if disponibilidad_medicamento[i] == 1:
        dispo_med = "Sí"
    else:
        dispo_med = "No"
    reporte_medicamentos_tres = f"Stock: {stock_medicamento[i]} | Disponible: {dispo_med}"
    print(reporte_medicamentos) 
    print(reporte_medicamentos_dos) 
    print(reporte_medicamentos_tres) 
    print( ) 