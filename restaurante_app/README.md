# Restaurante App

## Nombre del estudiante

Sebastián Veloz

## Descripción

Restaurante App es un sistema desarrollado en Python utilizando Programación Orientada a Objetos. El programa permite registrar, listar y buscar productos y clientes mediante un menú interactivo ejecutado desde la consola.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

## Constructor en la clase Producto

La clase Producto utiliza el constructor `__init__()` para crear objetos a partir de los datos ingresados por el usuario, inicializando el nombre, la categoría, el precio y la disponibilidad.

## Uso de @property y @setter

Se utilizan los decoradores `@property` y `@setter` para controlar el acceso y la modificación de los atributos del producto. Además, se validan datos como el nombre, la categoría y el precio para evitar información incorrecta.

## Uso de @dataclass

La clase Cliente está implementada mediante `@dataclass`, lo que simplifica la definición de sus atributos y facilita la creación de objetos.

## Menú interactivo

El sistema cuenta con un menú que permite:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del programa.

## Reflexión

Crear objetos a partir de datos ingresados por el usuario permite desarrollar aplicaciones más dinámicas y cercanas a situaciones reales. El uso de constructores, propiedades, setters y clases de datos mejora la organización del código y facilita su mantenimiento.