from comisario import Comisario
from compunicodep import ComplejoUnicoDeporte
from evento import Evento
from polideportivo import Polideportivo
from sedeolimpica import SedeOlimpica


comisario1 = Comisario("Juan")
comisario2 = Comisario("María")

# Crear eventos
evento1 = Evento("Carrera 100m", "Fondo", "2024-07-20", "2h", 10, 1, ["Pista"])
evento2 = Evento("Salto Largo", "Salto", "2024-07-21", "3h", 8, 1 , ["Arena", "Medidor"])

comisario1.asignar_evento(evento1)
comisario2.asignar_evento(evento2)

# Crear complejos deportivos
complejo1 = ComplejoUnicoDeporte("Estadio Olímpico", "Centro", "Pedro", 5000, "Atletismo")
complejo2 = Polideportivo("Polideportivo Norte", "Esquina N-E", "Ana", 2000, ["Fútbol", "Tenis"])

# Agregar eventos a los complejos
complejo1.agregar_evento(evento1)
complejo2.agregar_evento(evento2)

# Crear sede olímpica
sede = SedeOlimpica("Sede Central", 1000000)
sede.agregar_complejo(complejo1)
sede.agregar_complejo(complejo2)

# Mostrar datos
print(sede)
print(complejo1)
print(complejo2)
print(comisario1)
print(comisario2)