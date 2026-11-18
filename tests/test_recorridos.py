import random
import unittest

from algoritmos.bfs import bfs, camino_mas_corto, distancias, mas_cercana
from algoritmos.dfs import camino_dfs, componentes_conexas, dfs
from estructuras.grafo import Grafo
from servicios.catalogo import Catalogo
from servicios.relaciones import Relaciones


def armar(aristas, vertices=()):
    g = Grafo()
    for nombre in {n for a in aristas for n in a} | set(vertices):
        g.agregar_vertice(nombre, nombre)
    for a, b in aristas:
        g.agregar_arista(a, b)
    return g


class TestBFS(unittest.TestCase):

    def setUp(self):
        # A-B, A-C, B-D, C-D, D-E (A y D tienen dos caminos de igual largo) y F aislado
        self.g = armar([("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "e")], vertices=["f"])

    def test_orden_por_niveles(self):
        self.assertEqual(bfs(self.g, "a"), ["a", "b", "c", "d", "e"])

    def test_no_visita_lo_inalcanzable(self):
        self.assertNotIn("f", bfs(self.g, "a"))

    def test_distancias(self):
        self.assertEqual(distancias(self.g, "a"), {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3})

    def test_camino_mas_corto(self):
        camino = camino_mas_corto(self.g, "a", "e")
        self.assertEqual(len(camino), 4)
        self.assertEqual(camino[0], "a")
        self.assertEqual(camino[-1], "e")

    def test_camino_elige_el_atajo(self):
        g = armar([("a", "b"), ("b", "c"), ("c", "d"), ("a", "d")])
        self.assertEqual(camino_mas_corto(g, "a", "d"), ["a", "d"])

    def test_sin_camino_devuelve_none(self):
        self.assertIsNone(camino_mas_corto(self.g, "a", "f"))

    def test_mismo_origen_y_destino(self):
        self.assertEqual(camino_mas_corto(self.g, "a", "a"), ["a"])

    def test_vertice_inexistente(self):
        self.assertEqual(bfs(self.g, "zzz"), [])
        self.assertEqual(distancias(self.g, "zzz"), {})
        self.assertIsNone(camino_mas_corto(self.g, "a", "zzz"))
        self.assertIsNone(camino_mas_corto(self.g, "zzz", "a"))

    def test_mas_cercana_que_cumple_una_condicion(self):
        camino = mas_cercana(self.g, "a", lambda valor: valor == "e")
        self.assertEqual(camino[0], "a")
        self.assertEqual(camino[-1], "e")
        self.assertEqual(len(camino), 4)
        self.assertIsNone(mas_cercana(self.g, "a", lambda valor: valor == "f"))

    def test_claves_sin_distinguir_mayusculas(self):
        self.assertEqual(camino_mas_corto(self.g, "A", "E"), camino_mas_corto(self.g, "a", "e"))

    def test_distancias_coinciden_con_floyd_warshall(self):
        """BFS tiene que dar la distancia mínima real: se compara contra Floyd-Warshall."""
        azar = random.Random(7)
        n = 14
        aristas = {tuple(sorted(azar.sample(range(n), 2))) for _ in range(18)}
        g = armar([(f"v{a}", f"v{b}") for a, b in aristas], vertices=[f"v{i}" for i in range(n)])

        inf = float("inf")
        d = [[0 if i == j else inf for j in range(n)] for i in range(n)]
        for a, b in aristas:
            d[a][b] = d[b][a] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        for i in range(n):
            dist = distancias(g, f"v{i}")
            for j in range(n):
                esperado = d[i][j]
                if esperado == inf:
                    self.assertNotIn(f"v{j}", dist)
                else:
                    self.assertEqual(dist[f"v{j}"], esperado)


class TestDFS(unittest.TestCase):

    def setUp(self):
        self.g = armar([("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "e")], vertices=["f"])

    def test_orden_en_profundidad(self):
        # a -> b -> d -> c (por d) -> e: avanza hasta el fondo antes de volver.
        self.assertEqual(dfs(self.g, "a"), ["a", "b", "d", "c", "e"])

    def test_visita_cada_vertice_una_vez(self):
        orden = dfs(self.g, "a")
        self.assertEqual(len(orden), len(set(orden)))
        self.assertNotIn("f", orden)

    def test_vertice_inexistente(self):
        self.assertEqual(dfs(self.g, "zzz"), [])
        self.assertIsNone(camino_dfs(self.g, "a", "zzz"))

    def test_camino_dfs_es_valido_pero_no_necesariamente_corto(self):
        # Cuadrado con una diagonal: BFS usa la diagonal (1 salto), DFS da la vuelta.
        g = armar([("a", "b"), ("b", "c"), ("c", "d"), ("a", "d")])
        camino = camino_dfs(g, "a", "d")
        self.assertEqual(camino[0], "a")
        self.assertEqual(camino[-1], "d")
        for x, y in zip(camino, camino[1:]):
            self.assertTrue(g.conectados(x, y))
        self.assertGreater(len(camino), len(camino_mas_corto(g, "a", "d")))

    def test_camino_dfs_sin_camino(self):
        self.assertIsNone(camino_dfs(self.g, "a", "f"))

    def test_componentes_conexas(self):
        componentes = componentes_conexas(self.g)
        self.assertEqual(sorted(len(c) for c in componentes), [1, 5])

    def test_no_se_rompe_con_un_grafo_muy_profundo(self):
        """Un camino de 5.000 vértices desbordaría una DFS recursiva."""
        n = 5000
        g = Grafo()
        for i in range(n):
            g.agregar_vertice(f"v{i}")
        for i in range(n - 1):
            g.agregar_arista(f"v{i}", f"v{i + 1}")
        self.assertEqual(len(dfs(g, "v0")), n)


class TestRecorridosConPeliculas(unittest.TestCase):

    def setUp(self):
        catalogo = Catalogo()
        catalogo.cargar_desde_json("datos/peliculas.json")
        self.relaciones = Relaciones(catalogo.listar())

    def test_camino_mas_corto_cruza_generos_por_director(self):
        camino = self.relaciones.camino_mas_corto("Matrix", "Whiplash")
        self.assertEqual([p.titulo for p in camino],
                         ["Matrix", "Terminator 2", "Titanic", "La La Land", "Whiplash"])

    def test_motivos_del_camino(self):
        camino = self.relaciones.camino_mas_corto("Matrix", "Whiplash")
        self.assertEqual(Relaciones.motivos_del_camino(camino),
                         ["mismo género", "mismo director", "mismo género", "mismo director"])

    def test_no_hay_camino_hacia_otra_componente(self):
        self.assertIsNone(self.relaciones.camino_mas_corto("Matrix", "Shrek"))

    def test_mas_cercana_de_otro_genero(self):
        camino = self.relaciones.mas_cercana_de_otro_genero("Matrix")
        self.assertEqual(len(camino), 3)
        self.assertEqual(camino[0].titulo, "Matrix")
        self.assertNotEqual(camino[-1].genero, "Ciencia Ficción")

    def test_mas_cercana_de_otro_genero_en_componente_aislada(self):
        self.assertIsNone(self.relaciones.mas_cercana_de_otro_genero("Shrek"))

    def test_explorar_en_profundidad_cubre_la_componente(self):
        titulos = [p.titulo for p in self.relaciones.explorar_en_profundidad("Matrix")]
        self.assertEqual(titulos[0], "Matrix")
        self.assertEqual(len(titulos), 33)
        self.assertIn("Whiplash", titulos)
        self.assertNotIn("Shrek", titulos)

    def test_bfs_gana_en_largo_de_camino(self):
        grafo = self.relaciones.grafo
        corto = camino_mas_corto(grafo, "Matrix", "Whiplash")
        largo = camino_dfs(grafo, "Matrix", "Whiplash")
        self.assertEqual(len(corto) - 1, 4)
        self.assertGreater(len(largo), len(corto))


if __name__ == "__main__":
    unittest.main()
