import random
import paises_capitales

def quiz_capitales():
    print("Bienvenido al Quiz de Capitales")
    score = 0

    # Obtener una lista de los países y mezclarla aleatoriamente
    paises = list(paises_capitales.paises_capitales.keys())
    random.shuffle(paises)

    # Iterar sobre los países en el orden aleatorio
    for pais in paises:
        capital = paises_capitales.paises_capitales[pais]
        respuesta = input(f"¿Cuál es la capital de {pais}?: ")
        if respuesta.lower() == capital.lower():
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La capital de {pais} es {capital}")

    print(f"Tu puntuación es {score} de {len(paises_capitales.paises_capitales)}")

quiz_capitales()
