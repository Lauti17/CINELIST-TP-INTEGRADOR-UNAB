class NodoAVL:
    def __init__(self, clave: str, valor):
        self.clave = clave.lower()
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo: NodoAVL) -> int:
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo: NodoAVL) -> int:
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho) if nodo else 0

    # --- ROTACIONES ---

    def _rotar_derecha(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierdo
        T2 = x.derecho

        # Realizar rotación
        x.derecho = y
        y.izquierdo = T2

        # Actualizar alturas
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        x.altura = 1 + max(self.obtener_altura(x.izquierdo), self.obtener_altura(x.derecho))

        return x

    def _rotar_izquierda(self, x: NodoAVL) -> NodoAVL:
        y = x.derecho
        T2 = y.izquierdo

        # Realizar rotación
        y.izquierdo = x
        x.derecho = T2

        # Actualizar alturas
        x.altura = 1 + max(self.obtener_altura(x.izquierdo), self.obtener_altura(x.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))

        return y

    # --- INSERCIÓN CON AUTO-BALANCE ---

    def insertar(self, clave: str, valor):
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo: NodoAVL, clave: str, valor) -> NodoAVL:
        clave_lower = clave.lower()

        if not nodo:
            return NodoAVL(clave, valor)

        if clave_lower < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave_lower > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            return nodo  # No duplicados

        # 1. Actualizar altura del nodo padre
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo), self.obtener_altura(nodo.derecho))

        # 2. Obtener el factor de balance
        balance = self.obtener_balance(nodo)

        # 3. Aplicar rotaciones si el nodo se desbalanceó

        # Caso Izquierda-Izquierda
        if balance > 1 and clave_lower < nodo.izquierdo.clave:
            return self._rotar_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and clave_lower > nodo.derecho.clave:
            return self._rotar_izquierda(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and clave_lower > nodo.izquierdo.clave:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and clave_lower < nodo.derecho.clave:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def buscar(self, clave: str):
        return self._buscar_recursivo(self.raiz, clave.lower())

    def _buscar_recursivo(self, nodo: NodoAVL, clave_lower: str):
        if nodo is None or nodo.clave == clave_lower:
            return nodo.valor if nodo else None

        if clave_lower < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave_lower)
        return self._buscar_recursivo(nodo.derecho, clave_lower)