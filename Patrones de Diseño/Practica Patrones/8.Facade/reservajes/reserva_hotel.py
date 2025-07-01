class ReservaHotel:
    def __init__(self):
        self.reservado = False

    def reservar(self):
        if not self.reservado:
            print("Reservando hotel...")
            self.reservado = True
        else:
            print("Ya estás reservando el hotel.")

    def cancelar(self):
        if self.reservado:
            print("Cancelando reserva...")
            self.reservado = False
        else:
            print("No estás reservando el hotel.")