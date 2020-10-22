from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id = 0, origenX = 0, origenY = 0, destinoX = 0, destinoY = 0, velocidad = 0, colorR = 0, colorG = 0, colorB = 0, distancia = 0):
        self.id = id
        self.origenX = origenX
        self.origenY = origenY
        self.destinoX = destinoX
        self.destinoY = destinoY
        self.velocidad = velocidad
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB
        self.distancia = distancia_euclidiana(origenX, origenY, destinoX, destinoY)

    def  __str__(self):
        return(
            'Id: ' + str(self.id) + '\n' +
            'Origen X: ' + str(self.origenX) + '\n' +
            'Origen Y: ' + str(self.origenY) + '\n' +
            'Destino X: ' + str(self.destinoX) + '\n' +
            'Destino Y: ' + str(self.destinoY) + '\n' +
            'Velocidad: ' + str(self.velocidad) + '\n' +
            'Color R: ' + str(self.colorR) + '\n' +
            'Color G: ' + str(self.colorG) + '\n' +
            'Color B:  ' + str(self.colorB) + '\n' +
            'Distancia: ' + str(self.distancia) + '\n'
        )
    
    def to_dict(self): #esto retorna un diccionario
        return {
            "id" : self.id,
            "origenX" : self.origenX,
            "origenY" : self.origenY,
            "destinoX" : self.destinoX,
            "destinoY" : self.destinoY,
            "velocidad" : self.velocidad,
            "colorR" : self.colorR,
            "colorG" : self.colorG,
            "colorB" : self.colorB,
        }