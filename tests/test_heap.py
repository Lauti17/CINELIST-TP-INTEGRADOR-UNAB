import unittest
from modelos.pelicula import Pelicula
from estructuras.heap import MinHeapPeliculasManual


class TestMinHeapManual(unittest.TestCase):

    def test_top_n_manual(self):
        p1 = Pelicula("Matrix", "Ciencia Ficción", 9.8)
        p2 = Pelicula("Inception", "Ciencia Ficción", 9.6)
        p3 = Pelicula("Interstellar", "Ciencia Ficción", 9.5)
        p4 = Pelicula("Blade Runner", "Ciencia Ficción", 9.2)

        heap = MinHeapPeliculasManual(k=3)
        for p in [p4, p2, p1, p3]:
            heap.agregar(p)

        top = heap.obtener_top_k()
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].titulo, "Matrix")
        self.assertEqual(top[1].titulo, "Inception")
        self.assertEqual(top[2].titulo, "Interstellar")


if __name__ == "__main__":
    unittest.main()