


nombre = input("Introducir nombre del estudiante: ")

plataforma = float(input("Introduce el valor de la calificaccion de la plataforma :"))

trabajo_Practico = float(input("Introduce el valor de la calificaccion del trabajo practico :"))

Actitud_y_Valores = float(input("Introduce el valor de la calificaccion de las actidudes y valores :"))

Examen =  float(input("Introduce el valor de la calificaccion del examen :"))

calificacion = plataforma + trabajo_Practico + Actitud_y_Valores + Examen

if calificacion >= 90:

        nota = str(calificacion)

        calificacion = "A"

        validacion = 'aprobo'

        print("La calificavion final de   es: " + nota + "  " + calificacion + "  " + validacion)
    
elif calificacion >= 80:
        
        nota = str(calificacion)

        calificacion = "B"

        validacion = 'aprobo'

        print("La calificavion final de   es: " + nota + "  " + calificacion + "  " + validacion)
    
elif calificacion >= 70:
        
        nota = str(calificacion)

        calificacion = "C"

        validacion = 'aprobo'

        print("La calificavion final de   es: " + nota + "  " + calificacion + "  " + validacion)
    
elif calificacion <= 69:

        nota = str(calificacion)
    
        calificacion = "F"

        validacion = 'reprobo'

        print("La calificavion final de   es: " + nota + "  " + calificacion + "  " + validacion)
    
else:
    
     print("intentalo de nuevo")

