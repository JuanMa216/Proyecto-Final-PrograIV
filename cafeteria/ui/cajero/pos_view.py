import customtkinter as ctk
from tkinter import messagebox

from services.producto_service import obtener_productos
from services.pedido_service import crear_pedido

from utils.image_loader import (
    cargar_imagen_producto
)


class POSView(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        usuario,
        logout_callback
    ):

        super().__init__(parent)

        self.usuario = usuario
        self.logout_callback = logout_callback

        self.carrito = {}

        self.configure(
            fg_color="#0F0F0F"
        )

        self.sidebar = ctk.CTkFrame(
            self,
            width=340,
            fg_color="#141414"
        )

        self.sidebar.pack(
            side="right",
            fill="y"
        )

        self.content = ctk.CTkScrollableFrame(
            self,
            fg_color="#0F0F0F"
        )

        self.content.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.logout_btn = ctk.CTkButton(
            self.sidebar,
            text="Cerrar Sesión",
            fg_color="red",
            hover_color="#aa0000",
            height=50,
            corner_radius=15,
            command=self.logout_callback
        )

        self.logout_btn.pack(
            side="bottom",
            padx=20,
            pady=20,
            fill="x"
        )

        self.title = ctk.CTkLabel(
            self.sidebar,
            text="🧾 Pedido",
            font=("Montserrat", 30, "bold")
        )

        self.title.pack(pady=30)

        self.lista = ctk.CTkTextbox(
            self.sidebar,
            width=280,
            height=450,
            font=("Montserrat", 16)
        )

        self.lista.pack(padx=20)

        self.total_label = ctk.CTkLabel(
            self.sidebar,
            text="Total: $0",
            font=("Montserrat", 28, "bold"),
            text_color="#C67C3E"
        )

        self.total_label.pack(pady=20)

        self.confirmar_btn = ctk.CTkButton(
            self.sidebar,
            text="Confirmar Pedido",
            command=self.confirmar_pedido,
            height=55,
            fg_color="#C67C3E",
            hover_color="#A8642D",
            corner_radius=15,
            font=("Montserrat", 18, "bold")
        )

        self.confirmar_btn.pack(
            padx=20,
            pady=20,
            fill="x"
        )

        self.cargar_productos()

    def cargar_productos(self):

        productos = obtener_productos()

        row = 0
        column = 0

        for producto in productos:

            card = ctk.CTkFrame(
                self.content,
                width=320,
                height=280,
                fg_color="#1A1A1A",
                corner_radius=25
            )

            card.grid(
                row=row,
                column=column,
                padx=25,
                pady=25
            )

            card.grid_propagate(False)

            imagen = cargar_imagen_producto(
                producto.nombre
            )

            img_label = ctk.CTkLabel(
                card,
                text="",
                image=imagen
            )

            img_label.pack(
                pady=(25, 10)
            )

            nombre = ctk.CTkLabel(
                card,
                text=producto.nombre,
                font=("Montserrat", 26, "bold")
            )

            nombre.pack()

            categoria = ctk.CTkLabel(
                card,
                text=producto.categoria,
                text_color="gray",
                font=("Montserrat", 15)
            )

            categoria.pack(
                pady=5
            )

            precio = ctk.CTkLabel(
                card,
                text=f"${producto.precio}",
                text_color="#C67C3E",
                font=("Montserrat", 24, "bold")
            )

            precio.pack(
                pady=10
            )

            boton = ctk.CTkButton(
                card,
                text="Agregar",
                height=45,
                fg_color="#C67C3E",
                hover_color="#A8642D",
                corner_radius=15,
                font=("Montserrat", 16, "bold"),
                command=lambda p=producto: self.agregar_producto(p)
            )

            boton.pack(
                padx=30,
                fill="x"
            )

            column += 1

            if column > 2:
                column = 0
                row += 1

    def agregar_producto(self, producto):

        if producto.id in self.carrito:

            self.carrito[producto.id]["cantidad"] += 1

        else:

            self.carrito[producto.id] = {
                "producto": producto,
                "cantidad": 1
            }

        self.actualizar_pedido()

    def actualizar_pedido(self):

        self.lista.delete("1.0", "end")

        total = 0

        for item in self.carrito.values():

            producto = item["producto"]
            cantidad = item["cantidad"]

            subtotal = producto.precio * cantidad

            self.lista.insert(
                "end",
                f"{producto.nombre} x{cantidad} - ${subtotal}\n\n"
            )

            total += subtotal

        self.total_label.configure(
            text=f"Total: ${total}"
        )

    def confirmar_pedido(self):

        if not self.carrito:
            return

        productos = []

        for item in self.carrito.values():

            producto = item["producto"]
            cantidad = item["cantidad"]

            productos.append({
                "producto_id": producto.id,
                "cantidad": cantidad
            })

        pedido = crear_pedido(productos)

        messagebox.showinfo(
            "Pedido",
            f"Pedido #{pedido.id} creado"
        )

        self.carrito.clear()

        self.actualizar_pedido()