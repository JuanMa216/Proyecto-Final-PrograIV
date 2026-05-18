import customtkinter as ctk
from tkinter import messagebox

from services.pedido_service import (
    obtener_pedidos,
    cambiar_estado_pedido,
    eliminar_pedido
)


class CocinaView(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        usuario,
        logout_callback
    ):

        super().__init__(parent)

        self.logout_callback = logout_callback

        self.configure(
            fg_color="#0F0F0F"
        )

        self.topbar = ctk.CTkFrame(
            self,
            fg_color="#141414",
            height=80
        )

        self.topbar.pack(
            fill="x"
        )

        self.title = ctk.CTkLabel(
            self.topbar,
            text="☕ Cocina",
            font=("Montserrat", 28, "bold")
        )

        self.title.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.logout_btn = ctk.CTkButton(
            self.topbar,
            text="Cerrar Sesión",
            fg_color="red",
            hover_color="#aa0000",
            command=self.logout_callback
        )

        self.logout_btn.pack(
            side="right",
            padx=20,
            pady=20
        )

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="#0F0F0F"
        )

        self.scroll.pack(
            fill="both",
            expand=True
        )

        self.cargar_pedidos()

    def cargar_pedidos(self):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        pedidos = obtener_pedidos()

        for pedido in pedidos:

            if pedido.estado == "pendiente":
                color_estado = "#C67C3E"

            elif pedido.estado == "en_preparacion":
                color_estado = "#3498DB"

            else:
                color_estado = "#4CAF50"

            card = ctk.CTkFrame(
                self.scroll,
                fg_color="#1A1A1A",
                corner_radius=25
            )

            card.pack(
                fill="x",
                padx=20,
                pady=20
            )

            top = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            top.pack(
                fill="x",
                padx=20,
                pady=(20, 10)
            )

            titulo = ctk.CTkLabel(
                top,
                text=f"☕ Pedido #{pedido.id}",
                font=("Montserrat", 24, "bold")
            )

            titulo.pack(
                side="left"
            )

            eliminar_btn = ctk.CTkButton(
                top,
                text="X",
                width=40,
                fg_color="red",
                hover_color="#aa0000",
                command=lambda p=pedido: self.eliminar_pedido_ui(p.id)
            )

            eliminar_btn.pack(
                side="right"
            )

            badge = ctk.CTkFrame(
                card,
                fg_color=color_estado,
                corner_radius=30,
                height=35
            )

            badge.pack(
                anchor="w",
                padx=20,
                pady=10
            )

            badge_label = ctk.CTkLabel(
                badge,
                text=pedido.estado.upper(),
                font=("Montserrat", 14, "bold")
            )

            badge_label.pack(
                padx=15,
                pady=5
            )

            for detalle in pedido.detalles:

                nombre_producto = "Producto eliminado"

                if detalle.producto:
                    nombre_producto = detalle.producto.nombre

                detalle_label = ctk.CTkLabel(
                    card,
                    text=f"• {nombre_producto} x{detalle.cantidad}",
                    font=("Montserrat", 16)
                )

                detalle_label.pack(
                    anchor="w",
                    padx=35,
                    pady=2
                )

            total = ctk.CTkLabel(
                card,
                text=f"Total: ${pedido.total}",
                font=("Montserrat", 18, "bold"),
                text_color="#C67C3E"
            )

            total.pack(
                anchor="w",
                padx=20,
                pady=15
            )

            if pedido.estado == "pendiente":

                boton = ctk.CTkButton(
                    card,
                    text="Iniciar Preparación",
                    fg_color="#3498DB",
                    hover_color="#2874A6",
                    command=lambda p=pedido: self.iniciar_preparacion(p.id)
                )

                boton.pack(
                    padx=20,
                    pady=15
                )

            elif pedido.estado == "en_preparacion":

                boton = ctk.CTkButton(
                    card,
                    text="Marcar Listo",
                    fg_color="#4CAF50",
                    hover_color="#388E3C",
                    command=lambda p=pedido: self.marcar_listo(p.id)
                )

                boton.pack(
                    padx=20,
                    pady=15
                )

    def iniciar_preparacion(self, pedido_id):

        cambiar_estado_pedido(
            pedido_id,
            "En preparacion"
        )

        self.cargar_pedidos()

    def marcar_listo(self, pedido_id):

        cambiar_estado_pedido(
            pedido_id,
            "listo"
        )

        self.cargar_pedidos()

    def eliminar_pedido_ui(self, pedido_id):

        pedidos = obtener_pedidos()

        pedido_actual = None

        for pedido in pedidos:

            if pedido.id == pedido_id:
                pedido_actual = pedido
                break

        if not pedido_actual:
            return

        if pedido_actual.estado != "listo":

            messagebox.showerror(
                "Error",
                "Solo pedidos listos pueden eliminarse"
            )

            return

        confirmacion = messagebox.askyesno(
            "Confirmar",
            f"¿Eliminar pedido #{pedido_id}?"
        )

        if not confirmacion:
            return

        eliminar_pedido(pedido_id)

        self.cargar_pedidos()