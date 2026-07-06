class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    """

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado
        self.disponible = disponible

    # Getter
    def obtener_precio(self):
        return self.__precio

    # Setter con validación
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"Precio de '{self.nombre}' actualizado correctamente.")
        else:
            print("Error: El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.__precio:.2f}\n"
            f"Estado: {estado}"
        )