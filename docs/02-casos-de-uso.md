# Casos de uso

## Caso de uso: Buscar elemento

- **Actor**: Usuario
- **Precondición**: el catálogo está cargado.
- **Flujo principal**:
  1. El usuario selecciona "Buscar elemento".
  2. El sistema pide el título.
  3. El usuario ingresa el título.
  4. El sistema lo busca (sin distinguir mayúsculas) y lo muestra.
- **Flujo alternativo**: si no se encuentra, el sistema informa que no existe.

## Caso de uso: Listar todos los elementos

- **Actor**: Usuario
- **Precondición**: el catálogo está cargado.
- **Flujo principal**:
  1. El usuario selecciona "Listar todos los elementos".
  2. El sistema muestra todas las películas del catálogo.

## Caso de uso: Filtrar por categoría

- **Actor**: Usuario
- **Precondición**: el catálogo está cargado.
- **Flujo principal**:
  1. El usuario selecciona "Filtrar por categoría".
  2. El sistema pide el género.
  3. El usuario ingresa el género.
  4. El sistema muestra las películas de ese género.
- **Flujo alternativo**: si no hay películas en esa categoría, el sistema lo informa.
