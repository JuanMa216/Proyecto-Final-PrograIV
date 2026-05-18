import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

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

        self.configure(
            fg_color="#0F0F0F"
        )

        self.logo_image = ctk.CTkImage(
            light_image=Image.open(
                "assets/logo.png"
            ),
            size=(120, 120)
        )

        self.card = ctk.CTkFrame(
            self,
            width=430,
            height=560,
            fg_color="#1A1A1A",
            corner_radius=30
        )

        self.card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.logo = ctk.CTkLabel(
            self.card,
            text="",
            image=self.logo_image
        )

        self.logo.pack(
            pady=(40, 20)
        )

        self.title = ctk.CTkLabel(
            self.card,
            text="CAFETERÍA",
            font=("Montserrat", 34, "bold")
        )

        self.title.pack()

        self.subtitle = ctk.CTkLabel(
            self.card,
            text="Sistema inteligente de cafetería",
            text_color="gray"
        )

        self.subtitle.pack(
            pady=(0, 30)
        )

        self.username_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Usuario",
            width=320,
            height=50,
            corner_radius=15
        )

        self.username_entry.pack(
            pady=10
        )

        self.password_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Contraseña",
            show="*",
            width=320,
            height=50,
            corner_radius=15
        )

        self.password_entry.pack(
            pady=10
        )

        self.login_button = ctk.CTkButton(
            self.card,
            text="Ingresar",
            width=320,
            height=50,
            fg_color="#C67C3E",
            hover_color="#A8642D",
            corner_radius=15,
            font=("Montserrat", 18, "bold"),
            command=self.iniciar_sesion
        )

        self.login_button.pack(
            pady=30
        )

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