class ReservaVuelo:
    def __init__(self):
        self.reservado = False

    def reservar(self):
        if not self.reservado:
            print("Reservando vuelo...")
            self.reservado = True
        else:
            print("Ya estás reservando el vuelo.")

    def cancelar(self):
        if self.reservado:
            print("Cancelando reserva...")
            self.reservado = False
        else:
            print("No estás reservando el vuelo.")