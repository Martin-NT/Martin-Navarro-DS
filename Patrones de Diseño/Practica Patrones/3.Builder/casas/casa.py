class Casa:
    def __init__(self):
        self.habitaciones = 0
        self.baños = 0
        self.piscina = False
        self.jardin = False

    def resumen(self):
        resumen = (
            f"- Habitaciones: {self.habitaciones}\n"
            f"- Baños: {self.baños}\n"
            f"- Jardín: {'Sí' if self.jardin else 'No'}\n"
            f"- Psicina: {'Sí' if self.piscina else 'No'}\n"
        )
        print(resumen)