# patterns/observer.py
# Patron: Observer
#
# TODO: Clase Observer (interface)
#   - TODO: Metodo actualizar(evento, datos) que implementaran los observadores concretos
#
# TODO: Clase EventBus (Singleton)
#   - TODO: Atributo privado _suscriptores (diccionario: evento -> lista de observers)
#   - TODO: Atributo privado _instancia (Singleton)
#   - TODO: Metodo get_instance() que retorne la unica instancia
#   - TODO: Metodo suscribir(evento, observer) que agregue un observer a un evento
#   - TODO: Metodo desuscribir(evento, observer) que remueva un observer
#   - TODO: Metodo notificar(evento, datos) que recorra observers y llame actualizar()
