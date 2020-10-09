import random
import math

class Cromosoma():

    #Hacer dos constructores en uno, ya que en python no puedo tener varios. 
    def __init__(self, num_puntos, camino):
        if camino == None:
            lista_ordenada = list(range(num_puntos))
            random.shuffle(lista_ordenada)
            self.camino = lista_ordenada
            self.aptitud = None
        else:
            self.camino = camino
            self.aptitud = None


    def distancia(self, puntos,origen,destino):
        x1,y1,z1=puntos[origen]
        x2,y2,z2=puntos[destino]
        
        return math.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )

    #return inverso de la distancia total para que la menor sea la mejor.
    #se multiplica por 1000 para apreciar mejor la diferencia entre aptitudes.
    def funcionEvaluacion(self, puntos):
        distancia_total = 0
        numero_puntos = len(self.camino)
        i = 0
        while i < numero_puntos - 1:
            ciudad_actual = self.camino[i]
            ciudad_siguiente = self.camino[i+1]
            distancia_total += self.distancia(puntos, ciudad_actual, ciudad_siguiente)
            i += 1
        return 1/distancia_total * 100000



    def evaluar(self, puntos):
        self.aptitud = self.funcionEvaluacion(puntos)



    def mutar(self, probabilidad):
        aleatorio = random.randrange(101)
        if aleatorio <= probabilidad:
            ciudad1 = random.choice(self.camino)
            ciudad2 = random.choice(self.camino)
            while ciudad2 == ciudad1:
                ciudad2 = random.choice(self.camino)
            indice_ciudad1 = self.camino.index(ciudad1)
            indice_ciudad2 = self.camino.index(ciudad2)
            self.camino[indice_ciudad2] = ciudad1
            self.camino[indice_ciudad1] = ciudad2

            #print(f"El cromosoma {self.camino} ha intercambiado posiciones de los genes {ciudad1} y {ciudad2}")
