class Vuelo:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []

    def getDisponibles(self):
        return self.capacidad - len(self.pasajeros)

    def addPasajero(self, nombre):
        if self.getDisponibles():
           self.pasajeros.append(nombre)
           return True
        else:
            return False


vuelo = Vuelo(3)

#print(vuelo.getDisponibles())
#print(vuelo.addPasajero('raul1'))
#print(vuelo.addPasajero('raul2'))
#print(vuelo.addPasajero('raul3'))
#print(vuelo.addPasajero('raul4'))
#print(vuelo.getDisponibles())


persona = ['paulina', 'ruben', 'raul', 'joel', 'cristina']
for persona in persona:
    if vuelo.addPasajero(persona):
       print(f'se agrego a {persona} al vuelo')
    else:
       print(f'no hay asiento disponuble para {persona}')
#print(vuelo.getDisponibles())
