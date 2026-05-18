# Cafetería Premium

Sistema de gestión para cafetería con interfaz gráfica de escritorio, desarrollado en Python como proyecto final de Programación IV.

## Características

- **Interfaz gráfica moderna** con tema oscuro usando CustomTkinter
- **Control de acceso por roles**: Administrador, Cajero y Barista
- **Gestión de productos** (CRUD completo desde el panel de administración)
- **Sistema de pedidos y ventas** con punto de venta (POS)
- **Panel de cocina** para que el barista gestione los pedidos en preparación
- **Base de datos SQLite** con SQLAlchemy ORM
- **Patrones de diseño**: Decorator (bebidas con extras), Factory (creación de productos)

## Requisitos

- Python 3.10+

## Instalación

```bash
cd cafeteria
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

La base de datos se inicializa automáticamente con datos de ejemplo al arrancar la aplicación.

## Estructura del proyecto

```
cafeteria/
├── main.py                  # Punto de entrada
├── app.py                   # Aplicación principal con navegación entre vistas
├── requirements.txt         # Dependencias
├── database/
│   ├── conexion.py          # Configuración de SQLAlchemy (engine, session, base)
│   ├── config.py            # URL de la base de datos
│   └── seed.py              # Datos iniciales
├── models/
│   ├── usuario.py           # Modelo de usuarios (admin, cajero, barista)
│   ├── producto.py          # Modelo de productos
│   ├── pedido.py            # Modelo de pedidos
│   ├── detalle_pedido.py    # Modelo de líneas de pedido
│   ├── venta.py             # Modelo de ventas
│   └── extra.py             # Modelo de extras/adicionales para bebidas
├── repositories/            # Capa de acceso a datos
│   ├── usuario_repository.py
│   ├── producto_repository.py
│   ├── pedido_repository.py
│   └── extra_repository.py
├── services/                # Lógica de negocio
│   ├── auth_service.py
│   ├── producto_service.py
│   ├── pedido_service.py
│   └── venta_service.py
├── patterns/
│   ├── factory/
│   │   └── producto_factory.py   # Factory pattern para crear productos
│   └── decorator/
│       ├── bebida_base.py        # Componente base del decorator
│       ├── decorator_base.py     # Decorator abstracto
│       └── extras.py             # Decorators concretos (extras para bebidas)
├── ui/
│   ├── log/
│   │   └── login_view.py         # Pantalla de login
│   ├── admin/
│   │   ├── dashboard_admin.py    # Panel de administración
│   │   ├── productos_view.py     # Gestión de productos
│   │   ├── empleados_view.py     # Gestión de empleados
│   │   └── extras_view.py        # Gestión de extras
│   ├── cajero/
│   │   └── pos_view.py           # Punto de venta
│   └── barista/
│       └── cocina_view.py        # Vista de cocina/pedidos
├── utils/
│   ├── image_loader.py
│   ├── helper.py
│   └── validators.py
└── tests/
    ├── test_productos.py
    └── test_pedidos.py
```

## Roles del sistema

| Rol | Funcionalidad |
|---|---|
| **Administrador** | Gestión de productos, empleados, extras y reportes |
| **Cajero** | Punto de venta (POS), creación de pedidos y registro de ventas |
| **Barista** | Vista de cocina para ver y gestionar pedidos en preparación |

## Tecnologías

- **CustomTkinter** - Interfaz gráfica moderna
- **SQLAlchemy 2.0** - ORM para base de datos
- **SQLite** - Base de datos embebida
- **Pillow** - Procesamiento de imágenes
- **python-dotenv** - Gestión de variables de entorno

## Patrones de diseño

### Decorator
Se utiliza para componer bebidas con extras adicionales. La clase abstracta `Bebida` define la interfaz base y los decorators concretos agregan funcionalidad (costo y descripción) de forma dinámica.

### Factory
`ProductoFactory` centraliza la creación de instancias de `Producto`, asegurando una construcción consistente.
