from manejador_descuentos import ManejadorDescuentos

class DescuentoClienteFiel(ManejadorDescuentos):
    def aplicar_descuento(self,precio):
        if self.es_cliente_fiel:
            descuento = precio * 0.025
            precio -= descuento
            print(f"Descuento cliente fiel: Descuento de {descuento}% aplicado.")
        elif self.siguiente_manejador:
            self.siguiente_manejador.aplicar_descuento(precio)
        else:
            print(f"Descuento cliente field: No se puede aplicar el descuento de {precio}%.")
        return precio

    def es_cliente_fiel(self):
        return True