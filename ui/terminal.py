from servicios.catalogo import Catalogo
from servicios.categorias import GestorCategorias
from servicios.recomendador import Recomendador
from servicios.relaciones import Relaciones


class Terminal:
    """Interfaz de línea de comandos de CineliList."""

    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo
        self._gestor_categorias = GestorCategorias()
        self._relaciones: Relaciones | None = None  # el grafo se arma la primera vez que se usa

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = input("Opción: ").strip()

            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._listar()
            elif opcion == "3":
                self._filtrar()
            elif opcion == "4":
                self._explorar_categorias()
            elif opcion == "5":
                self._mostrar_top_n()
            elif opcion == "6":
                self._mostrar_relacionadas()
            elif opcion == "7":
                self._mostrar_camino_mas_corto()
            elif opcion == "8":
                self._mostrar_mas_cercana_de_otro_genero()
            elif opcion == "9":
                self._explorar_en_profundidad()
            elif opcion == "0":
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción inválida.")
            print()

    def _mostrar_menu(self) -> None:
        print("=" * 40)
        print(" 🎬 CINELILIST — TERMINAL")
        print("=" * 40)
        print("1. Buscar película")
        print("2. Listar todas las películas")
        print("3. Filtrar por categoría")
        print("4. Explorar categorías")
        print("5. Ver Top N películas")
        print("6. Ver películas relacionadas")
        print("7. Camino más corto entre dos películas")
        print("8. Película más cercana de otro género")
        print("9. Explorar todo lo conectado a una película")
        print("0. Salir")
        print("-" * 40)

    def _buscar(self) -> None:
        titulo = input("Título a buscar: ").strip()
        resultado = self._catalogo.buscar(titulo)
        if resultado:
            print(f"Encontrada: {resultado}")
        else:
            print(f"No encontramos '{titulo}'.")

    def _listar(self) -> None:
        for pelicula in self._catalogo.listar():
            print(f"- {pelicula}")

    def _filtrar(self) -> None:
        genero = input("Categoría: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            for pelicula in resultados:
                print(f"- {pelicula}")
        else:
            print(f"No hay elementos en '{genero}'.")

    def _explorar_categorias(self) -> None:
        print("\n--- JERARQUÍA DE CATEGORÍAS ---")
        print(self._gestor_categorias.obtener_arbol_visual())

    def _mostrar_top_n(self) -> None:
        try:
            val = input("¿Cuántas películas querés ver en el Top?: ").strip()
            n = int(val) if val else 5
        except ValueError:
            n = 5

        recomendador = Recomendador(self._catalogo.listar())
        top_peliculas = recomendador.obtener_top_n(n)

        print(f"\n--- TOP {n} PELÍCULAS MEJOR VALORADAS ---")
        for idx, p in enumerate(top_peliculas, 1):
            print(f"{idx}. {p.titulo:<25} | Rating: {p.rating}")

    def _mostrar_relacionadas(self) -> None:
        titulo = input("Título de la película: ").strip()
        pelicula = self._catalogo.buscar(titulo)
        if pelicula is None:
            print(f"No encontramos '{titulo}'.")
            return

        relacionadas = self._obtener_relaciones().relacionadas(pelicula.titulo)
        if not relacionadas:
            print(f"'{pelicula.titulo}' no tiene películas relacionadas.")
            return

        print(f"\n--- Si te gustó {pelicula.titulo} ({pelicula.director}), mirá también ---")
        for p, motivo in relacionadas:
            print(f"- {p.titulo:<35} ⭐{p.rating}  ({motivo})")

    def _obtener_relaciones(self) -> Relaciones:
        """Arma el grafo la primera vez que hace falta y lo reutiliza."""
        if self._relaciones is None:
            self._relaciones = Relaciones(self._catalogo.listar())
        return self._relaciones

    def _pedir_pelicula(self, mensaje: str):
        titulo = input(mensaje).strip()
        pelicula = self._catalogo.buscar(titulo)
        if pelicula is None:
            print(f"No encontramos '{titulo}'.")
        return pelicula

    def _imprimir_camino(self, camino) -> None:
        motivos = Relaciones.motivos_del_camino(camino)
        print(f"  {camino[0].titulo}")
        for pelicula, motivo in zip(camino[1:], motivos):
            print(f"   → {pelicula.titulo}  ({motivo})")

    def _mostrar_camino_mas_corto(self) -> None:
        origen = self._pedir_pelicula("Película de origen: ")
        if origen is None:
            return
        destino = self._pedir_pelicula("Película de destino: ")
        if destino is None:
            return
        if origen is destino:
            print("Elegiste la misma película dos veces.")
            return

        camino = self._obtener_relaciones().camino_mas_corto(origen.titulo, destino.titulo)
        if camino is None:
            print(f"\nNo existe camino entre '{origen.titulo}' y '{destino.titulo}': "
                  "ninguna cadena de películas relacionadas las une.")
            return
        print(f"\n--- Camino más corto: {len(camino) - 1} conexiones ---")
        self._imprimir_camino(camino)

    def _mostrar_mas_cercana_de_otro_genero(self) -> None:
        origen = self._pedir_pelicula("Título de la película: ")
        if origen is None:
            return
        camino = self._obtener_relaciones().mas_cercana_de_otro_genero(origen.titulo)
        if camino is None:
            print(f"\nNinguna película de otro género está conectada con '{origen.titulo}'.")
            return
        destino = camino[-1]
        print(f"\n--- La más cercana de otro género a {origen.titulo} ({origen.genero}) ---")
        self._imprimir_camino(camino)
        print(f"\nRecomendada: {destino.titulo} ({destino.genero}) ⭐{destino.rating}, "
              f"a {len(camino) - 1} conexiones.")

    def _explorar_en_profundidad(self) -> None:
        origen = self._pedir_pelicula("Película de partida: ")
        if origen is None:
            return
        recorrido = self._obtener_relaciones().explorar_en_profundidad(origen.titulo)[1:]
        print(f"\n--- Todo lo conectado con {origen.titulo}, explorado en profundidad ---")
        for numero, pelicula in enumerate(recorrido, start=1):
            print(f"{numero:>3}. {pelicula.titulo:<35} {pelicula.genero}")
        print(f"\nAlcanzables: {len(recorrido)} de {len(self._catalogo) - 1} películas.")
