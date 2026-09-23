import time
import random
from modelos.pelicula import Pelicula
from estructuras.arbol import ArbolBST


def generar_dataset(cantidad: int) -> list[Pelicula]:
    generos = ["Acción", "Comedia", "Drama", "Ciencia Ficción", "Terror"]
    return [
        Pelicula(
            titulo=f"Pelicula_{i}",
            genero=random.choice(generos),
            rating=round(random.uniform(1.0, 10.0), 1)
        )
        for i in range(cantidad)
    ]


def buscar_secuencial(lista: list[Pelicula], titulo_buscado: str) -> Pelicula | None:
    titulo_lower = titulo_buscado.lower()
    for p in lista:
        if p.titulo.lower() == titulo_lower:
            return p
    return None


def ejecutar_experimentos():
    tamanos = [1000, 10000, 100000]

    print("=" * 65)
    print(f"{'N ELEMENTOS':<15} | {'BÚSQUEDA SECUENCIAL':<20} | {'BÚSQUEDA EN ÁRBOL':<20}")
    print("=" * 65)

    for n in tamanos:
        # 1. Preparar datos
        peliculas = generar_dataset(n)
        
        # Cargar el árbol
        arbol = ArbolBST()
        for p in peliculas:
            arbol.insertar(p.titulo, p)

        # Buscar el último elemento cargado (peor caso para la lista)
        objetivo = f"Pelicula_{n - 1}"

        # 2. Medición Búsqueda Secuencial
        inicio = time.perf_counter()
        _ = buscar_secuencial(peliculas, objetivo)
        fin = time.perf_counter()
        tiempo_secuencial = (fin - inicio) * 1000  # Convertir a milisegundos

        # 3. Medición Búsqueda en Árbol
        inicio = time.perf_counter()
        _ = arbol.buscar(objetivo)
        fin = time.perf_counter()
        tiempo_arbol = (fin - inicio) * 1000  # Convertir a milisegundos

        print(f"{n:<15} | {tiempo_secuencial:.2f} ms{'':<13} | {tiempo_arbol:.2f} ms")

    print("=" * 65)


if __name__ == "__main__":
    ejecutar_experimentos()
    