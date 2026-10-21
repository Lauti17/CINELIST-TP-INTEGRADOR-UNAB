import sys
import time
from modelos.pelicula import Pelicula
from estructuras.arbol import ArbolBST
from estructuras.avl import ArbolAVL

# Elevamos el límite de recursión de Python para evitar el crash en el BST degenerado
sys.setrecursionlimit(20000)


def ejecutar_prueba_desbalance():
    n = 5000
    print(f"Generando dataset ORDENADO de {n} elementos (Peor Caso)...")
    peliculas_ordenadas = [
        Pelicula(titulo=f"Pelicula_{i:05d}", genero="Acción", rating=8.0)
        for i in range(n)
    ]

    arbol_bst = ArbolBST()
    arbol_avl = ArbolAVL()

    # Insertar en orden alfabético
    for p in peliculas_ordenadas:
        arbol_bst.insertar(p.titulo, p)
        arbol_avl.insertar(p.titulo, p)

    # Buscamos el último elemento (peor caso)
    objetivo = f"Pelicula_{(n-1):05d}"

    # 1. Búsqueda en BST (degenerado en lista)
    inicio = time.perf_counter()
    _ = arbol_bst.buscar(objetivo)
    fin = time.perf_counter()
    tiempo_bst = (fin - inicio) * 1000

    # 2. Búsqueda en AVL (auto-balanceado)
    inicio = time.perf_counter()
    _ = arbol_avl.buscar(objetivo)
    fin = time.perf_counter()
    tiempo_avl = (fin - inicio) * 1000

    print("\n" + "=" * 65)
    print(f"{'ESTRATEGIA':<25} | {'ALTURA ESTIMADA':<15} | {'TIEMPO BÚSQUEDA':<15}")
    print("=" * 65)
    print(f"{'BST Común (Desbalanceado)':<25} | {n:<15} | {tiempo_bst:.4f} ms")
    print(f"{'AVL (Auto-balanceado)':<25} | {'~13':<15} | {tiempo_avl:.4f} ms")
    print("=" * 65)


if __name__ == "__main__":
    ejecutar_prueba_desbalance()