# -*- coding: utf-8 -*-
from __future__ import division # :P

class Medio:
  def __init__(self):
    self.componentes = {}

  def agregarComponente(self, componente, moles):
    self.componentes[componente] = self.molesDeComponente(componente) + moles

  def masaTotal(self):
    """ Considerando la cantidad de moles de cada elemento. """
    return sum(componente.masaMolar() * self.molesDeComponente(componente) for componente in self.componentes)

  def elementosPresentes(self):
    """ Considerando todos los compuestos involucrados. """
    return set(elemento for componente in self.componentes for elemento in componente.elementosPresentes())

  def compuestosPresentes(self):
    """ También sin repetidos. """
    return set(self.componentes.keys())

  def cantMolesElemento(self, elem):
    """ La cantidad total de moles del elemento indicado en el medio, considerando todos los compuestos incluidos y sus cantidades. """
    return sum(componente.cantAtomosDe(elem) * moles for componente, moles in self.componentes.items())

  def masaDeCompuesto(self, comp):
    return comp.masaMolar() * self.componentes[comp]

  def masaDeElemento(self, elem):
    return self.cantMolesElemento(elem) * elem.pesoAtomico()

  def proporcionCompuestoSobreMasa(self, comp):
    return self.masaDeCompuesto(comp) / self.masaTotal()

  def proporcionElementoSobreMasa(self, elem):
    return self.masaDeElemento(elem) / self.masaTotal()

  # Auxiliares
  def molesDeComponente(self, componente):
    return self.componentes[componente] if self.componentes.has_key(componente) else 0


  ### Opcionales ###
  def escalar(self, numero):
    """ Multiplica las cantidades de cada componente por el número indicado. """
    for componente, moles in self.componentes.items():
      self.componentes[componente] = moles * numero

  def incorporarMedio(self, otroMedio):
    """ Suma a las cantidades del medio que recibe la operación, las incluidas en otroMedio. """
    for componente, moles in otroMedio.componentes.items():
      self.agregarComponente(componente, moles)

  def masMedio(self, otroMedio):
    """
      Devuelve un nuevo medio, que es la suma entre el medio que recibe la operación y otroMedio.
      Ni el medio que recibe la operación no debe modificarse ni otroMedio deben modificarse.
    """
    resultado = Medio()
    resultado.incorporarMedio(self)
    resultado.incorporarMedio(otroMedio)
    return resultado