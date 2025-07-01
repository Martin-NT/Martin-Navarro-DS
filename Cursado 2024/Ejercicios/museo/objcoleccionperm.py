from objetodearte import ObjetoDeArte


class ObjetoColeccionPermanente(ObjetoDeArte):
    def __init__(self, id_objeto, titulo, descripcion, artista, anio_creacion, origen, fecha_adquisicion, costo, estado):
        super().__init__(id_objeto, titulo, descripcion, artista, anio_creacion, origen)
        self.fecha_adquisicion = fecha_adquisicion
        self.costo = costo
        self.estado = estado  # "Exposición" o "Almacén"

    def __repr__(self):
        return super().__repr__() + f", Permanente(Adquisición={self.fecha_adquisicion}, Costo={self.costo}, Estado={self.estado})"
