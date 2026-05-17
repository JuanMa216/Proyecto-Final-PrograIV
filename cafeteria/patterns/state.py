# patterns/state.py
# Patron: State
#
# TODO: Clase EstadoPedido (interface / ABC)
#   - TODO: Metodo proximo_estado() que retorne el siguiente estado
#   - TODO: Metodo cancelar() que retorne estado cancelado
#   - TODO: Metodo __str__() que devuelva nombre del estado
#
# TODO: Clase Pendiente (hereda de EstadoPedido)
#   - TODO: proximo_estado() -> Preparando
#
# TODO: Clase Preparando (hereda de EstadoPedido)
#   - TODO: proximo_estado() -> Listo
#
# TODO: Clase Listo (hereda de EstadoPedido)
#   - TODO: proximo_estado() -> Listo (final)
#
# TODO: Clase Cancelado (hereda de EstadoPedido)
#   - TODO: proximo_estado() -> Cancelado (final)
