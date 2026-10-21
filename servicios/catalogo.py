import json
from modelos.pelicula import Pelicula
from estructuras.arbol import ArbolBST


class Catalogo:
    """Lógica de negocio: carga y operaciones sobre el catálogo de CineliList."""

    def __init__(self) -> None:
        self._elementos: list[Pelicula] = []
        self._indice_arbol: ArbolBST = ArbolBST()

    def agregar_pelicula(self, pelicula: Pelicula) -> None:
        """Agrega una película tanto a la lista como al índice de árbol BST."""
        self._elementos.append(pelicula)
        self._indice_arbol.insertar(pelicula.titulo, pelicula)

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
        for item in datos:
            pelicula = Pelicula(item["titulo"], item["genero"], item["rating"])
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