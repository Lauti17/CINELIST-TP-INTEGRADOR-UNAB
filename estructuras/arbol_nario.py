class NodoNArio:
    """Nodo para un Árbol General (N-ario) que almacena una lista de hijos."""

    def __init__(self, nombre: str, datos=None):
        self.nombre = nombre
        self.datos = datos if datos else []  # Películas asociadas a la categoría
        self.hijos: list['NodoNArio'] = []

    def agregar_hijo(self, hijo: 'NodoNArio'):
        self.hijos.append(hijo)

    def buscar(self, nombre_buscado: str) -> 'NodoNArio | None':
        """Búsqueda de un nodo por nombre dentro del árbol."""
        if self.nombre.lower() == nombre_buscado.lower():
            return self

        for hijo in self.hijos:
            resultado = hijo.buscar(nombre_buscado)
            if resultado:
                return resultado
        return None

    def mostrar_jerarquia(self, nivel: int = 0) -> str:
        """Devuelve un string formateado visualmente como un árbol jerárquico."""
        indentacion = "   " * nivel + ("└─ " if nivel > 0 else "")
        res = f"{indentacion}{self.nombre}\n"
        for hijo in self.hijos:
            res += hijo.mostrar_jerarquia(nivel + 1)
        return res