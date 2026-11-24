from ejercicio_02 import CancionNoEncontradaError
class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
class ListaEnlazada:
    def __init__(self):
        self._primero = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        return self._primero is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._primero = Nodo(dato, self._primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self._primero = nuevo
        else:
            actual = self._primero

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            return None

        dato = self._primero.dato
        self._primero = self._primero.siguiente
        self._tamanio -= 1

        return dato

    def __iter__(self):
        actual = self._primero

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def quitar_por_id(self, id):
        anterior = None
        actual = self._primero

        while actual is not None:
            if actual.dato.id == id:

                if anterior is None:
                    self._primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                self._tamanio -= 1
                return actual.dato

            anterior = actual
            actual = actual.siguiente

        return None
class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        cancion = self._canciones.quitar_por_id(id)

        if cancion is None:
            raise CancionNoEncontradaError(
                f"La canción con ID {id} no está en la playlist"
            )

        return cancion

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self):
        total = 0

        for cancion in self._canciones:
            total += cancion.duracion_seg

        return total
#Respuesta a la pregunta teórica:
#Cuando la lista ya tiene n nodos, para insertar al final debemos recorrer desde el primero hasta el último.Se atraviesan n-1 enlaces si n es mayor o igual a 1.
#Por eso, la complejidad temporal es O(n), ya queel trabajo aumenta proporcionalmente con la cantidad e nodos almacenados.