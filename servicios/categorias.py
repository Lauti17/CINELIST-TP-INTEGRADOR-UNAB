from estructuras.arbol_nario import NodoNArio
from modelos.pelicula import Pelicula


class GestorCategorias:
    """Maneja la estructura jerárquica de categorías en CineliList."""

    def __init__(self):
        self.raiz = NodoNArio("Catálogo de Cine")
        self._construir_jerarquia_base()

    def _construir_jerarquia_base(self):
        # 1. Ramas principales por Género
        scifi = NodoNArio("Ciencia Ficción")
        drama = NodoNArio("Drama & Suspenso")
        terror = NodoNArio("Terror & Thriller")
        animacion = NodoNArio("Animación & Cine Familiar")
        accion = NodoNArio("Acción & Aventura")
        comedia_romance = NodoNArio("Comedia & Romance")

        # 2. Subcategorías temáticas
        scifi.agregar_hijo(NodoNArio("Cyberpunk & Inteligencia Artificial"))  # Matrix, Blade Runner 2049
        scifi.agregar_hijo(NodoNArio("Viajes Temporales & Sueños"))           # Inception
        scifi.agregar_hijo(NodoNArio("Exploración Espacial & Epic"))          # Interstellar, Dune

        drama.agregar_hijo(NodoNArio("Crimen Organizado & Mafia"))            # El Padrino, Pulp Fiction
        drama.agregar_hijo(NodoNArio("Drama Psicológico & Intenso"))          # Whiplash, Parasite

        terror.agregar_hijo(NodoNArio("Clásicos del Terror Psicológico"))    # El Resplandor
        terror.agregar_hijo(NodoNArio("Terror Moderno & Sobrenatural"))       # Hereditary, It, Get Out

        animacion.agregar_hijo(NodoNArio("Cine de Animación Occidental"))     # Toy Story, Coco
        animacion.agregar_hijo(NodoNArio("Anime & Animación Japonesa"))       # El Viaje de Chihiro

        accion.agregar_hijo(NodoNArio("Superhéroes & Blockbusters"))          # Los Vengadores
        accion.agregar_hijo(NodoNArio("Acción Distópica & Combate"))          # Mad Max, John Wick

        comedia_romance.agregar_hijo(NodoNArio("Romance & Musicales"))        # Titanic, La La Land
        comedia_romance.agregar_hijo(NodoNArio("Comedia de Autor & Juvenil"))  # El Gran Hotel Budapest, Superbad

        # Conectar todas las ramas principales al nodo raíz
        self.raiz.agregar_hijo(scifi)
        self.raiz.agregar_hijo(drama)
        self.raiz.agregar_hijo(terror)
        self.raiz.agregar_hijo(animacion)
        self.raiz.agregar_hijo(accion)
        self.raiz.agregar_hijo(comedia_romance)

    def obtener_arbol_visual(self) -> str:
        return self.raiz.mostrar_jerarquia()

    def asociar_pelicula(self, nombre_categoria: str, pelicula: Pelicula) -> bool:
        nodo = self.raiz.buscar(nombre_categoria)
        if nodo:
            nodo.datos.append(pelicula)
            return True
        return False