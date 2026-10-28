import unittest
from estructuras.avl import ArbolAVL
from modelos.pelicula import Pelicula


class TestArbolAVL(unittest.TestCase):

    def test_busqueda_sin_distinguir_mayusculas(self):
        arbol = ArbolAVL()
        p = Pelicula("Matrix", "Ciencia Ficción", 8.7)
        arbol.insertar(p.titulo, p)
        self.assertIs(arbol.buscar("MATRIX"), p)
        self.assertIsNone(arbol.buscar("no-existe"))

    def test_se_mantiene_balanceado_con_datos_ordenados(self):
        """El peor caso del BST (inserción ordenada) no desbalancea al AVL."""
        arbol = ArbolAVL()
        n = 1023
        for i in range(n):
            titulo = f"{i:05d}"
            arbol.insertar(titulo, Pelicula(titulo, "Drama", 5.0))
        # Un árbol perfecto de 1023 nodos tiene altura 10; AVL permite poco más.
        self.assertLessEqual(arbol.obtener_altura(arbol.raiz), 11)

    def test_factor_de_balance_en_todos_los_nodos(self):
        arbol = ArbolAVL()
        for i in range(200):
            titulo = f"{i:04d}"
            arbol.insertar(titulo, Pelicula(titulo, "Drama", 5.0))

        def verificar(nodo):
            if nodo is None:
                return
            self.assertLessEqual(abs(arbol.obtener_balance(nodo)), 1)
            verificar(nodo.izquierdo)
            verificar(nodo.derecho)

        verificar(arbol.raiz)

    def test_no_inserta_duplicados(self):
        arbol = ArbolAVL()
        a = Pelicula("Matrix", "Ciencia Ficción", 8.7)
        b = Pelicula("matrix", "Ciencia Ficción", 1.0)
        arbol.insertar(a.titulo, a)
        arbol.insertar(b.titulo, b)
        self.assertIs(arbol.buscar("matrix"), a)


if __name__ == "__main__":
    unittest.main()
