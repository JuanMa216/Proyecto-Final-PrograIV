import customtkinter as ctk
from tkinter import messagebox

from services.producto_service import (
    obtener_extras,
    crear_extra,
    actualizar_extra,
    eliminar_extra
)


class ExtrasView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(
            fg_color="#111111"
        )

        self.title = ctk.CTkLabel(
            self,
            text="Extras / Toppings",
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
            placeholder_text="Nombre del extra",
            width=250,
            height=40
        )

        self.nombre_entry.grid(
            row=0,
            column=0,
            padx=10,
            pady=20
        )

        self.precio_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Precio",
            width=180,
            height=40
        )

        self.precio_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        self.crear_btn = ctk.CTkButton(
            self.form_frame,
            text="Agregar Extra",
            height=40,
            fg_color="#C67C3E",
            hover_color="#A8642D",
            command=self.crear_extra_ui
        )

        self.crear_btn.grid(
            row=0,
            column=2,
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

        self.cargar_extras()

    def cargar_extras(self):

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        extras = obtener_extras()

        row = 0
        column = 0

        for extra in extras:

            card = ctk.CTkFrame(
                self.grid_frame,
                width=250,
                height=200,
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
                text=extra.nombre,
                font=("Arial", 22, "bold")
            )

            nombre.pack(
                pady=(30, 15)
            )

            precio = ctk.CTkLabel(
                card,
                text=f"${extra.precio}",
                text_color="#C67C3E",
                font=("Arial", 24, "bold")
            )

            precio.pack(
                pady=10
            )

            btn_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            btn_frame.pack(
                padx=15,
                pady=10,
                fill="x"
            )

            editar_btn = ctk.CTkButton(
                btn_frame,
                text="Editar",
                fg_color="#2b6cb0",
                hover_color="#1a4f8a",
                command=lambda e=extra: self.editar_extra_ui(e)
            )

            editar_btn.pack(
                side="left",
                fill="x",
                expand=True,
                padx=(0, 5)
            )

            eliminar_btn = ctk.CTkButton(
                btn_frame,
                text="Eliminar",
                fg_color="red",
                hover_color="#aa0000",
                command=lambda e=extra: self.eliminar_extra_ui(e.id)
            )

            eliminar_btn.pack(
                side="right",
                fill="x",
                expand=True,
                padx=(5, 0)
            )

            column += 1

            if column > 2:
                column = 0
                row += 1

    def crear_extra_ui(self):

        try:

            nombre = self.nombre_entry.get().strip()
            precio_texto = self.precio_entry.get().strip()

            if not nombre or not precio_texto:

                messagebox.showerror(
                    "Error",
                    "Todos los campos son obligatorios"
                )

                return

            precio = float(precio_texto)

            if precio <= 0:

                messagebox.showerror(
                    "Error",
                    "El precio debe ser mayor a 0"
                )

                return

            crear_extra(nombre, precio)

            messagebox.showinfo(
                "Extra",
                "Extra agregado correctamente"
            )

            self.nombre_entry.delete(0, "end")
            self.precio_entry.delete(0, "end")

            self.cargar_extras()

        except ValueError:

            messagebox.showerror(
                "Error",
                "El precio debe ser numérico"
            )

    def editar_extra_ui(self, extra):

        dialog = ctk.CTkToplevel(self)
        dialog.title("Editar Extra")
        dialog.geometry("350x250")
        dialog.configure(fg_color="#111111")
        dialog.resizable(False, False)

        dialog.transient(self)
        dialog.grab_set()

        nombre_label = ctk.CTkLabel(
            dialog,
            text="Nombre",
            font=("Arial", 16)
        )

        nombre_label.pack(
            pady=(20, 5)
        )

        nombre_entry = ctk.CTkEntry(
            dialog,
            width=250,
            height=35
        )

        nombre_entry.insert(0, extra.nombre)
        nombre_entry.pack()

        precio_label = ctk.CTkLabel(
            dialog,
            text="Precio",
            font=("Arial", 16)
        )

        precio_label.pack(
            pady=(15, 5)
        )

        precio_entry = ctk.CTkEntry(
            dialog,
            width=250,
            height=35
        )

        precio_entry.insert(0, str(extra.precio))
        precio_entry.pack()

        def guardar():

            try:

                nuevo_nombre = nombre_entry.get().strip()
                nuevo_precio_texto = precio_entry.get().strip()

                if not nuevo_nombre or not nuevo_precio_texto:

                    messagebox.showerror(
                        "Error",
                        "Todos los campos son obligatorios"
                    )

                    return

                nuevo_precio = float(nuevo_precio_texto)

                if nuevo_precio <= 0:

                    messagebox.showerror(
                        "Error",
                        "El precio debe ser mayor a 0"
                    )

                    return

                actualizar_extra(
                    extra.id,
                    nuevo_nombre,
                    nuevo_precio
                )

                dialog.destroy()

                self.cargar_extras()

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "El precio debe ser numérico"
                )

        guardar_btn = ctk.CTkButton(
            dialog,
            text="Guardar",
            fg_color="#C67C3E",
            hover_color="#A8642D",
            command=guardar
        )

        guardar_btn.pack(
            pady=20
        )

    def eliminar_extra_ui(self, extra_id):

        confirmacion = messagebox.askyesno(
            "Confirmar",
            "¿Eliminar este extra?"
        )

        if not confirmacion:
            return

        eliminar_extra(extra_id)

        self.cargar_extras()
