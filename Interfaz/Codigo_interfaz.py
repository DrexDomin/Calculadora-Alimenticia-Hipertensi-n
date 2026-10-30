import tkinter as tk
from tkinter import ttk, messagebox

from Usuario.Codigo_usuario import Usuario
from CalculadoraHPT.Codigo_sistema import CalculadoraHPT


class Interfaz:

    def __init__(self):

        self.calculadora = CalculadoraHPT()

        self.ventana = tk.Tk()

        self.ventana.title(
            "Calculadora Alimenticia - Hipertension"
        )

        self.ventana.geometry("550x650")

        self.crear_interfaz()

    def crear_interfaz(self):

        marco = ttk.Frame(self.ventana, padding=20)

        marco.pack(fill="both", expand=True)

        titulo = ttk.Label(
            marco,
            text="Calculadora Alimenticia para Hipertension",
            font=("Arial", 15, "bold")
        )

        titulo.pack(pady=10)

        self.nombre = self.crear_campo(
            marco, "Nombre:"
        )

        self.peso = self.crear_campo(
            marco, "Peso en kg:"
        )

        self.altura = self.crear_campo(
            marco, "Altura en metros:"
        )

        self.sistolica = self.crear_campo(
            marco, "Presion sistolica:"
        )

        self.diastolica = self.crear_campo(
            marco, "Presion diastolica:"
        )

        self.sodio = self.crear_campo(
            marco, "Consumo diario de sodio (mg):"
        )

        boton = ttk.Button(
            marco,
            text="CALCULAR",
            command=self.calcular
        )

        boton.pack(pady=15)

        self.resultado = tk.Text(
            marco,
            height=15,
            width=58,
            state="disabled"
        )

        self.resultado.pack()

        aviso = ttk.Label(
            marco,
            text="Prototipo educativo. No reemplaza "
                 "la valoracion de un profesional de salud.",
            wraplength=480
        )

        aviso.pack(pady=10)

    def crear_campo(self, marco, texto):

        etiqueta = ttk.Label(
            marco,
            text=texto
        )

        etiqueta.pack(anchor="w")

        entrada = ttk.Entry(marco)

        entrada.pack(fill="x", pady=5)

        return entrada

    def calcular(self):

        try:

            nombre = self.nombre.get().strip()

            peso = float(self.peso.get())

            altura = float(self.altura.get())

            sistolica = int(self.sistolica.get())

            diastolica = int(self.diastolica.get())

            sodio = int(self.sodio.get())

            if (peso <= 0 or altura <= 0
                    or sistolica <= 0 or diastolica <= 0
                    or sodio < 0):

                raise ValueError

            paciente = Usuario(
                nombre, peso, altura,
                sistolica, diastolica, sodio
            )

            resultados = self.calculadora.evaluar(
                paciente
            )

            texto = ""

            texto += f"Paciente: {nombre or 'Usuario'}\n"

            texto += (
                f"IMC: {resultados['imc']:.2f}\n"
            )

            texto += (
                f"Clasificacion IMC: "
                f"{resultados['clasificacion_imc']}\n"
            )

            texto += (
                f"Presion arterial: "
                f"{resultados['clasificacion_presion']}\n"
            )

            texto += (
                f"Sodio: "
                f"{resultados['recomendacion_sodio']}\n"
            )

            texto += "\nRECOMENDACIONES:\n"

            for recomendacion in resultados["recomendaciones"]:

                texto += f"- {recomendacion}\n"

            self.resultado.config(state="normal")

            self.resultado.delete("1.0", tk.END)

            self.resultado.insert(tk.END, texto)

            self.resultado.config(state="disabled")

        except ValueError:

            messagebox.showerror(
                "Error",
                "Por favor, ingrese datos numericos validos."
            )

    def ejecutar(self):

        self.ventana.mainloop()