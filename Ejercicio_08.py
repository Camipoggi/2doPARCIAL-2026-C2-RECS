from ejercicio_02 import CancionNoEncontradaError
def busqueda_lineal(canciones, campo, valor) -> list:

    if campo not in ("titulo", "artista", "genero"):
        raise ValueError(
            "El campo debe ser 'titulo', 'artista' o 'genero'"
        )

    coincidencias = []

    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            coincidencias.append(cancion)

    return coincidencias
def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):

    izquierda = 0
    derecha = len(canciones_ordenadas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = canciones_ordenadas[medio]

        if actual.titulo == titulo:
            return actual

        if actual.titulo < titulo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    raise CancionNoEncontradaError(
        f"No existe una canción con título '{titulo}'"
    )

# Respuesta a la pregunta teórica:
#El ordenamiento por selección tiene complejidad temporal O(n²) en el peor caso, porque utiliza recorridos anidados para encontrar el elemento que corresponde a cada posición.
#El ordenamiento por inserción también tiene complejidad O(n²) en el peor caso, porque puede necesitar desplazar numerosos elementos para insertar cada canción.
#El algoritmo de inserción es estable porque conserva el orden relativo de canciones con la misma clave.
#El algoritmo de selección con intercambios no garantiza estabilidad, ya que puede alterar ese orden relativo.