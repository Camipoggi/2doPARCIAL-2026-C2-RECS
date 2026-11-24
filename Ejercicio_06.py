from Ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self):
        return self._datos.esta_vacia()

    def encolar(self, dato):
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError(
                "No se puede desencolar una cola vacía"
            )

        return self._datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError(
                "No se puede consultar una cola vacía"
            )

        return next(iter(self._datos))
class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        self._cola.encolar(cancion)

    def siguiente(self):
        return self._cola.desencolar()

    def que_sigue(self):
        return self._cola.ver_frente()

#Respuesta a la pregunta teórica:
#El primer siguiente() devuelve la canción "Jijiji", porque fue la primera canción que ingresó a la cola. La Cola sigue el principio FIFO:
#First In, First Out (primero en entrar, primero en salir). En cambio, la Pila sigue LIFO y retira primero el último elemento agregado.