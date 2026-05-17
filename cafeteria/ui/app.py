# ui/app.py
# Patron: N/A (controlador principal de la UI)
#
# TODO: Clase App
#   - TODO: Atributo ventana (la ventana raiz de CustomTkinter)
#   - TODO: Atributo contenedor (CTkFrame donde se intercambian vistas)
#   - TODO: Atributo empleado_actual (usuario logueado)
#   - TODO: Atributo facade (instancia de CafeteriaFacade)
#   - TODO: Metodo __init__(ventana) que configure la ventana y muestre login
#   - TODO: Metodo mostrar_vista(vista) que destruya la vista actual y cree una nueva
#   - TODO: Metodo iniciar_sesion(empleado) que guarde el empleado y muestre vista segun rol
#   - TODO: Metodo cerrar_sesion() que limpie empleado_actual y vuelva al login
#   - TODO: Metodo _obtener_vista_por_rol(empleado) que decida que vista mostrar segun el puesto
