class CalculadoraHPT:

    def calcular_imc(self, usuario):

        imc = usuario.peso / (usuario.altura ** 2)
        return imc

    def clasificar_imc(self, imc):

        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"

    def clasificar_presion(self, usuario):

        sistolica = usuario.sistolica
        diastolica = usuario.diastolica

        if sistolica >= 140 or diastolica >= 90:
            return "Presion arterial alta"
        elif sistolica >= 130 or diastolica >= 80:
            return "Presion arterial elevada"
        else:
            return "Presion arterial dentro del rango normal"

    def recomendacion_sodio(self, usuario):

        if usuario.sodio > 2000:
            return (
                "Reducir el consumo de sodio. "
                "Evitar agregar sal y reducir "
                "alimentos procesados y embutidos."
            )
        else:
            return (
                "Consumo de sodio dentro del "
                "limite orientativo."
            )

    def generar_recomendaciones(self, usuario, imc):

        recomendaciones = []

        if usuario.sodio > 2000:
            recomendaciones.append(
                "Reducir alimentos con alto contenido de sodio."
            )

        if imc >= 25:
            recomendaciones.append(
                "Procurar mantener un peso saludable."
            )

        if usuario.sistolica >= 130 or usuario.diastolica >= 80:
            recomendaciones.append(
                "Priorizar frutas, verduras, legumbres "
                "y cereales integrales."
            )

        if len(recomendaciones) == 0:
            recomendaciones.append(
                "Mantener una alimentacion saludable "
                "y realizar actividad fisica."
            )

        return recomendaciones

    def evaluar(self, usuario):

        imc = self.calcular_imc(usuario)

        clasificacion_imc = self.clasificar_imc(imc)

        clasificacion_presion = self.clasificar_presion(usuario)

        recomendacion_sodio = self.recomendacion_sodio(usuario)

        recomendaciones = self.generar_recomendaciones(
            usuario, imc
        )

        return {
            "imc": imc,
            "clasificacion_imc": clasificacion_imc,
            "clasificacion_presion": clasificacion_presion,
            "recomendacion_sodio": recomendacion_sodio,
            "recomendaciones": recomendaciones
        }
