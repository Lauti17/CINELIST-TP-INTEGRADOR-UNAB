from servicios.catalogo import Catalogo
from servicios.categorias import GestorCategorias
from servicios.recomendador import Recomendador


class Terminal:
    """Interfaz de línea de comandos de CineliList."""

    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo
        self._gestor_categorias = GestorCategorias()

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