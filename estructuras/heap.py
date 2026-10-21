from modelos.pelicula import Pelicula


class MinHeapPeliculasManual:
    """Heap Mínimo binario implementado manualmente sobre una lista."""

    def __init__(self, k: int):
        self.k = k
        self.heap: list[Pelicula] = []

    def _padre(self, i: int) -> int:
        return (i - 1) // 2

    def _hijo_izq(self, i: int) -> int:
        return 2 * i + 1

    def _hijo_der(self, i: int) -> int:
        return 2 * i + 2

    def _sift_up(self, i: int):
        """Acomoda el elemento hacia arriba para mantener la propiedad de Heap."""
        while i > 0 and self.heap[i].rating < self.heap[self._padre(i)].rating:
            p_idx = self._padre(i)
            self.heap[i], self.heap[p_idx] = self.heap[p_idx], self.heap[i]
            i = p_idx

    def _sift_down(self, i: int):
        """Acomoda el elemento hacia abajo para mantener la propiedad de Heap."""
        min_idx = i
        izq = self._hijo_izq(i)
        der = self._hijo_der(i)

        if izq < len(self.heap) and self.heap[izq].rating < self.heap[min_idx].rating:
            min_idx = izq

        if der < len(self.heap) and self.heap[der].rating < self.heap[min_idx].rating:
            min_idx = der

        if i != min_idx:
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            self._sift_down(min_idx)

    def agregar(self, pelicula: Pelicula):
        """Agrega un elemento manteniendo como máximo K elementos de mayor rating."""
        if len(self.heap) < self.k:
            self.heap.append(pelicula)
            self._sift_up(len(self.heap) - 1)
        elif pelicula.rating > self.heap[0].rating:
            # Reemplazamos la raíz (el menor de los K actuales) y reacomodamos
            self.heap[0] = pelicula
            self._sift_down(0)

    def obtener_top_k(self) -> list[Pelicula]:
        """Devuelve el ranking final ordenado de mayor a menor rating."""
        return sorted(self.heap, key=lambda p: p.rating, reverse=True)