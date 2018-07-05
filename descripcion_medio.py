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

  def compuestosDesconocidos(self, listaCompuestos):
    """
      Devuelve la lista de las fórmulas presentes en la descripción, que no coinciden con ninguno de los compuestos en listaCompuestos.
      P.ej. miDescripcion.compuestosDesconocidos([agua,nh3,metano]) devuelve ["CO2"],
      porque la lista suministrada no incluye al dióxido de carbono, que sí está presente en la descripción.
    """
    return (compuesto.nombre for compuesto in self.medio.compuestosPresentes() - set(listaCompuestos))


  def agregarTodosAMedio(self, medio, listaCompuestos):
    """ Que agrega al medio todos los compuestos presentes en la descripción que estén en listaCompuestos. """


  def agregarTodosAMedioConEscala(self, medio, listaCompuestos, escala):
    """
      Idem anterior, multiplicando las cantidades a agregar según la escala.
      P.ej. miDescripcion.agregarTodosAMedioConEscala([agua,nh3,metano], 100) agrega 200 moles de agua y 100 de metano.
    """
