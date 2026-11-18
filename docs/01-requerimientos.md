# Requerimientos — CineliList

## Alcance

CineliList es un sistema de recomendación de películas por terminal: permite
buscar una película por título, explorar categorías, ver el ranking de mejor
valoradas y, a medida que avanza el proyecto, descubrir películas relacionadas.
Está pensado para una persona de 20 a 35 años que, después de ver una película
que le encantó, quiere encontrar algo similar sin pasarse media hora
scrolleando plataformas de streaming.

## Propuesta (TP0)

- **Dominio:** películas. Hay datasets públicos con géneros, ratings y
  relaciones entre títulos, lo que da datos reales para toda la cursada. El
  dominio permite ordenar por título (BST/AVL), agrupar por género (árbol
  general), rankear un Top N (heap) y conectar películas relacionadas (grafo).
- **Problema:** "No sé qué película ver después de haber visto una que me
  encantó."
- **Usuario objetivo:** una persona de 20 a 35 años que quiere recomendaciones
  confiables en pocos pasos.

## Requerimientos funcionales (RF)

| ID | Requerimiento | Estado |
|---|---|---|
| RF01 | El sistema debe permitir buscar una película por título, sin distinguir mayúsculas | ✅ TP1 (BST en TP3) |
| RF02 | El sistema debe permitir listar las películas de una categoría (género) | ✅ TP1 |
| RF03 | El sistema debe mostrar el Top N de películas mejor rankeadas | ✅ TP6 |
| RF04 | El sistema debe mostrar las películas relacionadas con una dada | ✅ TP7 |
| RF05 | El sistema debe permitir encontrar el camino de menor costo entre dos películas, mostrando la secuencia completa de intermediarios | ⏳ TP9 |
| RF06 | El sistema debe sugerir películas a partir de una dada | ⏳ TP10 |
| RF07 | El sistema debe permitir explorar las categorías en forma de jerarquía (género y subgénero) | ✅ TP5 |
| RF08 | El sistema debe encontrar el camino con menos conexiones entre dos películas, mostrando todos los intermediarios | ✅ TP8 |
| RF09 | El sistema debe encontrar la película más cercana, de un género distinto, a una dada | ✅ TP8 |
| RF10 | El sistema debe mostrar todas las películas alcanzables a partir de una dada | ✅ TP8 |

### Criterios de aceptación

> **RF01 — Buscar por título**
> - "matrix" y "MATRIX" encuentran "Matrix".
> - Si el título no existe, el sistema informa que no lo encontró.
>
> **RF03 — Top N**
> - Se muestran exactamente N resultados (o todos los que existan si son menos).
> - El orden es descendente por rating.
> - Responde en menos de 1 segundo con 10.000 elementos (medido: ~1,3 ms con N = 10).
>
> **RF04 — Películas relacionadas**
> - Dado un título existente, se listan las películas que comparten director o género.
> - Cada resultado indica el motivo y se ordena de mayor a menor rating.
> - Si el título no existe, el sistema informa que no lo encontró.
>
> **RF08 — Camino con menos conexiones**
> - Se muestra la cadena completa, con el motivo de cada paso.
> - Ninguna otra cadena entre las dos películas tiene menos conexiones.
> - Si no existe cadena, el sistema lo informa.
>
> **RF09 — Más cercana de otro género**
> - La película recomendada es de un género distinto al de origen.
> - Se muestra el camino y a cuántas conexiones está.
>
> **RF10 — Explorar todo lo conectado**
> - Se listan todas las películas alcanzables, sin repetir, y cuántas son del total.
>
> **RF07 — Explorar categorías**
> - Se muestra el árbol completo de géneros con sus subcategorías.

## Requerimientos no funcionales (RNF)

| ID | Requerimiento | Verificación |
|---|---|---|
| RNF01 | La búsqueda por título debe ser logarítmica sobre el total de películas | ✅ [TP2](tp2-experimentos.md) y TP3 (BST) |
| RNF02 | El sistema debe soportar al menos 10.000 películas sin degradar la respuesta perceptiblemente | ✅ [TP2](tp2-experimentos.md) (probado hasta 100.000) |
| RNF03 | La interfaz debe ser usable por alguien que no conoce la implementación | Demo |
| RNF04 | El proyecto debe ejecutarse con Python 3.10+ sin instalaciones extra | ✅ README (matplotlib es opcional, solo para el gráfico) |
| RNF05 | El Top N no debe requerir ordenar todo el catálogo | ✅ TP6 (heap mínimo manual, O(n log k)) |

## Ejemplo de uso

```text
========================================
 🎬 CINELILIST — TERMINAL
========================================
1. Buscar película
2. Listar todas las películas
3. Filtrar por categoría
4. Explorar categorías
5. Ver Top N películas
6. Ver películas relacionadas
7. Camino más corto entre dos películas
8. Película más cercana de otro género
9. Explorar todo lo conectado a una película
0. Salir
----------------------------------------
Opción: 1
Título a buscar: matrix
Encontrada: Matrix (Ciencia Ficción) ⭐8.7
```

## Fuera de alcance

- Autenticación o perfiles de usuario.
- Persistencia de preferencias entre sesiones.
- Integración con APIs externas (TMDB, IMDb).

## Observaciones

- Búsqueda: se comparó secuencial, binaria y BST (ver
  [informe del TP2](tp2-experimentos.md)). El `Catalogo` busca con el BST.
- El AVL existe y se mide contra el BST en `experimento_avl.py`; el catálogo
  todavía no lo usa como índice.
- Relaciones: el grafo conecta películas que comparten director o género (ver
  [TP7](tp7-grafo.md)).
- Recorridos: BFS resuelve el camino más corto y la más cercana; DFS explora
  todo lo conectado (ver [TP8](tp8-recorridos.md)). RF05, el camino de menor
  *costo* (aristas con peso), queda para el TP9 con Dijkstra.
- El heap del Top N está implementado a mano (sin `heapq`), como pide la
  cátedra.
