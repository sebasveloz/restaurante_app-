from modelos.producto import Producto


class Bebida(Producto):

    def __init__(self, nombre, precio, disponible, tamano):
        super().__init__(nombre, precio, disponible)
        self.tamano = tamano

    # Polimorfismo
    def mostrar_informacion(self):
        return (
            "=========== BEBIDA ===========\n"
            f"{super().mostrar_informacion()}\n"
            f"Tamaño: {self.tamano}"
        )