import threading
import time

class ControladorImpresoras:
    _instance = None
    _instance_lock = threading.Lock()  # Lock para crear instancia singleton
    _imprimir_lock = threading.Lock()  # Lock para controlar impresión

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.impresoras = {}
                    cls._instance.impresora_actual = None
        return cls._instance

    def agregar_impresora(self, nombre):
        if nombre not in self.impresoras:
            self.impresoras[nombre] = 'Disponible'
            print(f"--> Impresora '{nombre}' agregada exitosamente.")
        else:
            print(f"--> Error: La impresora '{nombre}' ya existe.")

    def listar_impresoras(self):
        print("\nLista de impresoras:")
        for nombre, estado in self.impresoras.items():
            print(f"- {nombre}: {estado}")

    def imprimir(self, impresora, documento):
        if impresora not in self.impresoras:
            print(f"--> Error: La impresora '{impresora}' no está registrada.")
            return

        if self.impresoras[impresora] == 'Imprimiendo':
            print(f"-->Error: La impresora '{impresora}' está ocupada.")
            return

        with self._imprimir_lock:
            print(f"\nIniciando la impresión en la impresora '{impresora}'...")
            self.impresoras[impresora] = 'Imprimiendo'
            self.impresora_actual = impresora
            time.sleep(2)  # Simula el tiempo de impresión
            print(f"--> Documento '{documento}' impreso en la impresora '{impresora}'.")
            self.impresoras[impresora] = 'Disponible'
            self.impresora_actual = None

    def verificar_estado(self, impresora):
        if impresora in self.impresoras:
            print(f"--> Estado de la impresora '{impresora}': {self.impresoras[impresora]}")
        else:
            print(f"--> Error: La impresora '{impresora}' no está registrada.")
