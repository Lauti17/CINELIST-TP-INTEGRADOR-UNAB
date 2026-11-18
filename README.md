# 🎬 CineliList

Sistema de recomendación de películas: buscá, explorá categorías y descubrí lo qué podes ver basándote en lo que ya te gustó.

## Integrantes

- luciano Bazan
- Lautaro Arola

## Requisitos

- Python 3.10 o superior (el proyecto usa anotaciones de tipo modernas como `Pelicula | None`).

Verificá tu versión:

```bash
python --version    # Windows
python3 --version   # macOS / Linux
```

## Instalación

```bash
git clone https://github.com/Lauti17/CINELIST-TP-INTEGRADOR-UNAB.git
cd CINELIST-TP-INTEGRADOR-UNAB
```

### Entorno virtual (recomendado)

Crea una copia aislada de Python solo para este proyecto, sin tocar lo que tengas instalado en tu máquina.

```bash
python -m venv .venv       # Windows
python3 -m venv .venv      # macOS / Linux
```

Activarlo:

| Sistema | Comando |
|---|---|
| Windows (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

Vas a ver `(.venv)` al inicio de la línea de la terminal cuando esté activo. Para salir: `deactivate`.

> ⚠️ Si en Windows PowerShell aparece "la ejecución de scripts está deshabilitada", corré:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` y confirmá con `S`.

El proyecto usa solo librería estándar de Python (`json`, `unittest`), así que no hace falta `pip install` nada para correrlo.

## Ejecución

Desde la raíz del repo (la carpeta donde está `main.py`):

```bash
python main.py     # Windows
python3 main.py    # macOS / Linux
```

## Pruebas

```bash
python -m unittest discover tests     # Windows
python3 -m unittest discover tests    # macOS / Linux
```

## Experimentos

```bash
python algoritmos/experimentos/medicion.py   # TP2: secuencial vs binaria vs BST
python experimento_avl.py                    # TP4: BST desbalanceado vs AVL
python algoritmos/experimentos/medicion_recorridos.py   # TP8: BFS vs DFS
python experimentos.py                       # comparación rápida secuencial vs árbol
```

El gráfico del TP2 requiere `matplotlib` (`pip install matplotlib`); sin él, el
script imprime igual la tabla. Los datasets sintéticos se generan solos con
`datos/generar.py`.

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `modelos/` | Clases del dominio (`Pelicula`) |
| `estructuras/` | Estructuras de datos: BST, AVL, árbol N-ario, heap y grafo |
| `algoritmos/` | BFS y DFS, y experimentos de medición (`experimentos/`); caminos mínimos (pendiente) |
| `datos/` | Dataset real (`peliculas.json`) y generador de datasets sintéticos (`generar.py`) |
| `servicios/` | Lógica de negocio (`Catalogo`, recomendador) |
| `ui/` | Interfaz de terminal |
| `tests/` | Pruebas |
| `docs/` | Documentación del proyecto |

## Documentación

- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos-de-uso.md)
- [Diagrama de clases](docs/03-diagrama-clases.md)
- [Conexión entre estructuras](docs/04-diagrama-datos.md)
- [Gestión del proyecto](docs/05-gestion-proyecto.md)
- [Informe TP2: análisis de complejidad](docs/tp2-experimentos.md)
- [TP7: grafo de relaciones](docs/tp7-grafo.md)
- [TP8: recorridos BFS y DFS](docs/tp8-recorridos.md)
- [Guía del Demo Day](docs/06-guia-demo-day.md)

## Estado del proyecto

| TP | Tema | Estado |
|---|---|---|
| TP0 | Lanzamiento | ✅ |
| TP1 | Objetos y clases | ✅ |
| TP2 | Análisis de algoritmos | ✅ |
| TP3 | Árbol binario de búsqueda | ✅ |
| TP4 | AVL | ✅ |
| TP5 | Árbol general (categorías) | ✅ |
| TP6 | Heap (Top N) | ✅ |
| TP7 | Grafo | ✅ |
| TP8 | BFS / DFS | ✅ |
| TP9 | Caminos mínimos | ⏳ |
| TP10 | Producto final | ⏳ |
