import unittest
from modelos.pelicula import Pelicula
from estructuras.arbol import ArbolBST


class TestArbolBST(unittest.TestCase):

    def setUp(self):
        self.arbol = ArbolBST()
        self.p1 = Pelicula("Matrix", "Ciencia Ficción", 8.7)
        self.p2 = Pelicula("Inception", "Ciencia Ficción", 8.8)
        self.p3 = Pelicula("Titanic", "Drama", 7.9)

        self.arbol.insertar(self.p1.titulo, self.p1)
        self.arbol.insertar(self.p2.titulo, self.p2)
        self.arbol.insertar(self.p3.titulo, self.p3)

    def test_busqueda(self):
        resultado = self.arbol.buscar("Inception")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.titulo, "Inception")

    def test_recorrido_inorder(self):
        lista = self.arbol.inorder()
        titulos = [p.titulo for p in lista]
        self.assertEqual(titulos, ["Inception", "Matrix", "Titanic"])


if __name__ == "__main__":
    unittest.main()