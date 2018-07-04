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
    return self.componentes.keys()

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
