# viajante3D
El problema del viajante3D es una variación del problema del viajante.
Este problema se basa en buscar la manera más corta de recorrer un número determinado de puntos en el espacio tridimensional. Varía del problema del viajante porque el programa no recibe un grafo con conexiones entre sus puntos, sino un conjunto de puntos en el espacio tridimensional (la coordenada del eje X, la coordenada del eje Y y la coordenada del eje Z). Suponemos que los puntos tienen todos conexiones entre todos.

<b>Generar población inicial</b>:<br>
El algoritmo generará N puntos en el espacio de forma aleatoria a partir de sus coordenadas en los ejes X, Y y Z. Dado también al programa un número de cromosomas por población M, la población inicial serán M cromosomas cada cual estará compuesto por una permutación aleatoria sin repetición del número N.

<b>Evaluar población</b>:<br>
La función de aptitud es la inversa de la suma de las distancias de cada punto del cromosoma desde el primero hasta el último. La razón por la que sea la inversa es para que sea un problema de maximización de aptitud, porque mientras más cerca estén dos puntos mayor aptitud tendrá el cromosoma.

<b>¿Solución suficiente? Condición de parada</b>:<br>
La complejidad de la solución aumenta con el número de puntos disponibles, por lo que la condición de parada es que el mejor de cada población no mejore en un X tanto por ciento en unas Y generaciones.

<b>Selección de población</b>:<br>
La selección se basa en la ruleta con pesos.
Para asegurar el elitismo, automáticamente el mejor cromosoma es seleccionado. La probabilidad de que no salga en la ruleta con pesos es muy baja, pero existe; por el contrario una repetición más del mejor cromosoma no es relevante en el posterior cruzamiento.

<b>Cruzamiento</b>:<br>
Cruzamiento paso a paso:<br>
1) Selección de dos cromosomas de la población de forma aleatoria, padre 1 y padre 2.<br>
2) División de los cromosomas padre 1 y padre 2 en 3 grupos de genes de forma aleatoria.<br>
3) Los cromosomas hijo 1 e hijo 2 van a estar formados de la siguiente manera:<br>
  a) El grupo de genes del medio del hijo 1 va a ser el grupo de genes del medio del padre 2. EL grupo de genes del medio del hijo 2 va a ser el grupo de genes del medio del padre 1.<br>
  b) Los grupos de genes 1 y 3 del padre 2 se introducen en orden en los huecos restantes del hijo 1 (si algún gen estaba anteriormente, no se introduce).<br>
  c) Los grupos de genes 1 y 3 del padre 1 se introducen en orden en los huecos restantes del hijo 2 (si algún gen estaba anteriormente, no se introduce).<br>
4) Se recorre el hijo 1 y el hijo 2 para ir añadiendo los genes que falten hasta rellenarlo entero.<br>

De esta manera, garantizamos un cruzamiento por dos puntos preservando que el cromosoma siga siendo una permutación sin repetición del número de puntos a unir.
Para garantizar el elitismo, uno de los mejores cromosomas de esa población pasa directamente a formar parte de la nueva población. Si el total del resto de cromosomas son impares, el siguiente mejor cromosoma de la población pasa automáticamente también a la nueva población para así cruzar de dos en dos a los restantes cromosomas. 
Como la probabilidad de que solo haya un único “mejor cromosoma” en la población, no se pierde la propiedad de un algoritmo genético de cruzar a los mejores de cada población con otros.
La probabilidad de cruce es del 100%.



<b>Mutación</b>:<br>
Para la mutación se intercambian las posiciones de dos genes aleatorios del cromosoma bajo una probabilidad de mutación. 
Para garantizar el elitismo, el proceso de mutación se intenta en cada cromosoma de la población salvo en el mejor (o en uno de los mejores).
