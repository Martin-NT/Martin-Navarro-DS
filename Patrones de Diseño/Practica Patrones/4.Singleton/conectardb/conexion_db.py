import time
import random

class ConexionDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.conectado = False
        return cls.__instance
    
    def conectar(self):
        if not self.conectado:
            print("Conectando a la base de datos...")
            # Simulación de intentos de conexión con posibilidad de fallo
            intentos = 0
            while intentos < 3:
                intentos += 1
                exito = random.choice([True, False])  # Simula éxito o fallo aleatorio
                if exito:
                    self.conectado = True
                    print("Conexión a la base de datos establecida.")
                    break
                else:
                    print(f"Intento {intentos} fallido. Reintentando...")
                    time.sleep(1)
            if not self.conectado:
                print("Error: No se pudo establecer la conexión después de 3 intentos.")
        else:
            print("Ya estás conectado a la base de datos.")

    def cerrar_conexion(self):
        if self.conectado:
            print("Cerrando la conexión a la base de datos...")
            self.conectado = False
            print("Conexión cerrada.")
        else:
            print("No estás conectado a la base de datos.")

    def consultar(self, consulta):
        if self.conectado:
            print(f"Consulta: {consulta}")
            print("Datos obtenidos:")
            print("Nombre: Juan")
            print("Edad: 25")
            print("Dirección: Calle 123, Puerto 1234")
        else:
            print("No estás conectado a la base de datos.")
