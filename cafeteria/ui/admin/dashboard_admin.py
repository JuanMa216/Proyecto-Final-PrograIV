import customtkinter as ctk

from ui.admin.productos_view import ProductosView
from ui.admin.empleados_view import EmpleadosView


class DashboardAdmin(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        usuario,
        logout_callback
    ):

        super().__init__(parent)

        self.parent = parent
        self.usuario = usuario
        self.logout_callback = logout_callback

        self.configure(
            fg_color="#111111"
        )

        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            fg_color="#1b1b1b"
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content = ctk.CTkFrame(
            self,
            fg_color="#111111"
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="CAFETERÍA",
            font=("Arial", 28, "bold")
        )

        self.logo.pack(pady=40)

        self.productos_btn = ctk.CTkButton(
            self.sidebar,
            text="Productos",
            command=self.show_productos
        )

        self.productos_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.empleados_btn = ctk.CTkButton(
            self.sidebar,
            text="Empleados",
            command=self.show_empleados
        )

        self.empleados_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.logout_btn = ctk.CTkButton(
            self.sidebar,
            text="Cerrar Sesión",
            fg_color="red",
            hover_color="#aa0000",
            command=self.logout_callback
        )

        self.logout_btn.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=20
        )

        self.welcome = ctk.CTkLabel(
            self.content,
            text=f"Bienvenido {usuario.nombre}",
            font=("Arial", 35, "bold")
        )

        self.welcome.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def show_productos(self):

        self.clear_content()

        ProductosView(
            self.content
        ).pack(
            fill="both",
            expand=True
        )

    def show_empleados(self):

        self.clear_content()

        empleados_view = EmpleadosView(
            self.content,
            self.usuario
        )

        empleados_view.pack(
            fill="both",
            expand=True
        )