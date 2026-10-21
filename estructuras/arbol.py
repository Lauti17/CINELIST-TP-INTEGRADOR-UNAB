class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave.lower()
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave: str, valor):
        if not self.raiz:
            self.raiz = NodoArbol(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo: NodoArbol, clave: str, valor):
        clave_lower = clave.lower()
        if clave_lower < nodo.clave:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave_lower > nodo.clave:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.derecho, clave, valor)

    def buscar(self, clave: str):
        return self._buscar_recursivo(self.raiz, clave.lower())

    def _buscar_recursivo(self, nodo: NodoArbol, clave_lower: str):
        if nodo is None or nodo.clave == clave_lower:
            return nodo.valor if nodo else None

        if clave_lower < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave_lower)
        return self._buscar_recursivo(nodo.derecho, clave_lower)

    # --- RECORRIDOS OBLIGATORIOS ---

    def inorder(self) -> list:
        """Devuelve los elementos ordenados alfabéticamente (Izquierda, Raíz, Derecha)."""
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo: NodoArbol, resultado: list):
        if nodo:
            self._inorder_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, resultado)

    def preorder(self) -> list:
        """Recorrido Raíz, Izquierda, Derecha."""
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo: NodoArbol, resultado: list):
        if nodo:
            resultado.append(nodo.valor)
            self._preorder_recursivo(nodo.izquierdo, resultado)
            self._preorder_recursivo(nodo.derecho, resultado)

    def postorder(self) -> list:
        """Recorrido Izquierda, Derecha, Raíz."""
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo: NodoArbol, resultado: list):
        if nodo:
            self._postorder_recursivo(nodo.izquierdo, resultado)
            self._postorder_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)