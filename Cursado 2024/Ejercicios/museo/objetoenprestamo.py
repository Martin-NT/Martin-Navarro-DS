from objetodearte import ObjetoDeArte


class ObjetoEnPrestamo(ObjetoDeArte):
    def __init__(self, id_objeto, titulo, descripcion, artista, anio_creacion, origen, coleccion, fecha_recepcion, fecha_devolucion):
        super().__init__(id_objeto, titulo, descripcion, artista, anio_creacion, origen)
        self.coleccion = coleccion
        self.fecha_recepcion = fecha_recepcion
        self.fecha_devolucion = fecha_devolucion

    def __repr__(self):
        return super().__repr__() + f", Prestamo(Colección={self.coleccion}, Recepción={self.fecha_recepcion}, Devolución={self.fecha_devolucion})"
