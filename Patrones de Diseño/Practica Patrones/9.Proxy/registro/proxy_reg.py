from datetime import datetime
from serv_web import ServicioWeb

class ProxyRegistro:
    def __init__(self):
        self.servicio_web = ServicioWeb()
        self.registros = []

    def consultar_datos(self):
        self._registrar("Llamada al método: consultar_datos()")
        resultado = self.servicio_web.consultar_datos()
        self._registrar("Resultado: " + resultado)
        return resultado

    def enviar_datos(self, datos):
        self._registrar(f"Llamada al método: enviar_datos() con datos: {datos}")
        resultado = self.servicio_web.enviar_datos(datos)
        self._registrar("Resultado: " + resultado)
        return resultado

    def _registrar(self, mensaje):
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = f"{tiempo} - {mensaje}"
        self.registros.append(registro)
        # Guardar el registro en un archivo
        with open("registros.log", "a") as archivo:
            archivo.write(registro + "\n")

    def consultar_registros(self):
        print("\nRegistros guardados:")
        for registro in self.registros:
            print(registro)
