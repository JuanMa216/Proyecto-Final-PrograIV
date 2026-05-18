from models.producto import Producto


class ProductoFactory:

    @staticmethod
    def crear_producto(nombre, categoria, precio, stock):
        return Producto(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock
        )