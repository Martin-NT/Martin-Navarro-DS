class Personal:
    def __init__(self, dni, nombre, direccion, telefono, sueldo, numero_seguridad_social):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.sueldo = sueldo
        self.numero_seguridad_social = numero_seguridad_social

    def __repr__(self):
        return f"Personal(DNI={self.dni}, Nombre={self.nombre}, Teléfono={self.telefono}, Sueldo={self.sueldo})"


class Celador(Personal):
    def __init__(self, dni, nombre, direccion, telefono, sueldo, numero_seguridad_social):
        super().__init__(dni, nombre, direccion, telefono, sueldo, numero_seguridad_social)
        self.entrada_asignada = None

    def asignar_entrada(self, entrada):
        self.entrada_asignada = entrada
        entrada.agregar_celador(self)

    def __repr__(self):
        return super().__repr__() + f", Entrada asignada={self.entrada_asignada}"


class Guarda(Personal):
    def __init__(self, dni, nombre, direccion, telefono, sueldo, numero_seguridad_social, tipo_vehiculo, matricula_vehiculo):
        super().__init__(dni, nombre, direccion, telefono, sueldo, numero_seguridad_social)
        self.tipo_vehiculo = tipo_vehiculo
        self.matricula_vehiculo = matricula_vehiculo
        self.areas_asignadas = []

    def asignar_area(self, area):
        self.areas_asignadas.append(area)
        area.agregar_guarda(self)

    def __repr__(self):
        return (super().__repr__() + 
                f", Vehículo={self.tipo_vehiculo}, Matrícula={self.matricula_vehiculo}, "
                f"Áreas asignadas={len(self.areas_asignadas)}")


class Investigador(Personal):
    def __init__(self, dni, nombre, direccion, telefono, sueldo, numero_seguridad_social, titulacion):
        super().__init__(dni, nombre, direccion, telefono, sueldo, numero_seguridad_social)
        self.titulacion = titulacion
        self.proyectos = []  # Proyectos en los que participa
        self.especies_investigadas = []  # Especies investigadas por proyecto

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def agregar_especie_investigada(self, especie):
        self.especies_investigadas.append(especie)

    def __repr__(self):
        return (super().__repr__() + 
                f", Titulación={self.titulacion}, Proyectos={len(self.proyectos)}, "
                f"Especies investigadas={len(self.especies_investigadas)}")
