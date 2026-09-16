import json
from modelos.pelicula import Pelicula


class Catalogo:
    """Lógica de negocio: carga y operaciones sobre el catálogo de CineliList."""

    def __init__(self) -> None:
        self._elementos: list[Pelicula] = []

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
        for item in datos:
            self._elementos.append(
                Pelicula(item["titulo"], item["genero"], item["rating"])
            )

    def buscar(self, titulo: str) -> Pelicula | None:
        """Búsqueda por título, sin distinguir mayúsculas."""
        for pelicula in self._elementos:
            if pelicula.titulo.lower() == titulo.lower():
                return pelicula
        return None

    def listar(self) -> list[Pelicula]:
        return list(self._elementos)

    def filtrar(self, genero: str) -> list[Pelicula]:
        return [
            p for p in self._elementos
            if p.genero.lower() == genero.lower()
        ]

    def __len__(self) -> int:
        return len(self._elementos)
