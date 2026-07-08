class Producto:
    def __init__(self, nombre, categoria, precio, disponible):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío.")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if valor.strip():
            self._categoria = valor
        else:
            raise ValueError("La categoría no puede estar vacía.")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self._precio = valor
        else:
            raise ValueError("El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Estado: {estado}"
        )