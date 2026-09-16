import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from servicios.catalogo import Catalogo


class TestCatalogo(unittest.TestCase):
    def setUp(self):
        self.catalogo = Catalogo()
        self.catalogo.cargar_desde_json("datos/peliculas.json")

    def test_buscar_por_titulo(self):
        resultado = self.catalogo.buscar("matrix")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.titulo, "Matrix")

    def test_buscar_devuelve_none_si_no_existe(self):
        self.assertIsNone(self.catalogo.buscar("no-existe"))

    def test_listar_devuelve_todos(self):
        self.assertTrue(len(self.catalogo.listar()) > 0)

    def test_filtrar_por_genero(self):
        resultados = self.catalogo.filtrar("ciencia ficción")
        self.assertTrue(all(p.genero.lower() == "ciencia ficción" for p in resultados))


if __name__ == "__main__":
    unittest.main()
