import customtkinter as ctk
from tkinter import messagebox

from services.producto_service import obtener_productos, obtener_extras
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

        self.mostrar_selector_extras(producto)

    def mostrar_selector_extras(self, producto):

        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Agregar: {producto.nombre}")
        dialog.geometry("400x500")
        dialog.configure(fg_color="#111111")
        dialog.resizable(False, False)

        dialog.transient(self)
        dialog.update_idletasks()
        dialog.grab_set()

        main_frame = ctk.CTkScrollableFrame(
            dialog,
            fg_color="#111111"
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        nombre = ctk.CTkLabel(
            main_frame,
            text=producto.nombre,
            font=("Arial", 24, "bold")
        )

        nombre.pack(pady=(0, 5))

        precio_base = ctk.CTkLabel(
            main_frame,
            text=f"${producto.precio}",
            text_color="#C67C3E",
            font=("Arial", 20, "bold")
        )

        precio_base.pack(pady=(0, 15))

        cant_frame = ctk.CTkFrame(
            main_frame,
            fg_color="transparent"
        )

        cant_frame.pack(pady=10)

        cant_label = ctk.CTkLabel(
            cant_frame,
            text="Cantidad:",
            font=("Arial", 16)
        )

        cant_label.pack(side="left", padx=(0, 10))

        cantidad_var = ctk.IntVar(value=1)

        cant_spin = ctk.CTkEntry(
            cant_frame,
            textvariable=cantidad_var,
            width=60,
            height=35,
            justify="center"
        )

        cant_spin.pack(side="left")

        extras_label = ctk.CTkLabel(
            main_frame,
            text="Extras:",
            font=("Arial", 18, "bold")
        )

        extras_label.pack(
            anchor="w",
            pady=(20, 10)
        )

        extras_vars = []

        extras = obtener_extras()

        if not extras:

            sin_extras = ctk.CTkLabel(
                main_frame,
                text="No hay extras disponibles",
                text_color="gray"
            )

            sin_extras.pack(anchor="w")

        for extra in extras:

            frame = ctk.CTkFrame(
                main_frame,
                fg_color="#1b1b1b",
                corner_radius=10,
                height=45
            )

            frame.pack(
                fill="x",
                pady=4
            )

            frame.pack_propagate(False)

            var = ctk.BooleanVar(value=False)

            extras_vars.append({
                "var": var,
                "extra": extra
            })

            check = ctk.CTkCheckBox(
                frame,
                text=f"{extra.nombre}  (${extra.precio})",
                variable=var,
                font=("Arial", 15),
                fg_color="#C67C3E",
                hover_color="#A8642D"
            )

            check.pack(
                side="left",
                padx=10
            )

        total_var = ctk.StringVar(value=f"Total: ${producto.precio}")

        total_label = ctk.CTkLabel(
            main_frame,
            textvariable=total_var,
            font=("Arial", 22, "bold"),
            text_color="#C67C3E"
        )

        total_label.pack(pady=(20, 15))

        def actualizar_total():

            extra_total = sum(
                ev["extra"].precio for ev in extras_vars
                if ev["var"].get()
            )

            total = (producto.precio + extra_total) * cantidad_var.get()

            total_var.set(f"Total: ${total}")

        for ev in extras_vars:

            ev["var"].trace_add(
                "write",
                lambda *_: actualizar_total()
            )

        cantidad_var.trace_add(
            "write",
            lambda *_: actualizar_total()
        )

        def confirmar():

            try:

                cantidad = cantidad_var.get()

                if cantidad < 1:

                    messagebox.showerror(
                        "Error",
                        "La cantidad debe ser mayor a 0"
                    )

                    return

                seleccionados = [
                    {
                        "nombre": ev["extra"].nombre,
                        "precio": ev["extra"].precio
                    }
                    for ev in extras_vars if ev["var"].get()
                ]

                self.agregar_al_carrito(
                    producto,
                    cantidad,
                    seleccionados
                )

                dialog.destroy()

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Cantidad inválida"
                )

        btn_frame = ctk.CTkFrame(
            dialog,
            fg_color="#111111"
        )

        btn_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        confirmar_btn = ctk.CTkButton(
            btn_frame,
            text="Agregar al Pedido",
            fg_color="#C67C3E",
            hover_color="#A8642D",
            height=45,
            font=("Arial", 16, "bold"),
            command=confirmar
        )

        confirmar_btn.pack(fill="x")

    def agregar_al_carrito(
        self,
        producto,
        cantidad,
        extras
    ):

        key = (producto.id, tuple(e["nombre"] for e in extras))

        if key in self.carrito:

            self.carrito[key]["cantidad"] += cantidad

        else:

            self.carrito[key] = {
                "producto": producto,
                "cantidad": cantidad,
                "extras": extras
            }

        self.actualizar_pedido()

    def actualizar_pedido(self):

        self.lista.delete("1.0", "end")

        total = 0

        for item in self.carrito.values():

            producto = item["producto"]
            cantidad = item["cantidad"]
            extras = item.get("extras", [])

            extra_total = sum(e["precio"] for e in extras)

            precio_unitario = producto.precio + extra_total

            subtotal = precio_unitario * cantidad

            texto = f"{producto.nombre} x{cantidad} - ${subtotal}\n"

            for extra in extras:

                texto += f"   +{extra['nombre']} ${extra['precio']}\n"

            texto += "\n"

            self.lista.insert("end", texto)

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
            extras = item.get("extras", [])

            productos.append({
                "producto_id": producto.id,
                "cantidad": cantidad,
                "extras": extras
            })

        pedido = crear_pedido(productos)

        messagebox.showinfo(
            "Pedido",
            f"Pedido #{pedido.id} creado"
        )

        self.carrito.clear()

        self.actualizar_pedido()