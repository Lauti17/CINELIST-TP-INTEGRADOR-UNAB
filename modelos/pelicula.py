class Pelicula:
    """Representa un elemento del catálogo de CineliList."""

    def __init__(self, titulo: str, genero: str, rating: float):
        self._titulo = titulo
        self._genero = genero
        self._rating = rating

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def genero(self) -> str:
        return self._genero

    @property
    def rating(self) -> float:
        return self._rating

    def __repr__(self) -> str:
        return f"{self._titulo} ({self._genero}) ⭐{self._rating}"
