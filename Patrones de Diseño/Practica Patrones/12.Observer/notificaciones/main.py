from noticiario import Noticiario
from suscriptores import SuscriptoresEmail, SuscriptoresSMS

def main():
    # Crear noticiario
    noticiario = Noticiario()

    # Crear suscriptores
    suscriptor_email = SuscriptoresEmail()
    suscriptor_sms = SuscriptoresSMS()

    # Agregar suscriptores
    noticiario.agregar_suscriptor(suscriptor_email)
    noticiario.agregar_suscriptor(suscriptor_sms)

    # Publicar noticia
    noticia = "El sistema de notificaciones ha sido actualizado"
    noticiario.publicar_noticia(noticia)

    # Remover un suscriptor y publicar otra noticia
    noticiario.eliminar_suscriptor(suscriptor_email)
    noticiario.publicar_noticia("El clima para hoy será soleado con posibilidad de lluvias.")

if __name__ == "__main__":
    main()