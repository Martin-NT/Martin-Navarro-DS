from servicio_reserva import ServicioReserva
from transportes.avion import Avion
from transportes.tren import Tren
from transportes.micro import Micro  
from comunicacion.email import Email
from comunicacion.sms import Sms    

if __name__ == '__main__':
    reserva = ServicioReserva()
    
    avion = Avion()
    tren = Tren()
    micro = Micro()
    
    sms = Sms()
    email = Email()

    print("\n=== 📋 Inicio del sistema de reservas de viajes ===\n")

    viajes = [
        ("Buenos Aires", "Martina Rizzotti", avion, sms),
        ("Brasil", "Valentina Rosales", tren, email),
        ("Pinamar", "Martin Navarro", micro, sms),
    ]

    for i, (destino, cliente, transporte, notificador) in enumerate(viajes, start=1):
        print(f"--- ✈️ Reserva #{i} -------------------------------")
        reserva.realizar_reserva(destino, cliente, transporte, notificador)
        print("-----------------------------------------------\n")

    print("=== ✅ Todas las reservas fueron procesadas ===\n")
