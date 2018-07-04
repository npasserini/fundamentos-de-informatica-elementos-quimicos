# -*- coding: utf-8 -*-
import re
from fixture import compuestos
from medio import Medio

def buscarCompuesto(nombre):
  return (compuesto for compuesto in compuestos if compuesto.nombre == nombre).next()

class DescripcionMedio:
  def __init__(self, descripcion):
    self.medio = Medio()
    self.incorporarDescripcion(descripcion)

  def incorporarDescripcion(self, descripcion):
    for formula in re.findall("\[(.*?)\]", descripcion):
      self.medio.agregarComponente(buscarCompuesto(formula), 1)

  def apareceCompuesto(self, comp):
      ''' indica si un compuesto está presente en la descripción. '''
      return comp in self.medio.compuestosPresentes()

  def molesCompuesto(self, comp):
      ''' indica cuántos moles de un compuesto incluye la descripción. '''
      return self.medio.molesDeComponente(comp)

  def quienesAparecen(self, listaDeCompuestos):
      ''' indica cuáles de los compuestos incluidos en la lista, aparecen en la descripción. '''
      return self.medio.compuestosPresentes() & set(listaDeCompuestos)

  def agregarAMedio(self, medio, compuesto):
      ''' agrega al medio, la cantidad de moles del compuesto que están incluidas en la descripción. '''
      medio.agregarComponente(compuesto, self.molesCompuesto(compuesto))

