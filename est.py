import math

def media(lista):
    return sum(lista)/len(lista)

#Definir la Desviación Estándar crearemos la función sdd de la siguiente manera:

# El primero calcula las diferencias entre cada elemento de la lista con la media y eleva dicho resultado al cuadrado. Dado que esto se debe hacer elemento por elemento es que se
# implementa mediante un List Comprehension. Luego se calcula la raíz cuadrada de la división de la suma de las diferencias calculadas en el
# paso anterior, que a su vez se dividen por el número de elementos menos 1.
def sdd(lista, media):
    diff = [ (elemento-media) **2 for elemento in lista]
    return math.sqrt(sum(diff) / (len(lista)-1))

#Calcular la media y la desviación estándar de la lista en cuestión.  Calcular la diferencia de cada elemento con su media, resultado que
# posteriormente se divide por la desviación estándar; y nuevamente debido a que estos cálculos se deben implementar elemento a elemento es que se utiliza una
# List Comprehension. Nuestra función resultado() devolverá los 3 resultados 
def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor-m)/sd for valor in lista]
    return m, sd, lista_estandarizada

lista = [1,2,3,4,5,6]

m, desv_st,l_e = resultado(lista)
print('la media es: ', m)
print('La desviación estándar es: ', desv_st)
print('la lista estandarizada: ', l_e)