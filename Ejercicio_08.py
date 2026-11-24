def ordenar_por_anio_seleccion(canciones) -> list:
    # Ordena por año de mayor a menor.

    for i in range(len(canciones) - 1):
        mayor = i

        for j in range(i + 1, len(canciones)):
            if canciones[j].anio > canciones[mayor].anio:
                mayor = j

        canciones[i], canciones[mayor] = (
            canciones[mayor], canciones[i]
        )

    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    # Ordena por duración de menor a mayor.

    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1

        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1

        canciones[j + 1] = actual

    return canciones

# Respuesta a la pregunta teórica:
#El ordenamiento por selección tiene complejidad temporal O(n²) en el peor caso, porque utiliza recorridos anidados para encontrar el elemento que corresponde a cada posición.
#El ordenamiento por inserción también tiene complejidad O(n²) en el peor caso, porque puede necesitar desplazar numerosos elementos para insertar cada canción.
#El algoritmo de inserción es estable porque conserva el orden relativo de canciones con la misma clave.
#El algoritmo de selección con intercambios no garantiza estabilidad, ya que puede alterar ese orden relativo.