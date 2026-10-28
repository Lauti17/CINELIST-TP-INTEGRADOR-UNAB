import unittest
from modelos.pelicula import Pelicula
from servicios.catalogo import Catalogo
from servicios.relaciones import Relaciones, motivo_relacion


class TestMotivoRelacion(unittest.TestCase):

    def test_motivos(self):
        a = Pelicula("A", "Drama", 8.0, "Nolan")
        self.assertEqual(motivo_relacion(a, Pelicula("B", "Drama", 7.0, "Nolan")), "mismo director y género")
        self.assertEqual(motivo_relacion(a, Pelicula("C", "Acción", 7.0, "Nolan")), "mismo director")
        self.assertEqual(motivo_relacion(a, Pelicula("D", "Drama", 7.0, "Otro")), "mismo género")
        self.assertEqual(motivo_relacion(a, Pelicula("E", "Acción", 7.0, "Otro")), "")

    def test_sin_director_no_cuenta_como_mismo_director(self):
        a = Pelicula("A", "Drama", 8.0)
        b = Pelicula("B", "Acción", 7.0)
        self.assertEqual(motivo_relacion(a, b), "")


class TestRelaciones(unittest.TestCase):

    def setUp(self):
        catalogo = Catalogo()
        catalogo.cargar_desde_json("datos/peliculas.json")
        self.relaciones = Relaciones(catalogo.listar())

    def test_un_vertice_por_pelicula(self):
        self.assertEqual(len(self.relaciones.grafo), 45)

    def test_relacion_por_genero(self):
        titulos = [p.titulo for p, _ in self.relaciones.relacionadas("matrix")]
        self.assertIn("Inception", titulos)
        self.assertNotIn("Matrix", titulos)

    def test_relacion_por_director_entre_generos_distintos(self):
        # Nolan dirigió Inception (Ciencia Ficción) y El Caballero de la Noche (Acción)
        self.assertTrue(self.relaciones.estan_relacionadas("Inception", "Batman: El Caballero de la Noche"))
        # Cameron dirigió Terminator 2 (Ciencia Ficción) y Titanic (Romance)
        self.assertTrue(self.relaciones.estan_relacionadas("Terminator 2", "Titanic"))

    def test_la_relacion_es_simetrica(self):
        self.assertTrue(self.relaciones.estan_relacionadas("Titanic", "Terminator 2"))

    def test_peliculas_sin_relacion(self):
        self.assertFalse(self.relaciones.estan_relacionadas("Matrix", "Shrek"))

    def test_relacionadas_ordenadas_por_rating_descendente(self):
        ratings = [p.rating for p, _ in self.relaciones.relacionadas("Inception")]
        self.assertEqual(ratings, sorted(ratings, reverse=True))

    def test_titulo_inexistente_devuelve_lista_vacia(self):
        self.assertEqual(self.relaciones.relacionadas("no-existe"), [])


if __name__ == "__main__":
    unittest.main()
