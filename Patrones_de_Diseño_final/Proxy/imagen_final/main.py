from proxy_imagen import ProxyImagen

def separador():
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    print("🎯 Ejemplo del Patrón Proxy: Carga diferida de imágenes")

    # Lista de nombres de imágenes
    nombres = ["foto1.jpg", "foto2.jpg"]

    # Creamos un diccionario para guardar los proxies
    imagenes = {nombre: ProxyImagen(nombre) for nombre in nombres}

    # Primer acceso: simula carga desde disco
    for nombre in nombres:
        separador()
        print(f"--> Primer acceso a la imagen: {nombre}")
        imagenes[nombre].mostrar()

    # Segundo acceso: ya están cargadas
    for nombre in nombres:
        separador()
        print(f"--> Segundo acceso a la imagen: {nombre}")
        imagenes[nombre].mostrar()

    print("\n✅ Fin del ejemplo.")

#    imagen = ProxyImagen("foto1.jpg")
#    imagen.mostrar()