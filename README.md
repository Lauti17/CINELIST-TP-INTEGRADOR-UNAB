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
git clone #(url del git)
cd cinelilist
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

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `modelos/` | Clases del dominio (`Pelicula`) |
| `estructuras/` | Estr. de datos implementadas (BST, AVL, Heap, Grafo) |
| `algoritmos/` | Búsquedas, BFS/DFS, caminos mínimos |
| `datos/` | Datasets de prueba (JSON) |
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

## Estado del proyecto

#tp 0, tp1, tp2, tp3, tp4, tp5, tp6 