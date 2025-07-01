from imagen import Imagen
from imagen_real import ImagenReal

class ProxyImagen(Imagen):
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.imagen_real = None

    def mostrar(self):
        if self.imagen_real is None:
            print(f"⏳ Primera vez: creando y cargando la imagen '{self.nombre_archivo}'...")
            self.imagen_real = ImagenReal(self.nombre_archivo)
        else:
            print(f"🔁 La imagen '{self.nombre_archivo}' ya ha sido cargada previamente.")
        self.imagen_real.mostrar()
