from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante("Restaurante Sabor Ecuatoriano")


# Crear platillos
platillo1 = Platillo(
    "Encebollado",
    6.50,
    True,
    "Plato fuerte"
)

platillo2 = Platillo(
    "Ceviche de Camarón",
    8.25,
    True,
    "Mariscos"
)


# Crear bebidas
bebida1 = Bebida(
    "Limonada",
    2.00,
    True,
    "Grande"
)

bebida2 = Bebida(
    "Jugo de Mora",
    2.50,
    True,
    "Mediano"
)


# Agregar productos
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)


# Mostrar productos (Polimorfismo)
restaurante.mostrar_productos()


print("\n===== PRUEBA DE ENCAPSULACIÓN =====\n")

print("Precio actual:", platillo1.obtener_precio())

platillo1.cambiar_precio(7.00)

print("Nuevo precio:", platillo1.obtener_precio())

# Intentar colocar un precio incorrecto
platillo1.cambiar_precio(-3)