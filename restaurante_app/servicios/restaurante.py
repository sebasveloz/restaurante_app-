class Restaurante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):

        print("=" * 45)
        print(self.nombre.upper())
        print("=" * 45)

        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("-" * 45)