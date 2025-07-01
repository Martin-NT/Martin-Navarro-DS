class ParqueNacional:
    def __init__(self, nombre, fecha_declaracion):
        self.nombre = nombre
        self.fecha_declaracion = fecha_declaracion
        self.areas = []  # Lista de áreas en el parque
        self.comunidades = []  # Relación con comunidades autónomas
        self.entradas = []  # Lista de entradas
        self.alojamientos = []  # Lista de alojamientos
        self.excursiones = []  # Lista de excursiones
        self.personal = []  # Lista de personal empleado en el parque

    def agregar_area(self, area):
        self.areas.append(area)

    def agregar_comunidad(self, comunidad):
        self.comunidades.append(comunidad)

    def agregar_entrada(self, entrada):
        self.entradas.append(entrada)

    def agregar_alojamiento(self, alojamiento):
        self.alojamientos.append(alojamiento)

    def agregar_excursion(self, excursion):
        self.excursiones.append(excursion)

    def agregar_personal(self, persona):
        self.personal.append(persona)

    def __repr__(self):
        return (f"ParqueNacional({self.nombre}, Areas={len(self.areas)}, "
                f"Comunidades={len(self.comunidades)}, Entradas={len(self.entradas)}, "
                f"Alojamientos={len(self.alojamientos)}, Excursiones={len(self.excursiones)}, "
                f"Personal={len(self.personal)})")
