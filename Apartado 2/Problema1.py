#Crea una función que reciba una lista de enteros por parámetro y devuelva otra
#lista, de acuerdo a las siguientes acciones:
#1. Eliminar los números negativos de la lista.
#2. Eliminar los valores que están repetidos, quedándonos con uno de ellos.
#3. Ordenar los números resultantes de menor a mayor.
#Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4].

def listaDeEnteros(lista):
    #set para eliminar los números repetidos y devuelve un Conjunto desordenado
    no_repetidos = set(lista)
    #recorremos la lista para eliminar los números negativos y convertimos el Conjunto en una Lista con list()
    for numero in list(no_repetidos):
        if numero < 0:
            no_repetidos.remove(numero)
    
    #sorted para ordenar de menor a mayor
    return sorted(no_repetidos)

print(listaDeEnteros([4, -1, 2, 4, 3, -5, 2]))

