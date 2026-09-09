import medicamentos
medicamentos.mostrar_medicamentos() 

#if elemento == 5:
              if fila[elemento] == "1":
                    cad = f"|¿Requiere Receta?{'Si':^15} "
                else:   
                    cad = f"|¿Requiere Receta?{'No':^15} "
            elif elemento == 6:
                if fila[elemento] == "1":
                    cad = f"|¿Esta Disponible?{'Si':^15} "
                else:   
                    cad = f"|¿Esta Disponible?{'No':^15} "
            else:
                cad = f"|{elemento:^15} "