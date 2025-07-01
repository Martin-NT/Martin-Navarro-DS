from proxy_reg import ProxyRegistro

def main():
    proxy = ProxyRegistro()
    proxy.consultar_datos()
    proxy.enviar_datos("Datos enviados")
    proxy.consultar_datos()
    proxy.consultar_registros()

if __name__ == "__main__":
    main()