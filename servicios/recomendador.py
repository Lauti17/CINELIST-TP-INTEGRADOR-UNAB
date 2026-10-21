from estructuras.heap import MinHeapPeliculasManual
from modelos.pelicula import Pelicula


class Recomendador:
    def __init__(self, lista_peliculas: list[Pelicula]):
        self.peliculas = lista_peliculas

    def obtener_top_n(self, n: int = 5) -> list[Pelicula]:
        """Obtiene las Top N películas con mejor rating en O(N log N_top) usando el Heap manual."""
        heap = MinHeapPeliculasManual(k=n)
        for pelicula in self.peliculas:
            heap.agregar(pelicula)
        return heap.obtener_top_k()