from ejercicio_02 import CancionNoEncontradaError


class CampoInvalidoError(Exception):
    pass


def busqueda_lineal(canciones, campo, valor) -> list:
    if campo not in ("titulo", "artista", "genero"):
        raise CampoInvalidoError(
            f"El campo '{campo}' no es válido"
        )

    resultado = []

    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            resultado.append(cancion)

    return resultado


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    izquierda = 0
    derecha = len(canciones_ordenadas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        cancion = canciones_ordenadas[medio]

        if cancion.titulo == titulo:
            return cancion

        elif cancion.titulo < titulo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    raise CancionNoEncontradaError(
        f"No existe el título '{titulo}'"
    )

#Respuesta a la pregunta teórica:
#La búsqueda binaria necesita que la lista esté ordenadapor título porque compara con el elemento central y descarta una mitad de la colección en cada paso.
#Si los elementos no estuvieran ordenados, podría descartar una mitad que contiene la canción buscada. La búsqueda binaria tiene complejidad O(log n). La búsqueda lineal por artista tiene complejidad O(n),porque puede necesitar recorrer todas las canciones.