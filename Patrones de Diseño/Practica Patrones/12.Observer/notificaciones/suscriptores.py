from observador import Observador

class SuscriptoresEmail(Observador):
    def actualizar(self, noticia):
        print(f"Suscriptor Email recibe notificación: {noticia}")

class SuscriptoresSMS(Observador):
    def actualizar(self, noticia):
        print(f"Suscriptor SMS recibe notificación: {noticia}")
