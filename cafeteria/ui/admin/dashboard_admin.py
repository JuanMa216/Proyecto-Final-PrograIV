import customtkinter as ctk

from ui.admin.productos_view import ProductosView
from ui.admin.empleados_view import EmpleadosView

from services.producto_service import obtener_productos
from services.pedido_service import obtener_pedidos

from database.conexion import get_session
from models.usuario import Usuario


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
            fg_color="#0F0F0F"
        )

        self.sidebar = ctk.CTkFrame(
            self,
            width=270,
            fg_color="#141414"
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content = ctk.CTkFrame(
            self,
            fg_color="#0F0F0F"
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="☕ CAFETERÍA",
            font=("Montserrat", 28, "bold")
        )

        self.logo.pack(pady=40)

        self.dashboard_btn = ctk.CTkButton(
            self.sidebar,
            text="📊 Dashboard",
            height=50,
            corner_radius=15,
            fg_color="#1F1F1F",
            hover_color="#2A2A2A",
            command=self.mostrar_dashboard
        )

        self.dashboard_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.productos_btn = ctk.CTkButton(
            self.sidebar,
            text="📦 Productos",
            height=50,
            corner_radius=15,
            fg_color="#1F1F1F",
            hover_color="#2A2A2A",
            command=self.show_productos
        )

        self.productos_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.empleados_btn = ctk.CTkButton(
            self.sidebar,
            text="👨‍🍳 Empleados",
            height=50,
            corner_radius=15,
            fg_color="#1F1F1F",
            hover_color="#2A2A2A",
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
            height=50,
            corner_radius=15,
            command=self.logout_callback
        )

        self.logout_btn.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=20
        )

        self.mostrar_dashboard()

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def mostrar_dashboard(self):

        self.clear_content()

        title = ctk.CTkLabel(
            self.content,
            text="📊 Dashboard",
            font=("Montserrat", 36, "bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(30, 20)
        )

        stats_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=20
        )

        session = get_session()

        total_productos = len(
            obtener_productos()
        )

        total_pedidos = len(
            obtener_pedidos()
        )

        total_empleados = session.query(
            Usuario
        ).count()

        ventas = 0

        for pedido in obtener_pedidos():
            ventas += pedido.total

        cards = [
            ("📦 Productos", total_productos, "#C67C3E"),
            ("🧾 Pedidos", total_pedidos, "#3498DB"),
            ("👨‍🍳 Empleados", total_empleados, "#9B59B6"),
            ("💰 Ventas", f"${ventas}", "#4CAF50")
        ]

        for titulo, valor, color in cards:

            card = ctk.CTkFrame(
                stats_frame,
                width=260,
                height=180,
                fg_color="#1A1A1A",
                corner_radius=25
            )

            card.pack(
                side="left",
                padx=15,
                pady=20
            )

            card.pack_propagate(False)

            top = ctk.CTkFrame(
                card,
                fg_color=color,
                height=10,
                corner_radius=25
            )

            top.pack(
                fill="x"
            )

            titulo_label = ctk.CTkLabel(
                card,
                text=titulo,
                font=("Montserrat", 22, "bold")
            )

            titulo_label.pack(
                pady=(40, 15)
            )

            valor_label = ctk.CTkLabel(
                card,
                text=str(valor),
                text_color=color,
                font=("Montserrat", 38, "bold")
            )

            valor_label.pack()

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

        EmpleadosView(
            self.content,
            self.usuario
        ).pack(
            fill="both",
            expand=True
        )