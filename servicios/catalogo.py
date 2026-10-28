import bisect
import json
from modelos.pelicula import Pelicula
from estructuras.arbol import ArbolBST


class Catalogo:
    """Lógica de negocio: carga y operaciones sobre el catálogo de CineliList."""

    def __init__(self) -> None:
        self._elementos: list[Pelicula] = []
        self._indice_arbol: ArbolBST = ArbolBST()
        # Índice ordenado para la búsqueda binaria (TP2). Se arma una sola vez
        # y se invalida cuando se agrega una película.
        self._claves_ordenadas: list[str] | None = None
        self._peliculas_ordenadas: list[Pelicula] | None = None

    def agregar_pelicula(self, pelicula: Pelicula) -> None:
        """Agrega una película tanto a la lista como al índice de árbol BST."""
        self._elementos.append(pelicula)
        self._indice_arbol.insertar(pelicula.titulo, pelicula)
        self._claves_ordenadas = None
        self._peliculas_ordenadas = None

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
        for item in datos:
            pelicula = Pelicula(
                item["titulo"], item["genero"], item["rating"], item.get("director", "")
            )
            self.agregar_pelicula(pelicula)

    def buscar(self, titulo: str) -> Pelicula | None:
        """Búsqueda optimizada por título O(log N) utilizando el Árbol BST."""
        return self._indice_arbol.buscar(titulo)

    def buscar_secuencial(self, titulo: str) -> Pelicula | None:
        """Búsqueda lineal O(N) mantenida para comparaciones y pruebas."""
        for pelicula in self._elementos:
            if pelicula.titulo.lower() == titulo.lower():
                return pelicula
        return None

    def ordenar_por_titulo(self) -> None:
        """Arma una sola vez el índice ordenado por título, O(n log n).

        No modifica el orden de la lista original (`listar` sigue igual).
        """
        ordenadas = sorted(self._elementos, key=lambda p: p.titulo.lower())
        self._peliculas_ordenadas = ordenadas
        self._claves_ordenadas = [p.titulo.lower() for p in ordenadas]

    def buscar_binaria(self, titulo: str) -> Pelicula | None:
        """Búsqueda binaria por título sobre el índice ordenado, O(log N).

        Si el índice no está armado todavía, lo arma una única vez.
        """
        if self._claves_ordenadas is None:
            self.ordenar_por_titulo()
        clave = titulo.lower()
        indice = bisect.bisect_left(self._claves_ordenadas, clave)
        if indice < len(self._claves_ordenadas) and self._claves_ordenadas[indice] == clave:
            return self._peliculas_ordenadas[indice]
        return None

    def listar(self) -> list[Pelicula]:
        return list(self._elementos)

    def listar_ordenado(self) -> list[Pelicula]:
        """Devuelve las películas ordenadas alfabéticamente usando el recorrido inorder del BST."""
        return self._indice_arbol.inorder()

    def filtrar(self, genero: str) -> list[Pelicula]:
        return [
            p for p in self._elementos
            if p.genero.lower() == genero.lower()
        ]

    def __len__(self) -> int:
        return len(self._elementos)