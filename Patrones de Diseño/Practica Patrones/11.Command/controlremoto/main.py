from dispositivos import Television, Lampara, SistemaSonido
from comandos_concretos import ComandoEncenderTelevision, ComandoApagarTelevision, ComandoEncenderLampara, ComandoApagarLampara, ComandoEncenderSistemaSonido, ComandoApagarSistemaSonido
from control_remoto import ControlRemoto

def main():
    # Crear dispositivos
    television = Television()
    lampara = Lampara()
    sistema_sonido = SistemaSonido()

    # Crear comandos
    encender_tv = ComandoEncenderTelevision(television)
    apagar_tv = ComandoApagarTelevision(television)
    encender_lampara = ComandoEncenderLampara(lampara)
    apagar_lampara = ComandoApagarLampara(lampara)
    encender_sonido = ComandoEncenderSistemaSonido(sistema_sonido)
    apagar_sonido = ComandoApagarSistemaSonido(sistema_sonido)

    # Configurar el control remoto
    control = ControlRemoto()

    # Probar comandos
    control.asignar_comando(encender_tv)
    control.presionar_boton()
    control.presionar_boton_deshacer()

    control.asignar_comando(encender_lampara)
    control.presionar_boton()
    control.presionar_boton_deshacer()

    control.asignar_comando(encender_sonido)
    control.presionar_boton()
    control.presionar_boton_deshacer()

if __name__ == "__main__":
    main()