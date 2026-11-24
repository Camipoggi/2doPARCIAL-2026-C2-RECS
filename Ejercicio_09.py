
import csv
from Ejercicio_01 import Cancion
from Ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


COLUMNAS = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(COLUMNAS)

        for cancion in biblioteca:
            escritor.writerow([
                cancion.id, cancion.titulo, cancion.artista,
                cancion.album, cancion.genero, cancion.anio,
                cancion.duracion_seg
            ])


def cargar_canciones_csv(ruta) -> Biblioteca:
    biblioteca = Biblioteca()

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)

            if next(lector, None) != COLUMNAS:
                raise ArchivoInvalidoError("Encabezado incorrecto")

            for fila in lector:
                if len(fila) != 7:
                    raise ArchivoInvalidoError("Fila con columnas incorrectas")

                biblioteca.agregar(Cancion(
                    int(fila[0]), fila[1], fila[2], fila[3],
                    fila[4], int(fila[5]), int(fila[6])
                ))

    except ArchivoInvalidoError:
        raise
    except (OSError, UnicodeError, ValueError, csv.Error) as error:
        raise ArchivoInvalidoError(f"Archivo CSV inválido: {error}")

    return biblioteca

#Respuesta a la pregunta teórica:
#Sí, para leer la canción de la fila 50 hay que recorrer las filas anteriores porque el CSV no tiene registros de longitud fija. Por eso no podemos calcular directamente la posición de una fila.