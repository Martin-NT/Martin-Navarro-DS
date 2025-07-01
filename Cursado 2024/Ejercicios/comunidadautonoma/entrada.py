class Entrada:
    def __init__(self, numero):
        self.numero = numero
        self.celadores = []  # Celadores asignados a la entrada

    def agregar_celador(self, celador):
        self.celadores.append(celador)

    def __repr__(self):
        return f"Entrada(Número={self.numero}, Celadores={len(self.celadores)})"
