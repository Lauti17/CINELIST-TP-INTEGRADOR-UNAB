from algoritmos.bfs import camino_mas_corto, mas_cercana
from algoritmos.dfs import dfs
from estructuras.grafo import Grafo
from modelos.pelicula import Pelicula


def motivo_relacion(a: Pelicula, b: Pelicula) -> str:
    """Por qué dos películas están relacionadas ("" si no lo están).

    Regla de CineliList: hay arista si comparten director o comparten género.
    """
    mismo_director = bool(a.director) and a.director.lower() == b.director.lower()
    mismo_genero = a.genero.lower() == b.genero.lower()
    if mismo_director and mismo_genero:
        return "mismo director y género"
    if mismo_director:
        return "mismo director"
    if mismo_genero:
        return "mismo género"
    return ""


class Relaciones:
    """Arma y consulta el grafo de relaciones entre películas (TP7).

    - Vértice: una película.
    - Arista: comparten director o género (no dirigido, todas valen 1).
    """

    def __init__(self, peliculas: list[Pelicula]) -> None:
        self._grafo = Grafo()
        self._construir(peliculas)

    @property
    def grafo(self) -> Grafo:
        return self._grafo

    def _construir(self, peliculas: list[Pelicula]) -> None:
        for p in peliculas:
            self._grafo.agregar_vertice(p.titulo, p)

        # Se agrupa por género y por director y se conecta cada grupo entre sí.
        # Costo O(V + suma de g²) en vez de comparar todos contra todos (O(V²)).
        grupos: dict[tuple[str, str], list[Pelicula]] = {}
        for p in peliculas:
            grupos.setdefault(("genero", p.genero.lower()), []).append(p)
            if p.director:
                grupos.setdefault(("director", p.director.lower()), []).append(p)

        for miembros in grupos.values():
            for i, a in enumerate(miembros):
                for b in miembros[i + 1:]:
                    self._grafo.agregar_arista(a.titulo, b.titulo)

    def relacionadas(self, titulo: str) -> list[tuple[Pelicula, str]]:
        """Películas conectadas a `titulo`, con el motivo, de mejor a peor rating.

        Devuelve [] si el título no existe o no tiene relaciones.
        """
        origen = self._grafo.obtener(titulo)
        if origen is None:
            return []
        resultado = []
        for clave in self._grafo.vecinos(titulo):
            otra = self._grafo.obtener(clave)
            resultado.append((otra, motivo_relacion(origen, otra)))
        resultado.sort(key=lambda par: (-par[0].rating, par[0].titulo.lower()))
        return resultado

    def estan_relacionadas(self, titulo_a: str, titulo_b: str) -> bool:
        return self._grafo.conectados(titulo_a, titulo_b)

    def _a_peliculas(self, claves: list[str]) -> list[Pelicula]:
        return [self._grafo.obtener(clave) for clave in claves]

    def camino_mas_corto(self, titulo_a: str, titulo_b: str) -> list[Pelicula] | None:
        """Cadena de películas con menos conexiones entre dos títulos (BFS).

        Incluye las dos puntas. Devuelve None si algún título no existe o si no
        hay ninguna cadena que las una.
        """
        camino = camino_mas_corto(self._grafo, titulo_a, titulo_b)
        return None if camino is None else self._a_peliculas(camino)

    def mas_cercana_de_otro_genero(self, titulo: str) -> list[Pelicula] | None:
        """Camino hasta la película más cercana de un género distinto al de `titulo` (BFS).

        El último elemento del camino es esa película. None si no hay ninguna conectada.
        """
        origen = self._grafo.obtener(titulo)
        if origen is None:
            return None
        genero = origen.genero.lower()
        camino = mas_cercana(self._grafo, titulo, lambda p: p.genero.lower() != genero)
        return None if camino is None else self._a_peliculas(camino)

    def explorar_en_profundidad(self, titulo: str) -> list[Pelicula]:
        """Todas las películas alcanzables desde `titulo`, en orden DFS (la primera es el origen)."""
        return self._a_peliculas(dfs(self._grafo, titulo))

    @staticmethod
    def motivos_del_camino(camino: list[Pelicula]) -> list[str]:
        """Motivo de cada paso del camino (uno menos que películas)."""
        return [motivo_relacion(a, b) for a, b in zip(camino, camino[1:])]
