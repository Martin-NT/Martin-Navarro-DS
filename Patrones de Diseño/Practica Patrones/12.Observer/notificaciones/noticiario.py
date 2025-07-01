class Noticiario:
    def __init__(self):
        self.suscriptores = []

    def agregar_suscriptor(self, observador):
        print(f"Suscriptor {observador.__class__.__name__} agregado")
        self.suscriptores.append(observador)

    def eliminar_suscriptor(self, observador):
        print(f"Suscriptor {observador.__class__.__name__} eliminado")
        self.suscriptores.remove(observador)

    def notificar(self, noticia):
        print(f"Notificación: {noticia}")
        for suscriptor in self.suscriptores:
            suscriptor.actualizar(noticia)

    def publicar_noticia(self, noticia):
        print(f"Noticia: {noticia}")
        self.notificar(noticia)