import unittest
from estructuras.grafo import Grafo


class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g = Grafo()
        for nombre in ("A", "B", "C", "D"):
            self.g.agregar_vertice(nombre, f"valor {nombre}")
        self.g.agregar_arista("A", "B")
        self.g.agregar_arista("A", "C")

    def test_las_aristas_son_simetricas(self):
        self.assertTrue(self.g.conectados("A", "B"))
        self.assertTrue(self.g.conectados("B", "A"))
        self.assertFalse(self.g.conectados("B", "C"))

    def test_vecinos_y_grado(self):
        self.assertCountEqual(self.g.vecinos("A"), ["b", "c"])
        self.assertEqual(self.g.grado("A"), 2)
        self.assertEqual(self.g.grado("D"), 0)
        self.assertEqual(self.g.vecinos("no-existe"), [])

    def test_cantidad_de_vertices_y_aristas(self):
        self.assertEqual(len(self.g), 4)
        self.assertEqual(self.g.cantidad_aristas(), 2)

    def test_no_duplica_aristas_ni_acepta_lazos(self):
        self.g.agregar_arista("A", "B")
        self.g.agregar_arista("B", "A")
        self.g.agregar_arista("A", "A")
        self.assertEqual(self.g.cantidad_aristas(), 2)
        self.assertFalse(self.g.conectados("A", "A"))

    def test_claves_sin_distinguir_mayusculas(self):
        self.assertTrue(self.g.existe("a"))
        self.assertIn("B", self.g)
        self.assertEqual(self.g.obtener("a"), "valor A")

    def test_arista_con_vertice_inexistente_falla(self):
        with self.assertRaises(KeyError):
            self.g.agregar_arista("A", "Z")

    def test_peso_por_defecto_y_personalizado(self):
        self.g.agregar_arista("C", "D", peso=2.5)
        self.assertEqual(self.g.peso("A", "B"), 1.0)
        self.assertEqual(self.g.peso("D", "C"), 2.5)
        self.assertIsNone(self.g.peso("B", "D"))

    def test_agregar_vertice_existente_no_pisa_el_valor(self):
        self.g.agregar_vertice("a", "otro")
        self.assertEqual(self.g.obtener("A"), "valor A")


if __name__ == "__main__":
    unittest.main()
