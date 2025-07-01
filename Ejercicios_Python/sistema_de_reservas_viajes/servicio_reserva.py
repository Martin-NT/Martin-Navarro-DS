from interfaces.transporte import Transporte
from interfaces.notificador import Notificador
class ServicioReserva():
    def realizar_reserva(self, destino, cliente, transporte: Transporte, notificador: Notificador):
        print(f"--> Realizando reserva a {destino} para {cliente}")
        transporte.reservar(destino)
        transporte.calcular_costo(destino)
        mensaje = f"Tu reserva a {destino} fue realizada con éxito."
        notificador.notificar(mensaje, cliente)
