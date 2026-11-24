import csv

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

class ArchivoInvalidoError(Exception):
    pass

COLUMNAS = [
    "id",
    "titulo",
    "artista",
    "album",
    "genero",
    "anio",
    "duracion_seg"
]
def guardar_canciones_csv(ruta, biblioteca):

    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")

        escritor.writerow(COLUMNAS)

        for cancion in biblioteca:
            escritor.writerow([
                cancion.id,
                cancion.titulo,
                cancion.artista,
                cancion.album,
                cancion.genero,
                cancion.anio,
                cancion.duracion_seg
            ])

def cargar_canciones_csv(ruta) -> Biblioteca:
    biblioteca = Biblioteca()
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:

            lector = csv.reader(
                archivo,
                delimiter=",",
                strict=True
            )

            encabezado = next(lector, None)

            if encabezado != COLUMNAS:
                raise ArchivoInvalidoError(
                    "Encabezado CSV incorrecto"
                )

            for numero_fila, fila in enumerate(lector, start=2):

                if len(fila) != len(COLUMNAS):
                    raise ArchivoInvalidoError(
                        f"La fila {numero_fila} tiene "
                        f"{len(fila)} columnas; se esperaban 7"
                    )

                biblioteca.agregar(
                    Cancion(
                        int(fila[0]),
                        fila[1],
                        fila[2],
                        fila[3],
                        fila[4],
                        int(fila[5]),
                        int(fila[6])
                    )
                )

    except ArchivoInvalidoError:
        raise
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo cargar el CSV: {error}"
        ) from error

    return biblioteca

#Respuesta a la pregunta teórica:
#Sí, para leer la canción de la fila 50 debemos recorrerlas filas anteriores, porque el CSV es un archivo de textocon registros que pueden tener longitudes diferentes.
#Por eso no podemos calcular directamente la posiciónde una fila utilizando un tamaño fijo de registro.