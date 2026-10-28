class Grafo:
    """Grafo no dirigido con lista de adyacencia (diccionario de diccionarios).

    - Vértice: una clave (str, se normaliza a minúsculas) con un valor asociado,
      por ejemplo la `Pelicula`.
    - Arista: relación simétrica entre dos vértices, con un peso (1.0 por defecto).
      TP7 las usa sin peso (todas valen 1); el peso queda listo para Dijkstra (TP9).

    Representación: `_adyacencia[a][b] = peso`, y lo mismo en `_adyacencia[b][a]`.
    Memoria O(V + E); recorrer los vecinos de un vértice cuesta O(grado).
    """

    def __init__(self) -> None:
        self._valores: dict[str, object] = {}
        self._adyacencia: dict[str, dict[str, float]] = {}

    @staticmethod
    def _clave(clave: str) -> str:
        return clave.lower()

    def agregar_vertice(self, clave: str, valor=None) -> None:
        """Agrega un vértice. Si ya existe, no hace nada. O(1)."""
        k = self._clave(clave)
        if k not in self._valores:
            self._valores[k] = valor
            self._adyacencia[k] = {}

    def agregar_arista(self, a: str, b: str, peso: float = 1.0) -> None:
        """Conecta dos vértices existentes (en ambos sentidos). O(1).

        Ignora los lazos (un vértice conectado consigo mismo). Si la arista ya
        existía, actualiza el peso.
        """
        ka, kb = self._clave(a), self._clave(b)
        if ka not in self._valores or kb not in self._valores:
            raise KeyError("Los dos vértices deben existir antes de conectarlos")
        if ka == kb:
            return
        self._adyacencia[ka][kb] = peso
        self._adyacencia[kb][ka] = peso

    def existe(self, clave: str) -> bool:
        return self._clave(clave) in self._valores

    def obtener(self, clave: str):
        """Devuelve el valor asociado al vértice (o None si no existe)."""
        return self._valores.get(self._clave(clave))

    def vecinos(self, clave: str) -> list[str]:
        """Claves de los vértices conectados a `clave`. O(grado)."""
        return list(self._adyacencia.get(self._clave(clave), {}))

    def peso(self, a: str, b: str) -> float | None:
        """Peso de la arista a-b, o None si no están conectados."""
        return self._adyacencia.get(self._clave(a), {}).get(self._clave(b))

    def conectados(self, a: str, b: str) -> bool:
        return self.peso(a, b) is not None

    def grado(self, clave: str) -> int:
        return len(self._adyacencia.get(self._clave(clave), {}))

    def vertices(self) -> list[str]:
        return list(self._valores)

    def cantidad_aristas(self) -> int:
        """Cada arista está guardada dos veces, por eso se divide por 2."""
        return sum(len(v) for v in self._adyacencia.values()) // 2

    def __len__(self) -> int:
        return len(self._valores)

    def __contains__(self, clave: str) -> bool:
        return self.existe(clave)
