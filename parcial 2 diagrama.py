class Persona:
    def __init__(self, nombre, nif, fechaNac):
        self.nombre = nombre
        self.nif = nif
        self.fechaNac = fechaNac

class Jugador(Persona):
    def __init__(self, nombre, nif, fechaNac, numFed):
        super().__init__(nombre, nif, fechaNac) 
        self.numFed = numFed
jugador1 = Jugador("Carlos", "12345678A", "15/04/2000", "FED123")

print("Nombre:", jugador1.nombre)
print("NIF:", jugador1.nif)
print("Fecha de nacimiento:", jugador1.fechaNac)
print("Número de federación:", jugador1.numFed)
