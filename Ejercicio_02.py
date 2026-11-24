
class CancionNoEncontradaError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id):
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion

        raise CancionNoEncontradaError(
            f"No existe la canción con ID {id}"
        )

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)

#Respuesta de la pregunta teórica:
#La Biblioteca administra el catálogo general, es decir, todas las canciones disponibles. En cambio, la Playlist representa una selección de canciones que realiza el usuario.
#Por eso las mantenemos en clases separadas, ya que tienen responsabilidades y reglas diferentes.