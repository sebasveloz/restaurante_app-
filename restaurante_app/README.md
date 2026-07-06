# Restaurante App

## Autor

Sebastián Veloz

## Asignatura

Programación Orientada a Objetos

## Descripción

Este proyecto corresponde a la Tarea de la Semana 6 de la asignatura Programación Orientada a Objetos.

El sistema representa los productos de un restaurante utilizando los principios fundamentales de la Programación Orientada a Objetos (POO): herencia, encapsulación y polimorfismo. El proyecto está organizado de forma modular para facilitar su mantenimiento y reutilización.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

## Clases implementadas

### Producto

Es la clase padre del proyecto. Contiene los atributos comunes:

- Nombre
- Precio
- Disponibilidad

Además, el atributo `precio` está encapsulado para proteger su acceso.

### Platillo

Hereda de la clase Producto y agrega el atributo:

- Categoría

Sobrescribe el método `mostrar_informacion()` para mostrar información específica del platillo.

### Bebida

Hereda de la clase Producto y agrega el atributo:

- Tamaño

También sobrescribe el método `mostrar_informacion()`.

### Restaurante

Administra una lista de productos y permite agregarlos y mostrarlos en pantalla.

## Herencia

Se implementó una relación de herencia donde la clase `Producto` es la clase padre y las clases `Platillo` y `Bebida` reutilizan sus atributos y métodos mediante `super()`.

## Encapsulación

El atributo `__precio` se encuentra encapsulado.

Para acceder y modificar su valor se utilizan los métodos:

- `obtener_precio()`
- `cambiar_precio()`

El método `cambiar_precio()` valida que el nuevo precio sea mayor que cero antes de actualizarlo.

## Polimorfismo

Las clases `Platillo` y `Bebida` sobrescriben el método `mostrar_informacion()`.

Al recorrer la lista de productos del restaurante, el mismo método produce resultados diferentes dependiendo del tipo de objeto.

## Ejecución

Para ejecutar el proyecto:

```bash
python main.py
```

## Reflexión

La Programación Orientada a Objetos permite desarrollar aplicaciones más organizadas, reutilizables y fáciles de mantener. Gracias al uso de herencia, encapsulación y polimorfismo se reduce la duplicación de código y se mejora la estructura del programa.
