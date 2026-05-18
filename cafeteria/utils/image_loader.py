from PIL import Image
import customtkinter as ctk


def cargar_imagen_producto(nombre):

    rutas = {
        "Latte": "assets/latte.png",
        "Espresso": "assets/espresso.png",
        "Capuccino": "assets/capuccino.png",
        "Americano": "assets/americano.png",
        "Chocolate": "assets/chocolate.png",
        "Muffin": "assets/muffin.png",
        "Croissant": "assets/croissant.png",
        "Frappe": "assets/frappe.png",
        "Té verde": "assets/te_verde.png"
    }

    ruta = rutas.get(
        nombre,
        "assets/logo.png"
    )

    return ctk.CTkImage(
        light_image=Image.open(ruta),
        size=(95, 95)
    )