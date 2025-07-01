class Cooperativa:
    def __init__(self):
        self.lotes = []
        self.cereales = []

    def agregar_lote(self, lote):
        self.lotes.append(lote)

    def agregar_cereal(self, cereal):
        self.cereales.append(cereal)

    def sugerir_cereales(self, lote):
        sugerencias = []
        for cereal in self.cereales:
            if cereal.minerales_requeridos.issubset(lote.minerales):
                if cereal.tipo == "Pastura" and not lote.puede_sembrar_pastura():
                    continue
                sugerencias.append(cereal)
        return sugerencias

    def __repr__(self):
        return f"Cooperativa(Lotes={len(self.lotes)}, Cereales={len(self.cereales)})"
