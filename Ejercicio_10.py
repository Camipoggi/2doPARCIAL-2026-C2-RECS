import os
import struct

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

class ArchivoInvalidoError(Exception):
    pass

ENCABEZADO = struct.Struct("=4s1sI")

REGISTRO = struct.Struct("=I40s40s40s16sHH")

MAGIA = b"AYED"
TEMA = b"M"

def _codificar(texto, ancho):
    """Codifica UTF-8, recorta y completa con bytes nulos."""

    bytes_texto = str(texto).encode("utf-8")[:ancho]

    bytes_texto = bytes_texto.decode(
        "utf-8",
        errors="ignore"
    ).encode("utf-8")

    return bytes_texto.ljust(ancho, b"\0")

def _decodificar(valor):
    return valor.split(b"\0", 1)[0].decode("utf-8")

def _empaquetar_cancion(cancion):

    return REGISTRO.pack(
        cancion.id,
        _codificar(cancion.titulo, 40),
        _codificar(cancion.artista, 40),
        _codificar(cancion.album, 40),
        _codificar(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg
    )

def _leer_y_validar_encabezado(archivo):

    archivo.seek(0)

    datos = archivo.read(ENCABEZADO.size)

    if len(datos) != ENCABEZADO.size:
        raise ArchivoInvalidoError(
            "El encabezado binario está incompleto"
        )

    magia, tema, cantidad = ENCABEZADO.unpack(datos)

    if magia != MAGIA:
        raise ArchivoInvalidoError(
            "Magia inválida: se esperaba AYED"
        )

    if tema != TEMA:
        raise ArchivoInvalidoError(
            "Tema inválido: se esperaba M"
        )

    archivo.seek(0, os.SEEK_END)

    tamanio_real = archivo.tell()

    tamanio_esperado = (
        ENCABEZADO.size + cantidad * REGISTRO.size
    )

    if tamanio_real != tamanio_esperado:
        raise ArchivoInvalidoError(
            f"Tamaño incorrecto: {tamanio_real} bytes; "
            f"se esperaban {tamanio_esperado}"
        )

    return cantidad

def guardar_binario(ruta, biblioteca):

    canciones = list(biblioteca)

    try:
        with open(ruta, "wb") as archivo:

            archivo.write(
                ENCABEZADO.pack(
                    MAGIA,
                    TEMA,
                    len(canciones)
                )
            )

            for cancion in canciones:
                archivo.write(
                    _empaquetar_cancion(cancion)
                )

    except (OSError, struct.error, ValueError, UnicodeError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el binario: {error}"
        ) from error

def cargar_binario(ruta) -> Biblioteca:

    biblioteca = Biblioteca()

    try:
        with open(ruta, "rb") as archivo:

            cantidad = _leer_y_validar_encabezado(archivo)

            archivo.seek(ENCABEZADO.size)

            for _ in range(cantidad):

                datos = archivo.read(REGISTRO.size)

                (
                    id,
                    titulo,
                    artista,
                    album,
                    genero,
                    anio,
                    duracion
                ) = REGISTRO.unpack(datos)

                biblioteca.agregar(
                    Cancion(
                        id,
                        _decodificar(titulo),
                        _decodificar(artista),
                        _decodificar(album),
                        _decodificar(genero),
                        anio,
                        duracion
                    )
                )

    except ArchivoInvalidoError:
        raise

    except (OSError, struct.error, ValueError, UnicodeError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer el binario: {error}"
        ) from error

    return biblioteca

def actualizar_registro(ruta, posicion, cancion):

    try:
        with open(ruta, "r+b") as archivo:

            cantidad = _leer_y_validar_encabezado(archivo)

            if (
                not isinstance(posicion, int)
                or not 0 <= posicion < cantidad
            ):
                raise ArchivoInvalidoError(
                    f"Posición {posicion} fuera de rango "
                    f"(0 a {cantidad - 1})"
                )

            offset = (
                ENCABEZADO.size
                + posicion * REGISTRO.size
            )

            archivo.seek(offset)

            archivo.write(
                _empaquetar_cancion(cancion)
            )

    except ArchivoInvalidoError:
        raise

    except (OSError, struct.error, ValueError, UnicodeError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el registro: {error}"
        ) from error

#Respuesta a la pregunta teórica:
#La posición inicial de un registro se calcula mediante: offset = 9 + k * 144
#
# Donde:
# 9 representa los bytes del encabezado.
# k representa la posición del registro, comenzando desde 0.
# 144 representa los bytes que ocupa cada registro.
#
# Como los registros tienen longitud fija, podemos calcular
# directamente su ubicación y acceder mediante seek,
# sin recorrer todos los registros anteriores.