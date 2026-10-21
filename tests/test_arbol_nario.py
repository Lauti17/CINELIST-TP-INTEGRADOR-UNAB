import unittest
from estructuras.arbol_nario import NodoNArio


class TestArbolNArio(unittest.TestCase):

    def test_construccion_y_busqueda(self):
        raiz = NodoNArio("Películas")
        scifi = NodoNArio("Ciencia Ficción")
        cyberpunk = NodoNArio("Cyberpunk")

        scifi.agregar_hijo(cyberpunk)
        raiz.agregar_hijo(scifi)

        nodo_encontrado = raiz.buscar("Cyberpunk")
        self.assertIsNotNone(nodo_encontrado)
        self.assertEqual(nodo_encontrado.nombre, "Cyberpunk")


if __name__ == "__main__":
    unittest.main()