# Diagrama de clases

> Estado: **TP8**. Se actualiza en cada etapa con la estructura nueva.
> Pendiente: Dijkstra (TP9).

```mermaid
classDiagram
    class Pelicula {
        -titulo: str
        -genero: str
        -rating: float
        -director: str
        +titulo() str
        +genero() str
        +rating() float
        +director() str
        +repr() str
    }
    class Catalogo {
        -elementos: list
        -indice_arbol: ArbolBST
        -claves_ordenadas: list
        +cargar_desde_json(ruta) None
        +agregar_pelicula(pelicula) None
        +buscar(titulo) Pelicula
        +buscar_secuencial(titulo) Pelicula
        +ordenar_por_titulo() None
        +buscar_binaria(titulo) Pelicula
        +listar() list
        +listar_ordenado() list
        +filtrar(genero) list
    }
    class ArbolBST {
        -raiz: NodoArbol
        +insertar(clave, valor) None
        +buscar(clave) Pelicula
        +inorder() list
        +preorder() list
        +postorder() list
    }
    class ArbolAVL {
        -raiz: NodoAVL
        +insertar(clave, valor) None
        +buscar(clave) Pelicula
        +obtener_altura(nodo) int
        +obtener_balance(nodo) int
    }
    class NodoNArio {
        -nombre: str
        -datos: list
        -hijos: list
        +agregar_hijo(hijo) None
        +buscar(nombre) NodoNArio
        +mostrar_jerarquia(nivel) str
    }
    class GestorCategorias {
        -raiz: NodoNArio
        +obtener_arbol_visual() str
        +asociar_pelicula(categoria, pelicula) bool
    }
    class MinHeapPeliculasManual {
        -k: int
        -heap: list
        +agregar(pelicula) None
        +obtener_top_k() list
    }
    class Recomendador {
        -peliculas: list
        +obtener_top_n(n) list
    }
    class Grafo {
        -valores: dict
        -adyacencia: dict
        +agregar_vertice(clave, valor) None
        +agregar_arista(a, b, peso) None
        +vecinos(clave) list
        +conectados(a, b) bool
        +peso(a, b) float
        +grado(clave) int
        +cantidad_aristas() int
    }
    class Relaciones {
        -grafo: Grafo
        +relacionadas(titulo) list
        +estan_relacionadas(a, b) bool
        +camino_mas_corto(a, b) list
        +mas_cercana_de_otro_genero(titulo) list
        +explorar_en_profundidad(titulo) list
    }
    class Bfs {
        <<modulo>>
        +bfs(grafo, origen) list
        +distancias(grafo, origen) dict
        +camino_mas_corto(grafo, origen, destino) list
        +mas_cercana(grafo, origen, condicion) list
    }
    class Dfs {
        <<modulo>>
        +dfs(grafo, origen) list
        +camino_dfs(grafo, origen, destino) list
        +componentes_conexas(grafo) list
    }
    class Terminal {
        -catalogo: Catalogo
        -gestor_categorias: GestorCategorias
        -relaciones: Relaciones
        +iniciar() None
    }

    Terminal --> Catalogo : usa
    Terminal --> GestorCategorias : usa
    Terminal ..> Recomendador : crea para el Top N
    Catalogo "1" o-- "*" Pelicula : contiene
    Catalogo --> ArbolBST : delega la búsqueda (TP3)
    ArbolBST "1" o-- "*" Pelicula : ordena por título
    ArbolAVL "1" o-- "*" Pelicula : ordena por título (TP4)
    GestorCategorias --> NodoNArio : raíz de la jerarquía (TP5)
    NodoNArio "1" o-- "*" NodoNArio : hijos
    NodoNArio "1" o-- "*" Pelicula : datos
    Recomendador --> MinHeapPeliculasManual : arma el Top N (TP6)
    Recomendador "1" o-- "*" Pelicula : recibe
    Terminal --> Relaciones : usa (opciones 6 a 9)
    Relaciones ..> Bfs : camino más corto y más cercana (TP8)
    Relaciones ..> Dfs : explorar en profundidad (TP8)
    Bfs ..> Grafo : recorre
    Dfs ..> Grafo : recorre
    Relaciones --> Grafo : arma y consulta (TP7)
    Grafo "1" o-- "*" Pelicula : un vértice por película
```

> `ArbolAVL` está implementado y se compara contra `ArbolBST` en
> `experimento_avl.py`; el `Catalogo` todavía indexa con el BST común.
