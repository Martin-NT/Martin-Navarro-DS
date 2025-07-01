class ReservaAuto:
    def __init__(self):
        self.reservado = False

    def reservar(self):
        if not self.reservado:
            print("Reservando auto...")
            self.reservado = True
        else:
            print("Ya estás reservando el auto.")

    def cancelar(self):
        if self.reservado:
            print("Cancelando reserva...")
            self.reservado = False
        else:
            print("No estás reservando el auto.")