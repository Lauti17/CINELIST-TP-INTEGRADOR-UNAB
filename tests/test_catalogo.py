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

    def test_buscar_binaria_encuentra_sin_distinguir_mayusculas(self):
        resultado = self.catalogo.buscar_binaria("MATRIX")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.titulo, "Matrix")

    def test_buscar_binaria_devuelve_none_si_no_existe(self):
        self.assertIsNone(self.catalogo.buscar_binaria("no-existe"))

    def test_las_tres_estrategias_coinciden(self):
        for pelicula in self.catalogo.listar():
            titulo = pelicula.titulo
            self.assertIs(self.catalogo.buscar_secuencial(titulo), pelicula)
            self.assertIs(self.catalogo.buscar_binaria(titulo), pelicula)
            self.assertIs(self.catalogo.buscar(titulo), pelicula)

    def test_ordenar_por_titulo_no_altera_el_orden_de_listar(self):
        antes = [p.titulo for p in self.catalogo.listar()]
        self.catalogo.ordenar_por_titulo()
        self.assertEqual(antes, [p.titulo for p in self.catalogo.listar()])

    def test_buscar_binaria_ve_peliculas_agregadas_despues(self):
        from modelos.pelicula import Pelicula
        self.catalogo.ordenar_por_titulo()
        nueva = Pelicula("Zzz Nueva", "Drama", 5.0)
        self.catalogo.agregar_pelicula(nueva)
        self.assertIs(self.catalogo.buscar_binaria("zzz nueva"), nueva)


if __name__ == "__main__":
    unittest.main()
