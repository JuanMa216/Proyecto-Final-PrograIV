import customtkinter as ctk
from tkinter import messagebox

from services.auth_service import login


class LoginView(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        show_admin,
        show_cajero,
        show_barista
    ):

        super().__init__(parent)

        self.show_admin = show_admin
        self.show_cajero = show_cajero
        self.show_barista = show_barista

        self.configure(fg_color="#111111")

        self.frame = ctk.CTkFrame(
            self,
            width=400,
            height=400,
            fg_color="#1b1b1b",
            corner_radius=20
        )

        self.frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.title_label = ctk.CTkLabel(
            self.frame,
            text="Bienvenido",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(
            pady=(40, 10)
        )

        self.username_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Usuario",
            width=300,
            height=45
        )

        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Contraseña",
            show="*",
            width=300,
            height=45
        )

        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self.frame,
            text="Ingresar",
            command=self.iniciar_sesion,
            width=300,
            height=45,
            fg_color="#C67C3E"
        )

        self.login_button.pack(pady=30)

    def iniciar_sesion(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        usuario = login(
            username,
            password
        )

        if not usuario:

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )

            return

        if usuario.rol == "admin":
            self.show_admin(usuario)

        elif usuario.rol == "cajero":
            self.show_cajero(usuario)

        elif usuario.rol == "barista":
            self.show_barista(usuario)