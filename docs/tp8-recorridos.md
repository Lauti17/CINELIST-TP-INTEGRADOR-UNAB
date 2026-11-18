# TP8 — Recorridos de grafos: BFS y DFS

## 1. Qué se implementó

| Algoritmo | Archivo | Funciones |
|---|---|---|
| BFS (búsqueda en anchura) | [`algoritmos/bfs.py`](../algoritmos/bfs.py) | `bfs`, `distancias`, `camino_mas_corto`, `mas_cercana` |
| DFS (búsqueda en profundidad) | [`algoritmos/dfs.py`](../algoritmos/dfs.py) | `dfs`, `camino_dfs`, `componentes_conexas` |

Ambos trabajan sobre el [grafo del TP7](tp7-grafo.md) (películas conectadas si
comparten director o género) y se usan desde `servicios/relaciones.py` y el menú.

## 2. Las dos consultas reales

### Consultas con BFS

> **"¿Cuál es el camino más corto entre dos películas?"**: opción **7** del menú.
>
> **"¿Cuál es la película más cercana de otro género?"**: opción **8** del menú.

**Por qué BFS:** todas las aristas valen lo mismo (1) y la pregunta es "la
menor cantidad de conexiones". BFS explora por niveles (primero a distancia 1,
después a distancia 2…), así que la primera vez que llega a una película lo
hace por un camino con la menor cantidad posible de aristas.

```text
Opción: 7
Película de origen: matrix
Película de destino: whiplash

--- Camino más corto: 4 conexiones ---
  Matrix
   → Terminator 2  (mismo género)
   → Titanic  (mismo director)
   → La La Land  (mismo género)
   → Whiplash  (mismo director)
```

```text
Opción: 8
Título de la película: matrix

--- La más cercana de otro género a Matrix (Ciencia Ficción) ---
  Matrix
   → Inception  (mismo género)
   → Batman: El Caballero de la Noche  (mismo director)

Recomendada: Batman: El Caballero de la Noche (Acción) ⭐9.0, a 2 conexiones.
```

Si no hay ninguna cadena que una las dos películas, el sistema lo informa:

```text
No existe camino entre 'Matrix' y 'Shrek': ninguna cadena de películas relacionadas las une.
```

### Consulta con DFS

> **"Explorá todo lo que está conectado con una película"**: opción **9** del menú.

**Por qué DFS:** la pregunta es "mostrame todo lo alcanzable", no importa la
distancia ni el orden. DFS avanza por un camino hasta el fondo y recién
entonces vuelve a probar otro; cubre todo el grupo conectado con una pila y
poca memoria.

```text
Opción: 9
Película de partida: matrix

--- Todo lo conectado con Matrix, explorado en profundidad ---
  1. Inception                           Ciencia Ficción
  2. Interstellar                        Ciencia Ficción
  ...
  7. Terminator 2                        Ciencia Ficción
  8. Titanic                             Romance
  9. La La Land                          Romance
 10. Whiplash                            Drama
 ...
Alcanzables: 32 de 44 películas.
```

Se nota que DFS "se mete hasta el fondo": desde *Terminator 2* salta a
*Titanic* (James Cameron), de ahí a *La La Land* y a *Whiplash* (Damien
Chazelle), y recién después vuelve a explorar el resto.

## 3. Cómo funciona cada uno

**BFS: cola (FIFO).** Se guarda el origen en una cola; mientras la cola no esté
vacía se saca el primero, se anotan sus vecinos no visitados y se encolan. Para
reconstruir el camino se guarda, por cada vértice, desde quién se lo descubrió.

**DFS: pila (LIFO).** Se apila el origen; mientras la pila no esté vacía se
saca el último, si no estaba visitado se lo visita y se apilan sus vecinos.
Está implementado de forma **iterativa** (con una pila explícita) y no
recursiva: una DFS recursiva falla con `RecursionError` en grafos profundos, y
hay un test con un camino de 5.000 vértices que lo verifica.

La cola de BFS es `collections.deque`: sacar del frente cuesta O(1), mientras
que con una lista (`pop(0)`) costaría O(n).

## 4. Complejidad

| | BFS | DFS |
|---|---|---|
| Tiempo (recorrido completo) | **O(V + E)** | **O(V + E)** |
| Memoria extra | O(V) (cola + visitados) | O(V) (pila + visitados) |
| Mejor caso de `camino_mas_corto` | Ω(1) (origen y destino son la misma película) | n/a |

**Por qué O(V + E):** cada vértice se encola (o apila) y se visita una sola vez
(gracias al conjunto de visitados), y cada arista se mira como mucho dos veces,
una desde cada extremo, porque el grafo es no dirigido. Con la **lista de
adyacencia** el costo de "ver los vecinos de un vértice" es proporcional a su
grado; con una matriz de adyacencia sería O(V) por vértice y el recorrido
completo O(V²). Esa es una de las razones por las que se eligió lista en el TP7.

## 5. Diferencias y cuándo conviene cada uno

| | BFS | DFS |
|---|---|---|
| Estructura auxiliar | Cola | Pila |
| Orden de exploración | Por niveles (cerca primero) | Hasta el fondo y vuelve |
| ¿Encuentra el camino con menos aristas? | **Sí, siempre** | **No** (encuentra *un* camino) |
| Memoria en el peor caso | El nivel más ancho del grafo | La profundidad máxima |
| Conviene para | Camino mínimo en aristas, "lo más cercano a…", distancias | Explorar todo lo alcanzable, componentes conexas, detectar si hay camino |

En CineliList:

- Para **"el camino más corto"** y **"el más cercano"** se usa BFS (opciones 7 y 8).
- Para **"todo lo conectado"** se usa DFS (opción 9). También sirve
  `componentes_conexas` para saber cuántos grupos aislados hay: hoy son 3
  (33, 6 y 6 películas).

## 6. Resultados

### 6.1 BFS contra DFS: largo del camino

Mismo origen (*Matrix*) y distintos destinos del dataset real. Cantidad de
conexiones del camino que devuelve cada algoritmo:

| Origen | Destino | BFS | DFS |
|---|---|---:|---:|
| Matrix | Inception | 1 | 1 |
| Matrix | Titanic | 2 | 8 |
| Matrix | Whiplash | 4 | 10 |
| Matrix | Gladiador | 3 | 11 |
| Matrix | Get Out | 5 | 11 |
| Matrix | Shrek | sin camino | sin camino |

DFS encuentra un camino válido, pero hasta **4 veces más largo** que el
mínimo (8 contra 2 para *Titanic*; 10 contra 4 para *Whiplash*). BFS es la
herramienta correcta cuando importa la distancia.

Para tener una idea de la forma del grafo, así se reparten las películas por
distancia a *Matrix*:

| Distancia | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Películas | 1 | 7 | 2 | 11 | 2 | 10 |

### 6.2 Escalabilidad

Recorrido completo (visita todos los vértices) sobre grafos sintéticos ralos
con E ≈ 4V aristas, midiendo con `timeit` (mejor de 5 repeticiones):

| Vértices (V) | Aristas (E) | BFS | DFS |
|---:|---:|---:|---:|
| 1.000 | 3.981 | 0,68 ms | 0,93 ms |
| 10.000 | 39.981 | 9,86 ms | 11,92 ms |
| 100.000 | 399.976 | 207,55 ms | 224,96 ms |

Al multiplicar V y E por 10, el tiempo de BFS se multiplica por ~14 (de 1.000
a 10.000) y por ~21 (de 10.000 a 100.000); el de DFS, por ~13 y ~19. Es más que
el 10 que predice O(V + E), pero está muy lejos del 100 que daría un costo
cuadrático. Una explicación probable son los efectos de memoria: con 100.000
vértices los diccionarios ya no entran en la caché del procesador. La
tendencia es **cercana a lineal**, como indica la teoría, aunque no perfecta.

> Medido en el entorno donde se generó este informe; los valores absolutos
> cambian según la máquina. Volvé a correr el script para obtener los tuyos.

## 7. Decisiones

- Los dos algoritmos devuelven **claves normalizadas** (minúsculas); la capa de
  servicio las convierte a `Pelicula` con `grafo.obtener(...)`.
- `mas_cercana` recibe una **condición** (una función), así el mismo BFS sirve
  para "la más cercana de otro género" y para cualquier otro criterio.
- `camino_dfs` existe para **comparar** contra BFS; la aplicación usa BFS
  siempre que se necesita un camino.
- El camino mínimo "con costo" (aristas con peso) es el TP9 (Dijkstra). Acá
  todas las aristas valen 1, por eso alcanza con BFS.

## 8. Pruebas y cómo reproducir

`tests/test_recorridos.py` cubre orden de visita, distancias, atajos, ausencia
de camino, vértices inexistentes, grafos muy profundos y películas reales. Un
test compara las distancias de BFS contra **Floyd–Warshall** en un grafo
aleatorio para comprobar que son mínimas.

```bash
python -m unittest discover tests
python algoritmos/experimentos/medicion_recorridos.py
```
