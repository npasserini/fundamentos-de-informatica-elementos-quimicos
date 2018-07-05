# -*- coding: utf-8 -*-
class ReaccionQuimica:
  def __init__(self, reactivos, productos):
    self.reactivos = reactivos
    self.productos = productos

  def sePuedeAplicar(self, medio):
    """ Indica si el medio incluye todos los reactivos de la reacción, de forma tal que la reacción se pueda llevar a cabo. """
    return all(reactivo in medio.compuestosPresentes() for reactivo in self.reactivos)

  def maximoMoles(self, medio):
    """ Indica cuántos moles de cada reactivo pueden participar, como máximo, de aplicarse la reacción en el medio indicado. """
    if not self.sePuedeAplicar(medio):
      raise ValueError("La reacción no se puede aplicar en el medio.")
    return min(medio.molesDeComponente(reactivo) for reactivo in self.reactivos)

  def aplicar(self, medio, proporcion):
    """
      Aplica la reacción al medio indicado, modificando su composición: se consumen los reactivos y se generan los productos.
      La proporcion es respecto de la cantidad máxima de moles que podría participar.
    """
    moles = self.maximoMoles(medio) * proporcion
    for reactivo in self.reactivos:
      medio.quitarComponente(reactivo, moles)

    for producto in self.productos:
      medio.agregarComponente(producto, moles)
