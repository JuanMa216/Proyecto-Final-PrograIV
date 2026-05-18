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
            fg_color="#111111"
        )

        self.topbar = ctk.CTkFrame(
            self,
            fg_color="#1b1b1b",
            height=80
        )

        self.topbar.pack(
            fill="x"
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
            fg_color="#111111"
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

            card = ctk.CTkFrame(
                self.scroll,
                fg_color="#1b1b1b",
                corner_radius=20
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
                text=f"Pedido #{pedido.id}",
                font=("Arial", 25, "bold")
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

            estado = ctk.CTkLabel(
                card,
                text=f"Estado: {pedido.estado}",
                text_color="#C67C3E"
            )

            estado.pack(
                anchor="w",
                padx=20
            )

            for detalle in pedido.detalles:

                producto = detalle.producto.nombre

                detalle_label = ctk.CTkLabel(
                    card,
                    text=f"- {producto} x{detalle.cantidad}"
                )

                detalle_label.pack(
                    anchor="w",
                    padx=40
                )

            total = ctk.CTkLabel(
                card,
                text=f"Total: ${pedido.total}",
                font=("Arial", 18, "bold")
            )

            total.pack(
                anchor="w",
                padx=20,
                pady=10
            )

            boton = ctk.CTkButton(
                card,
                text="Marcar Listo",
                command=lambda p=pedido: self.marcar_listo(p.id)
            )

            boton.pack(
                padx=20,
                pady=20
            )

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

        eliminar_pedido(
            pedido_id
        )

        self.cargar_pedidos()