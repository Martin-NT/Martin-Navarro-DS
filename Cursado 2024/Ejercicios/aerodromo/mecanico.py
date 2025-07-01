from persona import Persona


class Mecanico(Persona):
    def __init__(self, nss, nombre, direccion, telefono, salario, turno):
        super().__init__(nss, nombre, direccion, telefono)
        self.salario = salario
        self.turno = turno
        self.servicios = []  

    def realizar_servicio(self, avion, fecha, horas, tipo_trabajo):
        
        for servicio in self.servicios:
            if servicio["avion"] == avion and servicio["fecha"] == fecha and servicio["tipo_trabajo"] == tipo_trabajo:
                raise ValueError("Servicio ya registrado para este avión en la misma fecha con el mismo tipo de trabajo.")
        self.servicios.append({"avion": avion, "fecha": fecha, "horas": horas, "tipo_trabajo": tipo_trabajo})

    def __repr__(self):
        return super().__repr__() + f", Mecanico , Servicios={len(self.servicios)}"
