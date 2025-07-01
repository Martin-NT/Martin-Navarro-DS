from reproductor import Reproductor

def mostrar_menu():
    print("\n🎵 Opciones:")
    print("1. ▶️  Reproducir")
    print("2. ⏸️  Pausar")
    print("3. ⏹️  Detener")
    print("4. ⏭️  Avanzar canción")
    print("5. ⏮️  Retroceder canción")
    print("0. ❌ Salir")

if __name__ == "__main__":
    r = Reproductor()
    while True:
        mostrar_menu()
        opcion = input("👉 Elegí una opción: ")
        
        if opcion == "1":
            r.reproducir()
        elif opcion == "2":
            r.pausar()
        elif opcion == "3":
            r.detener()
        elif opcion == "4":
            r.avanzar_cancion()
        elif opcion == "5":
            r.retroceder_cancion()
        elif opcion == "0":
            print("👋 Saliendo del reproductor...")
            break
        else:
            print("❌ Opción no válida. Probá otra vez.")
