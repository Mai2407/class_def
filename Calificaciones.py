class CalificacionFinal:

        nombre = ""

        apellido = ""

        plataforma = ""
        
        trabajo_Practico = ""
        
        Actitud_y_Valores = ""
    
        Examen = ""

        validaciones = ""

        def NombreCompleto(self):

            return self.nombre + " " + self.apellido
            
        def valorFinal(self):

            if self.validaciones >= 70:

                validado = 'Aprobado'

            else:

                validado = 'Reprobado'     


            return "nota final: " , self.plataforma + self.trabajo_Practico + self.Actitud_y_Valores + self.Examen, validado