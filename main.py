from Poblacion import *
import time
from Cromosoma import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import numpy as np
import sys


def getEje(puntos, eje):
	eje_N = []
	for i in range(len(puntos)):
		coordenada = puntos[i][eje]
		eje_N.append(coordenada)
	return np.array(eje_N)




def mejorCromosoma(listacromosomas):
	mejorcromosoma = listacromosomas[0]
	for i in listacromosomas:
		if i.aptitud > mejorcromosoma.aptitud:
			mejorcromosoma = i
	return mejorcromosoma



def condicionDeParada(mejores_cromosomas, generaciones_parada, porcentaje_parada):
	generaciones = len(mejores_cromosomas)
	mejor_cromosoma = mejorCromosoma(mejores_cromosomas)
	condicion_generaciones = False 
	condicion_aptitudes = False

	if (generaciones - mejores_cromosomas.index(mejor_cromosoma)) > generaciones_parada:
		condicion_generaciones = True

	porcentaje_de_aptitud = porcentaje_parada * mejor_cromosoma.aptitud / 100
	diferencia_aptitudes = abs(mejores_cromosomas[-1].aptitud - mejor_cromosoma.aptitud)

	if (diferencia_aptitudes < porcentaje_de_aptitud):
		condicion_aptitudes = True

	return condicion_generaciones and condicion_aptitudes




nombre_archivo = input("Introduzca el nombre del archivo que contiene los datos\n")
datos = []
with open(nombre_archivo) as f:
	for linea in f:
		datos.append(linea)


prob_mutacion = float(datos[0])
num_cromosomas = int(datos[1])
num_puntos = int(datos[2])
generaciones_parada = int(datos[3])
porcentaje_parada = float(datos[4])

if num_puntos <= 2:
	sys.exit("El numero de ciudades ha de ser mayor que 2.")

puntos = []
contador_generaciones = 1

for i in range(num_puntos):
	coordenada_x = random.randrange(0, 100000001)/100000
	coordenada_y = random.randrange(0, 100000001)/100000
	coordenada_z = random.randrange(0, 100000001)/100000
	puntos.append([coordenada_x, coordenada_y, coordenada_z])





poblacion = Poblacion(num_cromosomas, num_puntos)
poblacion.evaluarPoblacion(puntos)
mejores_cromosomas = [poblacion.getMejorCromosoma()]
while not condicionDeParada(mejores_cromosomas, generaciones_parada, porcentaje_parada):
	#print(f"\n**********************GENERACION {contador_generaciones}*************************\n")
	poblacion.seleccionar()
	poblacion.cruzar()
	poblacion.mutarPoblacion(prob_mutacion)
	poblacion.evaluarPoblacion(puntos)
	contador_generaciones += 1
	mejores_cromosomas.append(poblacion.getMejorCromosoma())

mejor_cromosoma = mejorCromosoma(mejores_cromosomas)
indice = mejores_cromosomas.index(mejor_cromosoma)
print(f"\n\nEl mejor cromosoma ha sido: {mejor_cromosoma.camino} con aptitud {mejor_cromosoma.aptitud} de la generacion {indice}")





#Para mostrar las graficas
lista_mejores_cromosomas = []
for i in mejores_cromosomas:
	lista_mejores_cromosomas.append(i.aptitud)

puntos_ordenados = []

for index in mejor_cromosoma.camino:
	puntos_ordenados.append(puntos[index])

plt.plot(lista_mejores_cromosomas)
figura = plt.figure()
ax1 = figura.add_subplot(111, projection='3d')
datos_x = getEje(puntos, 0)
datos_y = getEje(puntos, 1)
datos_z = getEje(puntos, 2)
ax1.scatter3D(datos_x, datos_y, datos_z, c='red')

datos_x_ord = getEje(puntos_ordenados, 0)
datos_y_ord = getEje(puntos_ordenados, 1)
datos_z_ord = getEje(puntos_ordenados, 2)
ax1.plot(datos_x_ord, datos_y_ord, datos_z_ord)

plt.show()

