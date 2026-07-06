from modelos.producto import Producto


class Platillo(Producto):

    def __init__(self, nombre, precio, disponible, categoria):
        super().__init__(nombre, precio, disponible)
        self.categoria = categoria

    # Polimorfismo
    def mostrar_informacion(self):
        return (
            "========== PLATILLO ==========\n"
            f"{super().mostrar_informacion()}\n"
            f"Categoría: {self.categoria}"
        )