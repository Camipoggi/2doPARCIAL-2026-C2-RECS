
class Cancion:
    def __init__(self, id, titulo, artista, album,
                 genero, anio, duracion_seg):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self):
        minutos, segundos = divmod(self.duracion_seg, 60)
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return (
            f"#{self.id} {self.titulo} | {self.artista} | "
            f"{self.anio} | {self.duracion_mmss()}"
        )

    def __eq__(self, otra):
        if not isinstance(otra, Cancion):
            return NotImplemented
        return self.id == otra.id

#Respuesta de la pregunta teórica:
#Conviene guardar la duración como un número entero de segundos porque así podemos realizar operaciones matemáticas, comparar duraciones, directamente.
#Después podemos convertirla al formato de minutos y segundos solamente cuando necesitemos mostrarla.