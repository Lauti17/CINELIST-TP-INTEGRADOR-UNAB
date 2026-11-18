# Guía del Demo Day 🎤

> **Objetivo:** que el grupo llegue a la defensa final (Parte VIII) sin improvisar. Son 7 a 10 minutos divididos en 4 partes: presentación (1′), demo (3′), parte técnica (3′) y desafío sorpresa. Todos los integrantes deben poder explicar cualquier parte del sistema: no existe "el que hizo los grafos".
>
> La defensa pesa **10 puntos directos** en la rúbrica, y la forma de exponer afecta la percepción de casi todos los demás criterios.

## Contenido

1. [El guion completo (7–10 minutos)](#1-el-guion-completo)
2. [La demo (3 min): reglas de oro](#2-la-demo-3-min--reglas-de-oro)
3. [La parte técnica (3 min): el mapa del sistema](#3-la-parte-técnica-3-min--el-mapa-del-sistema)
4. [Reparto de roles y práctica](#4-reparto-de-roles-y-práctica)
5. [Banco de preguntas con respuestas modelo](#5-banco-de-preguntas-con-respuestas-modelo)
6. [El desafío sorpresa: cómo entrenar](#6-el-desafío-sorpresa--cómo-entrenar)
7. [Checklist del día de la defensa](#7-checklist-del-día-de-la-defensa)
8. [Errores comunes en defensas](#8-errores-comunes-en-defensas)

## 1. El guion completo

| Minuto | Qué pasa | Quién habla |
|---|---|---|
| 0:00–1:00 | Presentación: problema + usuario + solución en 60 segundos | 1 persona |
| 1:00–4:00 | Demo en vivo: el menú, una búsqueda, el Top 10, un camino | 1 persona maneja el teclado |
| 4:00–7:00 | Parte técnica: dónde está cada estructura, complejidades, por qué eligieron eso | TODOS rotan |
| 7:00–10:00 | Preguntas + desafío sorpresa | Quien corresponda, sin miedo a rotar |

**Minuto 1 (presentación): la frase.** Empezá con el problema, no con la app. Plantilla:

> "[Problema en una oración], y construimos [Nombre], un sistema para resolver [problema] para [usuario objetivo]. Hoy te muestro cómo elige estructuras reales para [qué hace distinto]."

Resistí la tentación de leer: mirá al jurado, usá una sola tarjeta mental con 3 puntos (problema, usuario, solución), y tirá la pelota al teclado.

## 2. La demo (3 min): reglas de oro

La demo es **en vivo, sobre la aplicación real** (Parte 8.2: no capturas ni videos).

1. **Prepará el escenario:** datos cargados, terminal limpia, repo con `git pull` al día, `main` funcional. Corré el programa una vez completa antes de empezar para matar sorpresas.
2. **Mostrá consultas cortas y con salida clara:** un menú, una búsqueda, el Top 10, y un camino entre dos elementos (el momento "wow" de la demo). Elegí los elementos de antemano y que existan en tu dataset.
3. **Cronometrá:** 3 minutos pasan rápido. Guion sugerido:
   - 0:30 → arranque + menú
   - 1:00 → buscar un elemento
   - 1:30 → Top 10
   - 2:00 → mostrar un camino / conexión (lo más vistoso)
   - 0:15 → "cerramos acá porque el tiempo vuela" (algo preparado por si quedó tiempo)
4. **Si falla algo:** que un integrante tenga el plan B (recargar datos, o correr con el dataset chico). Hablar mientras se recupera ("esto pasa si el dataset no está cargado, fíjense...") muestra dominio, no miedo.
5. **Datos reales:** una demo con 10 películas inventadas se nota. Con 1.000+ elementos también se nota, pero para bien.

## 3. La parte técnica (3 min): el mapa del sistema

La pregunta del jurado: ¿dónde está el árbol? ¿el heap? ¿el grafo? Respondé con el diagrama [`04-diagrama-datos.md`](04-diagrama-datos.md) como guion (Parte 8.3). Es literalmente el flujo de tu app:

```text
datos JSON → lista de objetos → ArbolBST (títulos) / Heap (ratings) / Grafo (relaciones)
           → BFS/DFS/Dijkstra → Recomendador → terminal
```

Tené preparada esta tabla mental (y explicala señalando el diagrama):

| Estructura | Dónde está | Consulta que resuelve | Complejidad |
|---|---|---|---|
| ArbolBST/AVL | `estructuras/` | Buscar por título sin barrido | O(log n) (AVL) |
| Heap | `estructuras/heap.py` | Top-N sin ordenar todo | O(n log k) |
| Grafo | `estructuras/grafo.py` | Conexiones y caminos | según algoritmo |
| BFS | `algoritmos/bfs.py` | "el relacionado más cercano" (camino más corto en aristas) | O(V + E) |
| DFS | `algoritmos/dfs.py` | "recorré todos los relacionados en profundidad" | O(V + E) |
| Dijkstra | `algoritmos/caminos.py` | Camino de menor costo | O(E log V) |

**Frases modelo para "¿por qué esta estructura?"** (las que la consigna da en la Parte 11.2):

> "Elegimos un heap porque mantenemos rápidamente los elementos con mayor prioridad y nuestro sistema consulta frecuentemente los mejores N resultados."

> "Usamos BFS porque necesitamos la relación más cercana entre dos elementos y todas las conexiones tienen el mismo costo."

> "Usamos un árbol balanceado porque hacemos búsquedas frecuentes y queremos evitar que degrade a comportamiento lineal."

Nunca digas "porque lo vimos esta semana". Toda estructura de tu repo tiene que poder responder a **¿qué problema real resuelve acá?**: es la pregunta más importante de la cursada (Parte 11.2).

## 4. Reparto de roles y práctica

- Los tres deben **rotar** en la parte técnica: cada uno trae una estructura/algoritmo "suya" para asegurar cobertura, pero al terminar cualquiera responde cualquiera de las otras.
- **Mínimo 2 prácticas completas con cronómetro** antes del día. En la segunda, que un compañero haga de jurado duro con las preguntas de la sección 5.
- El que maneja el teclado no es el único que habla. Si el tecladista va a lo suyo y el que explica a lo suyo, se nota y se pierde naturalidad: uno explica y el otro acota (pero nunca los dos hablando a la vez).

## 5. Banco de preguntas con respuestas modelo

Parte X de la consigna. Acá van las que seguro aparecen, con el esqueleto de respuesta.

### Estructuras

**¿Por qué eligieron esta estructura? ¿Qué alternativa había? ¿Ventajas/desventajas?**

> "Buscamos varias veces por título sobre datos que no cambian mucho en cada consulta, por eso árbol balanceado: O(log n) por búsqueda. La alternativa era diccionario O(1) promedio, pero perdíamos el orden y el TP pedía árbol; y recorrer la lista O(n) ya lo descartamos midiéndolo en TP2."

### Complejidad

**¿Cuánto cuesta buscar? ¿Qué pasa si multiplico los datos x10? ¿Cuál es el peor caso?**

> "Buscar en el AVL es O(log n); a 100k elementos son ~17 pasos. El peor caso de un BST común es O(n) si insertás ordenado, y por eso usamos AVL: la tabla del TP4 lo muestra."

### Árboles

**¿Qué pasa si el árbol se desbalancea? ¿Qué aporta AVL?**

> "Degrada de O(log n) a O(n) (una lista). AVL rota para mantener |altura(izq) − altura(der)| ≤ 1, garantizando O(log n)."

### Heap

**¿Por qué un heap para el ranking? ¿Qué diferencia con ordenar todo?**

> "Ordenar todo paga O(n log n) en cada consulta. El heap arma el Top-N en O(n log N) (N chico), y sujeto a la regla de la cátedra, el heap está implementado por nosotros."

### Grafo

**¿Qué es un vértice y una arista acá? ¿Por qué no dirigido? ¿Por qué no pesado?**

> "Vértice = elemento. Arista = comparten [género y director] (definida en TP7). Es no dirigido porque la relación es simétrica; no pesado en BFS porque ahí todas las conexiones valen 1, y pesado cuando definimos 'costo' en TP9."

### Recorridos

**¿Cuándo BFS y cuándo DFS?**

> "BFS cuando la pregunta es 'el más cercano' (camino mínimo en aristas). DFS cuando es 'mostrame todo lo conectado, a profundidad'."

### Caminos

**¿Qué significa 'camino mínimo' en su problema? ¿Qué es el costo? ¿Por qué ese algoritmo?**

> "El costo es [diferencia de rating / distancia / similitud inversa]. Dijkstra porque el grafo tiene pesos no negativos y queremos la ruta de menor costo; si tuviera negativos usaríamos Bellman-Ford."

### Defensa al código

**"Muéstrenme dónde insertan en el AVL" / "¿qué hace esta línea?"**

> Respuesta sincera si no sabés: "Esa parte la implementó [compañero]; te muestro la rotación y vuelvo en 20 segundos". Rotar a quien la hizo es válido si después cualquiera la explica.

## 6. El desafío sorpresa: cómo entrenar

La consigna nombra tres ejemplos. Prepará cada uno en el ensayo:

1. **"Agreguen 100.000 elementos y vuelvan a buscar."** → Tené el script generador (`datos/generar.py` del TP2) y la carga parametrizable. En el ensayo, hacelo 2 veces para que salga en menos de 1 minuto.
2. **"Encuentren el camino entre A y B."** → Conocé de memoria 3 pares de tu dataset que tengan camino (y uno que no, por si preguntan el "no existe").
3. **"¿Y si el dataset fuera 100 veces más grande?"** → Respondé desde tus mediciones: "la búsqueda O(log n) solo agrega 7 pasos; lo que hay que mirar es la memoria y la carga, no la búsqueda". Si mediste en TP2/TP4/TP6, tenés datos para decirlo.

**Entrenamiento express:** los 10 experimentos de tus TPs (script de medición + generador de datos conocido de memoria + saber los 3 caminos). Eso cubre el 90% de los desafíos.

## 7. Checklist del día de la defensa

### Días antes

- [ ] Repo actualizado, `main` funcional, sin pendientes de merge
- [ ] El repo clonado de cero en una máquina del aula corre siguiendo el README
- [ ] Diagramas 03 y 04 actualizados (se explican con ellos)
- [ ] 2 prácticas con cronómetro y jurado duro hechas
- [ ] Script generador + medición preparados por si cae el desafío sorpresa

### El día (30 min antes)

- [ ] `git pull` y `python main.py` corren limpios
- [ ] `__pycache__` borrado / `git status` limpio (no muestres basura en el repo)
- [ ] Dataset real cargado (no 8 elementos inventados)
- [ ] Anotados los 3 caminos de la demo y los elementos de ejemplo
- [ ] En una hoja: tabla estructura → consulta → complejidad (para el bolsillo, no para leer)
- [ ] Agua, respiración, y todos saben qué parte habla cada uno

## 8. Errores comunes en defensas

1. **Leer del código o de la tarjeta:** la defensa es de conversación, no de lectura. La tarjeta es solo de apoyo.
2. **Empezar por la tecnología** ("usamos Python y...") en vez de por el problema. El jurado quiere el problema primero.
3. **Nadie puede explicar el módulo del compañero:** se practica justamente rotando.
4. **"El dibujo es viejito":** si el 04 no refleja lo que se codeó, se nota en la primera pregunta técnica. Actualizalo por TP, no la semana de la defensa.
5. **Complejidades sin respaldo:** decir O(log n) de un árbol sin haberlo medido nunca. Si preguntan "¿y cómo lo saben?", la respuesta correcta es "lo medimos en TP2/TP4".
6. **Demo sin volumen:** diez elementos no demuestran nada. Si tu sistema "aguanta 100k", mostralo.
7. **No saber qué es cada cosa en SU dominio:** van a preguntar "¿qué es un vértice en tu problema?" y el sílabo no alcanza. Adaptá los conceptos a tu caso real.
8. **Improvisar la organización:** el que explica, el que teclea y el que cierra, definidos y ensayados. El mejor sistema del curso con una defensa floja pierde puntos que no tenía por qué perder.

> 💡 **Cierre útil:** cuando termines la parte técnica, hacé un cierre de una frase que relacione el problema con la tecnología (lo que pide la Parte 11.3): *"Lo que vieron en la demo no son ejercicios sueltos: cada estructura resuelve una consulta real del sistema, y el diagrama 04 es exactamente ese recorrido."*
