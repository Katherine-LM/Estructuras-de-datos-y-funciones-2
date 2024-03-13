def calcular_promedio(velocidades):
    if not velocidades:
        return 0

    return sum(velocidades) / len(velocidades)

def posiciones_sobre_promedio(velocidades):
    promedio = calcular_promedio(velocidades)
    posiciones = []

    for i, velocidad in enumerate(velocidades):
        if velocidad > promedio:
            posiciones.append(i)

    return posiciones

if __name__ == "__main__":
    # Lista de velocidades de muestra
    velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
                 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22,
                 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5,
                 23, 20, 23, 21]

    # Obtener las posiciones sobre el promedio
    posiciones_sobre_promedio = posiciones_sobre_promedio(velocidad)

    # Mostrar el resultado
    print(posiciones_sobre_promedio)
