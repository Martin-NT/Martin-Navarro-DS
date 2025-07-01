from servicio_reserva import ServicioReserva
from transportes.avion import Avion
from transportes.tren import Tren
from transportes.micro import Micro  
from comunicacion.email import Email
from comunicacion.sms import Sms    

def separador():
    print("\n" + "-" * 80 + "\n")

if __name__ == '__main__':
    
    reserva = ServicioReserva()
    
    avion = Avion()
    tren = Tren()
    micro = Micro()
    
    sms = Sms()
    email = Email()
    
    print("\n=== 📋 Inicio del sistema de reservas de viajes ===\n")
    
    reserva.realizar_reserva("Buenos Aires", "Martina Rizzotti", avion, sms)
    separador()
    reserva.realizar_reserva("Brasil", "Valentina Rosales", tren, email)
    separador()
    reserva.realizar_reserva("Pinamar", "Martin Navarro", micro, sms)
    separador()
    
    