# Gestión de proyecto — CineliList

- **Tablero**: [completar con el link real de Trello o GitHub Projects]
- **Metodología**: Scrum simplificado — un sprint por TP, columnas:
  `Backlog · En progreso · En revisión · Hecho`.
- **Integrantes**: Luciano Bazan, Lautaro Arola.

> Las retros están para completar con lo que realmente vivió el grupo: la
> rúbrica pide evidencia de uso del tablero a lo largo de toda la cursada.

## Sprint TP0 (Lanzamiento)

Historias:
- [x] Como equipo quiero elegir el universo para definir el alcance del proyecto.
  - Criterio: dominio justificado con datos disponibles.
- [x] Como equipo quiero una propuesta de 1 página para comunicar la idea.
  - Criterio: 5 funcionalidades + usuario objetivo concreto.
- [x] Como equipo quiero el repo y el tablero listos para empezar.
  - Criterio: README, `.gitignore` y primer commit en `main`.

**Retro TP0**: [qué salió bien / qué mejorar].

## Sprint TP1 (Objetos y clases)

Historias:
- [x] Como usuario quiero buscar una película por título para encontrarla rápido.
  - Criterio: la búsqueda no distingue mayúsculas; respuesta < 1 s.
- [x] Como usuario quiero ver la lista completa para explorar el catálogo.
- [x] Como usuario quiero filtrar por categoría para no recorrer todo a mano.
- [x] Como equipo quiero pruebas automatizadas de buscar, listar y filtrar.

**Retro TP1**: [qué salió bien / qué mejorar].

## Sprint TP2 (Complejidad)

Historias:
- [x] Como equipo quiero comparar búsqueda secuencial, binaria y BST para elegir con datos.
  - Criterio: misma consulta y mismo dataset, medido con `timeit`.
- [x] Como equipo quiero un generador de datasets para repetir el experimento.
  - Criterio: `datos/generar.py` con semilla fija, 100 a 100.000 elementos.
- [x] Como equipo quiero un informe con tabla, O/Ω/Θ y conclusión.
  - Criterio: [`tp2-experimentos.md`](tp2-experimentos.md) con números reales.

**Retro TP2**: [qué salió bien / qué mejorar].

## Sprint TP3 (Árbol binario de búsqueda)

Historias:
- [x] Como usuario quiero que la búsqueda por título sea rápida aunque crezca el catálogo.
  - Criterio: `Catalogo.buscar` usa `ArbolBST`; búsqueda O(log n) promedio.
- [x] Como usuario quiero ver el catálogo ordenado alfabéticamente.
  - Criterio: recorrido inorder (`listar_ordenado`).
- [x] Como equipo quiero pruebas del árbol (`tests/test_arbol.py`).

**Retro TP3**: [qué salió bien / qué mejorar].

## Sprint TP4 (AVL)

Historias:
- [x] Como equipo quiero evitar que el BST degrade a lista con datos ordenados.
  - Criterio: `ArbolAVL` con rotaciones; factor de balance en [-1, 1].
- [x] Como equipo quiero medir BST contra AVL en el peor caso.
  - Criterio: `experimento_avl.py` (5.000 títulos ordenados).
- [x] Como equipo quiero pruebas del AVL (`tests/test_avl.py`).
- [ ] Como equipo quiero que el `Catalogo` indexe con el AVL en vez del BST.

**Retro TP4**: [qué salió bien / qué mejorar].

## Sprint TP5 (Árbol general)

Historias:
- [x] Como usuario quiero explorar las categorías en jerarquía para descubrir géneros y subgéneros.
  - Criterio: `NodoNArio` + `GestorCategorias`, opción 4 del menú.
- [x] Como equipo quiero pruebas del árbol N-ario (`tests/test_arbol_nario.py`).

**Retro TP5**: [qué salió bien / qué mejorar].

## Sprint TP6 (Heap)

Historias:
- [x] Como usuario quiero ver el Top N de películas mejor valoradas.
  - Criterio: heap mínimo implementado a mano; no ordena todo el catálogo.
- [x] Como equipo quiero pruebas del heap (`tests/test_heap.py`).

**Retro TP6**: [qué salió bien / qué mejorar].

## Sprint TP7 (Grafos)

Historias:
- [x] Como usuario quiero ver películas relacionadas con una que me gustó para decidir qué ver después.
  - Criterio: opción 6 del menú; muestra el motivo y ordena por rating.
- [x] Como equipo quiero definir y justificar el modelo del grafo (vértice, arista, tipo y representación).
  - Criterio: [`tp7-grafo.md`](tp7-grafo.md) con lista de adyacencia justificada.
- [x] Como equipo quiero pruebas del grafo y de las relaciones (`tests/test_grafo.py`, `tests/test_relaciones.py`).

**Retro TP7**: [qué salió bien / qué mejorar].

## Sprint TP8 (Recorridos: BFS y DFS)

Historias:
- [x] Como usuario quiero ver el camino más corto entre dos películas para entender cómo se conectan.
  - Criterio: BFS; muestra todos los intermediarios y el motivo de cada paso; informa si no hay camino.
- [x] Como usuario quiero saber cuál es la película más cercana de otro género para salir de mi género habitual.
  - Criterio: BFS con condición; muestra el camino y la distancia.
- [x] Como usuario quiero explorar todo lo conectado a una película.
  - Criterio: DFS iterativo; sin repetidos; informa el total alcanzable.
- [x] Como equipo quiero comparar BFS y DFS con mediciones y análisis de complejidad.
  - Criterio: [`tp8-recorridos.md`](tp8-recorridos.md) con tablas reales.
- [x] Como equipo quiero pruebas de los recorridos (`tests/test_recorridos.py`).

**Retro TP8**: [qué salió bien / qué mejorar].

## Próximos sprints

- [ ] TP9: camino mínimo (Dijkstra).
- [ ] TP10: producto final, demo y defensa.
