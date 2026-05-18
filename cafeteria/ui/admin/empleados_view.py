import customtkinter as ctk
from tkinter import messagebox

from database.conexion import get_session
from models.usuario import Usuario

from services.auth_service import hash_password


class EmpleadosView(ctk.CTkFrame):

    def __init__(self, parent, usuario_actual):
        super().__init__(parent)

        self.usuario_actual = usuario_actual

        self.configure(
            fg_color="#111111"
        )

        self.title = ctk.CTkLabel(
            self,
            text="Empleados",
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
            width=180,
            height=40
        )

        self.nombre_entry.grid(
            row=0,
            column=0,
            padx=10,
            pady=20
        )

        self.username_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Username",
            width=180,
            height=40
        )

        self.username_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        self.password_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Password",
            width=180,
            height=40
        )

        self.password_entry.grid(
            row=0,
            column=2,
            padx=10
        )

        self.rol_option = ctk.CTkOptionMenu(
            self.form_frame,
            values=[
                "admin",
                "cajero",
                "barista"
            ]
        )

        self.rol_option.grid(
            row=0,
            column=3,
            padx=10
        )

        self.crear_button = ctk.CTkButton(
            self.form_frame,
            text="Contratar",
            command=self.crear_empleado,
            fg_color="#C67C3E",
            hover_color="#A8642D",
            height=40
        )

        self.crear_button.grid(
            row=0,
            column=4,
            padx=10
        )

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="#111111"
        )

        self.scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.cargar_empleados()

    def cargar_empleados(self):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        session = get_session()

        empleados = session.query(Usuario).all()

        row = 0
        column = 0

        for empleado in empleados:

            card = ctk.CTkFrame(
                self.scroll,
                width=280,
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
                text=empleado.nombre,
                font=("Arial", 24, "bold")
            )

            nombre.pack(
                pady=(35, 10)
            )

            username = ctk.CTkLabel(
                card,
                text=empleado.username,
                text_color="gray",
                font=("Arial", 16)
            )

            username.pack()

            rol = ctk.CTkLabel(
                card,
                text=empleado.rol.upper(),
                text_color="#C67C3E",
                font=("Arial", 18, "bold")
            )

            rol.pack(
                pady=15
            )

            despedir_btn = ctk.CTkButton(
                card,
                text="Despedir",
                fg_color="red",
                hover_color="#aa0000",
                command=lambda e=empleado: self.eliminar_empleado(e.id)
            )

            despedir_btn.pack(
                padx=20,
                pady=10,
                fill="x"
            )

            column += 1

            if column > 2:
                column = 0
                row += 1

    def crear_empleado(self):

        try:

            session = get_session()

            usuario = Usuario(
                nombre=self.nombre_entry.get(),
                username=self.username_entry.get(),
                password=hash_password(
                    self.password_entry.get()
                ),
                rol=self.rol_option.get()
            )

            session.add(usuario)
            session.commit()

            messagebox.showinfo(
                "Empleado",
                "Empleado contratado"
            )

            self.nombre_entry.delete(0, "end")
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")

            self.cargar_empleados()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def eliminar_empleado(self, empleado_id):

        try:

            session = get_session()

            empleado = session.query(Usuario).filter_by(
                id=empleado_id
            ).first()

            if not empleado:
                return

            if empleado.id == self.usuario_actual.id:

                messagebox.showerror(
                    "Error",
                    "No puedes despedirte a ti mismo"
                )

                return

            confirmacion = messagebox.askyesno(
                "Confirmar",
                f"¿Despedir a {empleado.nombre}?"
            )

            if not confirmacion:
                return

            session.delete(empleado)
            session.commit()

            self.cargar_empleados()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )