from proxy_doc import ProxyDocumentoSecreto

def main():
    proxy_documento = ProxyDocumentoSecreto("12345")

    # Intentar leer el documento
    proxy_documento.leer()

    # Intentar escribir en el documento
    proxy_documento.escribir("Este es el nuevo contenido del documento.")

    # Cambiar la contraseña
    print("\nIntento de cambio de contraseña:")
    proxy_documento.cambiar_contraseña("12345", "nuevaContraseña")

    # Intentar leer el documento con la nueva contraseña
    print("\nVerificación con la nueva contraseña:")
    proxy_documento.leer()

if __name__ == "__main__":
    main()
