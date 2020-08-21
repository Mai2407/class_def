from Calificaciones import *

nota = CalificacionFinal()
nota.nombre = input("Introduce el nombre: ")
nota.apellido = input("Introduce el apellido: ")
nota.plataforma = float(input("Introduce el valor de la calificaccion de la plataforma :"))
nota.trabajo_Practico = float(input("Introduce el valor de la calificaccion del trabajo practico :"))
nota.Actitud_y_Valores = float(input("Introduce el valor de la calificaccion de las actidudes y valores :"))
nota.Examen = float(input("Introduce el valor de la calificaccion del examen :"))
nota.validaciones = nota.plataforma + nota.trabajo_Practico + nota.Actitud_y_Valores + nota.Examen


print(nota.NombreCompleto())
print(nota.valorFinal())
