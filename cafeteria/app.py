import customtkinter as ctk

from ui.log.login_view import LoginView
from ui.admin.dashboard_admin import DashboardAdmin
from ui.cajero.pos_view import POSView
from ui.barista.cocina_view import CocinaView


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Cafetería")
        self.geometry("1400x800")
        self.configure(fg_color="#111111")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.current_frame = None

        self.show_login()

    def clear_frame(self):

        if self.current_frame is not None:

            self.current_frame.pack_forget()
            self.current_frame.destroy()

            self.current_frame = None

    def show_login(self):

        self.clear_frame()

        self.current_frame = LoginView(
            self,
            self.show_admin,
            self.show_cajero,
            self.show_barista
        )

        self.current_frame.pack(
            fill="both",
            expand=True
        )

    def show_admin(self, usuario):

        self.clear_frame()

        self.current_frame = DashboardAdmin(
            self,
            usuario,
            self.show_login
        )

        self.current_frame.pack(
            fill="both",
            expand=True
        )

    def show_cajero(self, usuario):

        self.clear_frame()

        self.current_frame = POSView(
            self,
            usuario,
            self.show_login
        )

        self.current_frame.pack(
            fill="both",
            expand=True
        )

    def show_barista(self, usuario):

        self.clear_frame()

        self.current_frame = CocinaView(
            self,
            usuario,
            self.show_login
        )

        self.current_frame.pack(
            fill="both",
            expand=True
        )
