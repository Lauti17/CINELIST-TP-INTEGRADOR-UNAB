class Pelicula:
    """Representa un elemento del catálogo de CineliList."""

    def __init__(self, titulo: str, genero: str, rating: float, director: str = ""):
        self._titulo = titulo
        self._genero = genero
        self._rating = rating
        self._director = director

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def genero(self) -> str:
        return self._genero

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def director(self) -> str:
        return self._director

    def __repr__(self) -> str:
        return f"{self._titulo} ({self._genero}) ⭐{self._rating}"
