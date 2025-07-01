from conexion_db import ConexionDB

def main():
    conexion = ConexionDB()
    conexion.conectar()
    conexion.consultar("SELECT * FROM usuarios")
    conexion.cerrar_conexion()
    conexion.consultar("SELECT * FROM usuarios")

if __name__ == "__main__":
    main()