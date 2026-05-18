import customtkinter as ctk
from tkinter import messagebox

from services.producto_service import (
    obtener_productos,
    crear_producto,
    eliminar_producto
)


class ProductosView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(
            fg_color="#111111"
        )

        self.title = ctk.CTkLabel(
            self,
            text="Productos",
            font=("Arial", 30, "bold")
        )

        self.title.pack(pady=20)

        self.form_frame = ctk.CTkFrame(
            self,
            fg_color="#1b1b1b",
            corner_radius=20
        )

        self.form_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.nombre_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Nombre",
            width=220,
            height=40
        )

        self.nombre_entry.grid(
            row=0,
            column=0,
            padx=10,
            pady=20
        )

        self.categoria_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Categoría",
            width=220,
            height=40
        )

        self.categoria_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        self.precio_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Precio",
            width=180,
            height=40
        )

        self.precio_entry.grid(
            row=0,
            column=2,
            padx=10
        )

        self.crear_btn = ctk.CTkButton(
            self.form_frame,
            text="Agregar Producto",
            height=40,
            fg_color="#C67C3E",
            hover_color="#A8642D",
            command=self.crear_producto_ui
        )

        self.crear_btn.grid(
            row=0,
            column=3,
            padx=10
        )

        self.grid_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="#111111"
        )

        self.grid_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.cargar_productos()

    def cargar_productos(self):

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        productos = obtener_productos()

        row = 0
        column = 0

        for producto in productos:

            card = ctk.CTkFrame(
                self.grid_frame,
                width=250,
                height=220,
                fg_color="#1b1b1b",
                corner_radius=20
            )

            card.grid(
                row=row,
                column=column,
                padx=20,
                pady=20
            )

            card.grid_propagate(False)

            nombre = ctk.CTkLabel(
                card,
                text=producto.nombre,
                font=("Arial", 24, "bold")
            )

            nombre.pack(
                pady=(30, 10)
            )

            categoria = ctk.CTkLabel(
                card,
                text=producto.categoria,
                text_color="gray",
                font=("Arial", 16)
            )

            categoria.pack()

            precio = ctk.CTkLabel(
                card,
                text=f"${producto.precio}",
                text_color="#C67C3E",
                font=("Arial", 24, "bold")
            )

            precio.pack(
                pady=15
            )

            eliminar_btn = ctk.CTkButton(
                card,
                text="Eliminar",
                fg_color="red",
                hover_color="#aa0000",
                command=lambda p=producto: self.eliminar_producto_ui(p.id)
            )

            eliminar_btn.pack(
                padx=20,
                pady=10,
                fill="x"
            )

            column += 1

            if column > 2:
                column = 0
                row += 1

    def crear_producto_ui(self):

        try:

            nombre = self.nombre_entry.get()
            categoria = self.categoria_entry.get()

            precio = float(
                self.precio_entry.get()
            )

            if (
                not nombre or
                not categoria
            ):

                messagebox.showerror(
                    "Error",
                    "Todos los campos son obligatorios"
                )

                return

            crear_producto(
                nombre,
                categoria,
                precio,
                0
            )

            messagebox.showinfo(
                "Producto",
                "Producto agregado correctamente"
            )

            self.nombre_entry.delete(0, "end")
            self.categoria_entry.delete(0, "end")
            self.precio_entry.delete(0, "end")

            self.cargar_productos()

        except ValueError:

            messagebox.showerror(
                "Error",
                "El precio debe ser numérico"
            )

    def eliminar_producto_ui(self, producto_id):

        confirmacion = messagebox.askyesno(
            "Confirmar",
            "¿Eliminar producto?"
        )

        if not confirmacion:
            return

        eliminar_producto(producto_id)

        self.cargar_productos()