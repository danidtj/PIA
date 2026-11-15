#Escribe una función que reciba dos listas de enteros y devuelva un diccionario
#con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
#CALCULARLOS)
#1. La intersección de ambos conjuntos (elementos comunes).
#2. La unión de ambos conjuntos (todos los elementos sin duplicados).
#3. La diferencia simétrica (elementos que están en uno u otro conjunto,
#pero no en ambos).

def interseccion_union_diferencia(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    interseccion = conjunto1.intersection(conjunto2)
    union = conjunto1.union(conjunto2)
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
    
    resultado = {
        "interseccion": interseccion,
        "union": union,
        "diferencia_simetrica": diferencia_simetrica
    }
    
    return resultado


if __name__ == "__main__":
    lista1 = [1, 2, 2, 3, 4, 5, 5]
    lista2 = [4, 4, 5, 6, 7, 8]

    resultado = interseccion_union_diferencia(lista1, lista2)
    print("Intersección:", sorted(resultado["interseccion"]))
    print("Unión:", resultado["union"])
    print("Diferencia simétrica:", resultado["diferencia_simetrica"])