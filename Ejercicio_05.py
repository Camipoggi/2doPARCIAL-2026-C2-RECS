from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    pass

class Pila:
    def __init__(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self):
        return self._datos.esta_vacia()

    def apilar(self, dato):
        self._datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError(
                "No se puede desapilar una pila vacía"
            )

        return self._datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError(
                "No se puede consultar una pila vacía"
            )

        return next(iter(self._datos))
class HistorialReproduccion:
    def __init__(self):
        self._historial = Pila()

    def registrar(self, cancion):
        self._historial.apilar(cancion)

    def anterior(self):
        return self._historial.desapilar()

    def ultima(self):
        return self._historial.ver_tope()
#Respuesta a la pregunta teórica:
#El primer anterior() devuelve la canción "De Musica Ligera",porque fue la última canción registrada en el historial. Esto sucede porque una Pila sigue el principio LIFO:
#Last In, First Out (último en entrar, primero en salir).