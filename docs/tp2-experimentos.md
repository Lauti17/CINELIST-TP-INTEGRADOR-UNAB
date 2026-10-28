# TP2 — Análisis de complejidad

## 1. Operación crítica elegida

**Búsqueda de una película por título** en el catálogo. Es la operación que el
usuario ejecuta con más frecuencia y la que justifica pasar de una lista a un
árbol (TP3) y a un árbol balanceado (TP4).

## 2. Estrategias comparadas

| ID | Estrategia | Implementación | Complejidad esperada |
|---|---|---|---|
| A | Secuencial | `Catalogo.buscar_secuencial` (recorre la lista) | O(n) |
| B | Binaria | `Catalogo.buscar_binaria` (`bisect` sobre lista ordenada por título) | O(log n) |
| C | BST | `Catalogo.buscar` (`ArbolBST.buscar`) | O(log n) promedio, O(n) peor caso |

## 3. Datos de prueba

Datasets sintéticos de 100, 1.000, 10.000 y 100.000 películas ("Pelicula 0" …
"Pelicula n-1"), con género y rating al azar y semilla fija (reproducible).

- Generador: [`datos/generar.py`](../datos/generar.py)
- Los archivos `datos/peliculas_N.json` no se suben al repo (el de 100.000 pesa
  ~8 MB): `medicion.py` los genera solo si no existen.

## 4. Método de medición

- `timeit`: 20 ejecuciones × 5 repeticiones, se toma el **mejor** tiempo por llamada.
- Una llamada de warm-up antes de cronometrar.
- Se mide **solo la consulta**: la carga del JSON y el ordenamiento
  (`ordenar_por_titulo`, una sola vez) quedan fuera del cronómetro.
- Mismo dataset y mismo elemento buscado en las tres estrategias: el último
  ("Pelicula n-1"), que existe en las tres.
- Script: [`algoritmos/experimentos/medicion.py`](../algoritmos/experimentos/medicion.py)

```bash
python algoritmos/experimentos/medicion.py
```

> **Nota metodológica:** `buscar_binaria` guarda la lista de claves ordenadas y
> la reutiliza. Si se reconstruyera en cada llamada, la "binaria" cargaría un
> costo O(n) escondido y la medición mentiría.

## 5. Resultados

| N elementos | Secuencial | Binaria | BST | Crecimiento secuencial |
|---|---:|---:|---:|---:|
| 100 | 0,0089 ms | 0,0003 ms | 0,0014 ms | base |
| 1.000 | 0,0884 ms | 0,0003 ms | 0,0021 ms | ~10x |
| 10.000 | 0,9377 ms | 0,0003 ms | 0,0027 ms | ~11x |
| 100.000 | 10,3978 ms | 0,0004 ms | 0,0033 ms | ~11x |

> Medido en el entorno donde se generó este informe. Los valores absolutos
> cambian en cada máquina; lo que se mantiene es la **tendencia**. Volvé a
> correr el script en tu equipo y reemplazá la tabla con tus números.

![Resultados TP2](capturas/experimento-tp2.png)

En escala log-log, la secuencial es una recta de pendiente 1 (lineal) y la
binaria es casi horizontal (logarítmica).

## 6. Análisis de complejidad

| Estrategia | Peor caso O() | Mejor caso Ω() | Caso típico Θ() |
|---|---|---|---|
| Secuencial | O(n) | Ω(1) (está primero) | Θ(n) (~n/2 comparaciones) |
| Binaria | O(log n) | Ω(1) (está en el medio) | Θ(log n) |
| Ordenar antes de la binaria (una vez) | O(n log n) | Ω(n log n) | Se paga una vez y se amortiza |
| BST | O(n) (árbol degenerado) | Ω(1) (está en la raíz) | Θ(log n) con inserciones al azar |

La búsqueda secuencial recorre la lista hasta encontrar el elemento: en el peor
caso recorre los n elementos (O(n)). La búsqueda binaria descarta la mitad del
espacio en cada paso: a lo sumo log2(n) comparaciones (O(log n)), pero requiere
que la lista esté ordenada (O(n log n) al cargar, una sola vez).

**Sobre el BST con nuestros datos.** Los títulos del dataset se insertan casi
en orden ("Pelicula 0", "Pelicula 1", …), que es la situación incómoda para un
BST sin balanceo. Altura medida: 20 con n = 100, 30 con n = 1.000, 40 con
n = 10.000 y 50 con n = 100.000, contra una altura ideal de ~7, ~10, ~13 y
~17. Sigue creciendo despacio, pero ~3 veces por encima de lo ideal. Por eso el
BST resultó más lento que la binaria en la tabla, y por eso existe el AVL
(TP4), que garantiza altura O(log n) aunque los datos lleguen ordenados.

## 7. Conclusión

1. **Qué se comparó:** la misma operación (buscar por título), sobre los mismos
   datos y en las mismas condiciones, con tres estrategias.
2. **Qué dice la tabla:** cuando n crece 10 veces, la secuencial tarda ~10 veces
   más (de 0,09 ms a 10,40 ms entre 1.000 y 100.000). La binaria y el BST casi
   no se mueven (menos de 0,01 ms en todos los tamaños).
3. **Por qué:** O(n) contra O(log n). Pasar de 1.000 a 100.000 elementos suma
   solo ~7 comparaciones a la binaria, pero multiplica por 100 el trabajo de la
   secuencial.
4. **Cuál conviene:** para un catálogo que se consulta seguido por título y no
   cambia en cada consulta, conviene una estructura ordenada: el costo de
   ordenar se paga una vez y se amortiza. La binaria es la más rápida y simple,
   pero necesita volver a ordenar si el catálogo cambia. El BST permite
   insertar sin reordenar todo, a cambio de depender de que no se desbalancee
   (por eso el siguiente paso es el AVL). La secuencial solo se justifica con
   listas muy chicas: con 100 elementos las tres "andan igual", y eso también
   es un dato.
5. **Qué se aprende:** la complejidad asintótica predice bien la tendencia, pero
   las constantes y el balance del árbol importan: un BST sin balancear puede
   quedar por detrás de una binaria sobre lista ordenada.

## 8. Reproducir el experimento

```bash
python datos/generar.py                          # opcional: genera los datasets
python algoritmos/experimentos/medicion.py       # imprime la tabla y guarda el gráfico
python experimento_avl.py                        # BST desbalanceado vs AVL
```

El gráfico requiere `matplotlib` (`pip install matplotlib`); sin él, el script
imprime igual la tabla.
