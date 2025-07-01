from fachada_reserva import FachadaReserva

def main():
    fachada = FachadaReserva()
    fachada.reservar_viaje()
    fachada.mostrar_detalles_reserva()
    input("Presione ENTER para cancelar la reserva...")
    fachada.cancelar_viaje()
    fachada.mostrar_detalles_reserva()

if __name__ == "__main__":
    main()