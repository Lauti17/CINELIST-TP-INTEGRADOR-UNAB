# CineliList — Propuesta (TP0)

Sistema de recomendación de películas que permite buscar, ordenar y descubrir
películas a partir de una que ya viste.

## 1. Dominio elegido y justificación

Dominio: **películas**.

Elegimos este dominio porque hay datasets públicos de películas con géneros,
ratings y relaciones entre sí (secuelas, mismo director, mismo género), lo que
da datos reales para toda la cursada. El dominio permite ordenar por rating
(BST/AVL), agrupar por género (jerarquía para el árbol general), rankear un
Top N (heap) y conectar películas relacionadas (grafo).

## 2. Problema que resuelve

"No sé qué película ver después de haber visto una que me encantó."

## 3. Usuario objetivo

Una persona de 20-35 años que después de ver una película quiere encontrar
algo similar sin pasarse media hora scrolleando plataformas de streaming.

## 4. Funcionalidades iniciales

| ID | Funcionalidad |
|---|---|
| F1 | Buscar una película por título |
| F2 | Listar películas de una categoría (género) |
| F3 | Ver el Top 10 mejor rankeadas |
| F4 | Ver películas relacionadas con una dada |
| F5 | Sugerir películas a partir de una dada |

## 5. Ejemplo de uso (input/output)

```text
========================================
 🎬 CINELILIST — TERMINAL
========================================
1. Buscar elemento
2. Explorar categorías
3. Ver Top 10
4. Ver elementos relacionados
5. Encontrar camino
0. Salir
----------------------------------------
Opción: 1
Título a buscar: Matrix

Encontrada: Matrix (Ciencia Ficción) ⭐8.7
```

## 6. Requerimientos (borrador)

> Los requerimientos formales (RF / RNF) se completan con más detalle a lo
> largo del TP.

| ID | Requerimiento | Tipo |
|---|---|---|
| RF01 | El sistema debe permitir buscar una película por título | Funcional |
| RF02 | El sistema debe permitir listar películas de un género | Funcional |
| RF03 | El sistema debe mostrar el Top N de películas mejor rankeadas | Funcional |
| RF04 | El sistema debe sugerir películas relacionadas a una dada | Funcional |
| RF05 | El sistema debe permitir encontrar el camino de menor costo entre dos películas | Funcional |
| RNF01 | La búsqueda debe mantener respuesta aceptable con +1.000 elementos | No funcional |

## 7. Fuera de alcance (por ahora)

- No hay autenticación ni perfiles de usuario.
- No hay persistencia de preferencias entre sesiones.
- No se integra con APIs externas (TMDB, IMDb).
