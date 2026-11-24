 def versiones_de(biblioteca, versiones, cancion_id) -> list:
    biblioteca.obtener(cancion_id)

    directas = []

    for version_id, original_id, tipo in versiones:
        if original_id == cancion_id:
            directas.append((version_id, tipo))

    directas.sort(key=lambda version: version[0])

    resultado = []

    for version_id, tipo in directas:
        cancion = biblioteca.obtener(version_id)

        resultado.append((cancion.titulo, tipo))
        resultado.extend(
            versiones_de(biblioteca, versiones, version_id)
        )

    return resultado

#Respuesta a la pregunta teórica:
#El caso base ocurre cuando una canción no tiene versiones directas. En ese caso, la función devuelve una lista vacía [].
#Secuencia de llamadas:
#versiones_de(..., 12):
#Encuentra la versión 13, de tipo "live".
#Llama recursivamente a versiones_de(..., 13).
#versiones_de(..., 13):
#Encuentra la versión 70, de tipo "remix".
#Llama recursivamente a versiones_de(..., 70).
#versiones_de(..., 70):
#No tiene versiones derivadas.
#Devuelve [] porque se cumple el caso base.
#Al regresar, versiones_de(..., 13) devuelve:
#[("Ji Ji Ji (Remix)", "remix")]
#Finalmente, versiones_de(..., 12) devuelve:
#[("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]
#El recorrido es en preorden porque primero agrega a versión directa y después sus versiones derivadas.