class ServicioDeCobro:
    def realizar_pago(self, monto, metodo_pago):
        metodo_pago.pagar(monto)

#¿Qué cambia?
#Ya no se valida que metodo_pago tenga .pagar(), pero mientras lo tenga, todo funciona.
#No hay herencia. Es más flexible, pero puede ser más riesgoso en proyectos grandes.