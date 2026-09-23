class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave.lower()  # Normalizamos a minúsculas para buscar sin problemas
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