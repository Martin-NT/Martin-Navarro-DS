from reserva_auto import ReservaAuto
from reserva_hotel import ReservaHotel
from reserva_vuelo import ReservaVuelo

class FachadaReserva:
    def __init__(self):
        self.auto = ReservaAuto()
        self.hotel = ReservaHotel()
        self.vuelo = ReservaVuelo()

    def reservar_viaje(self):   
        print("Iniciando reserva")
        self.auto.reservar()
        self.hotel.reservar()
        self.vuelo.reservar()
        print("Reserva finalizada")

    def cancelar_viaje(self):
        print("Iniciando cancelación")
        self.auto.cancelar()
        self.hotel.cancelar()
        self.vuelo.cancelar()        
        print("Cancelación finalizada")

    def mostrar_detalles_reserva(self):
        print("Detalles de la reserva:")
        print(f"- Auto: {'Reservado' if self.auto.reservado else 'No reservado'}")
        print(f"- Hotel: {'Reservado' if self.hotel.reservado else 'No reservado'}")
        print(f"- Vuelo: {'Reservado' if self.vuelo.reservado else 'No reservado'}")