#Matriz de Medicamentos 
matriz_medicamentos = [
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

def mostrar_medicamentos():
    for fila in matriz_medicamentos:
        print("-" * 175) 
        for elemento in range(len(fila)):
            if elemento == 0:
                cad = f"| Código de Medicamento:{fila[elemento]:^15} "
            elif elemento == 1:
                cad = f"| Nombre de Medicamento:{fila[elemento]:^15} "
            elif elemento == 2:
                cad = f"| Descripción de Medicamento:{fila[elemento]:^15} " [:75] + "..."
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
            
            print(cad, end="|")
            print()
        print()
        print("-" * 175) 
        print() 

