#Escribe una función que reciba por parámetro una lista de palabras y la ruta a
#un fichero de texto y devuelva un diccionario que muestre cuantas veces
#aparecen las distintas palabras de la lista en el fichero de texto. Haz un pequeño
#programa que la ponga a prueba.
#Requisitos:
#1. Eliminar signos de puntuación y convertir todo a minúsculas.
#2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
#3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.

from pathlib import Path


def lista_palabras_ruta(lista_palabras, ruta_fichero):
    """Devuelve un diccionario {palabra: frecuencia}, ordenado por palabra,
    con las veces que aparece cada palabra de la lista en el fichero."""
    frecuencias = {}
    with open(ruta_fichero, 'r', encoding='utf-8') as fichero:
        contenido = fichero.read().lower()
        for signo in '.,;:!?¡¿()[]{}"\'-':
            contenido = contenido.replace(signo, ' ')
        palabras = contenido.split()
        for palabra in lista_palabras:
            palabra = palabra.lower()
            frecuencias[palabra] = palabras.count(palabra)
    return dict(sorted(frecuencias.items()))


if __name__ == "__main__":
    palabras_buscadas = ["gato", "Perro", "el", "duerme", "ladra", "pez", "mesa", "dónde"]
    ruta = Path(__file__).parent / "textoproblema2.txt"

    try:
        resultado = lista_palabras_ruta(palabras_buscadas, ruta)
    except FileNotFoundError:
        print(f"No se encuentra el fichero: {ruta}")
    else:
        print(f"Frecuencias de palabras en '{ruta.name}':")
        for palabra, frecuencia in resultado.items():
            print(f"  {palabra}: {frecuencia}")