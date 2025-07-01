import time
from imagen import Imagen

class ImagenReal(Imagen):
    def __init__(self, nombre_archivo):
        """Inicializa la imagen real y simula su carga desde disco"""
        self.nombre_archivo = nombre_archivo
        self.cargar_desde_disco()

    def cargar_desde_disco(self):
        print(f"📂 Cargando la imagen '{self.nombre_archivo}' desde el disco...")
        time.sleep(5) 

    def mostrar(self):
        print(f"🖼️  Mostrando imagen: {self.nombre_archivo}")
