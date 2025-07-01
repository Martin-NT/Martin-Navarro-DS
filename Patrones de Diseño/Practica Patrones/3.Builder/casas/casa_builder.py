from casa import Casa

class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def set_habitaciones(self, habitaciones):
        self.casa.habitaciones = habitaciones

    def set_baños(self, baños):
        self.casa.baños = baños

    def set_piscina(self, piscina):
        self.casa.piscina = piscina

    def set_jardin(self, jardin):
        self.casa.jardin = jardin

    def build(self):
        casa_final = self.casa
        self.casa = Casa()  # Reiniciar el builder para nuevas construcciones
        return casa_final