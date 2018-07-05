# -*- coding: utf-8 -*-
import re
from medio import Medio

class DescripcionMedio:
  # En lo que sigue formula siempre referencia un string que es el nombre de un compuesto
  # comp o compuesto siempre referencia una instancia de clase Compuesto

  def __init__(self, descripcion):
    self.formulas = {} # Diccionario con fórmulas como claves y cantidad de moles como values
    self.incorporarDescripcion(descripcion)

  def incorporarDescripcion(self, descripcion):
    for formula in re.findall("\[(.*?)\]", descripcion):
      self.agregarFormula(formula, 1)

  def apareceCompuesto(self, compuesto):
    ''' indica si un compuesto está presente en la descripción. '''
    return self.apareceFormula(compuesto.nombre)

  def molesCompuesto(self, comp):
      ''' indica cuántos moles de un compuesto incluye la descripción. '''
      return self.molesFormula(comp.nombre)

  def quienesAparecen(self, listaDeCompuestos):
      ''' indica cuáles de los compuestos incluidos en la lista, aparecen en la descripción. '''
      return (compuesto for compuesto in listaDeCompuestos if self.apareceCompuesto(compuesto))

  def agregarAMedio(self, medio, compuesto):
      ''' agrega al medio, la cantidad de moles del compuesto que están incluidas en la descripción. '''
      medio.agregarComponente(compuesto, self.molesCompuesto(compuesto))

  # Auxiliares
  def agregarFormula(self, formula, moles):
    self.formulas[formula] = self.molesFormula(formula) + moles

  def molesFormula(self, formula):
    return self.formulas[formula] if self.apareceFormula(formula) else 0

  def apareceFormula(self, formula):
    return self.formulas.has_key(formula)

  ### Opcionales ###

  def compuestosDesconocidos(self, listaCompuestos):
    """
      Devuelve la lista de las fórmulas presentes en la descripción, que no coinciden con ninguno de los compuestos en listaCompuestos.
      P.ej. miDescripcion.compuestosDesconocidos([agua,nh3,metano]) devuelve ["CO2"],
      porque la lista suministrada no incluye al dióxido de carbono, que sí está presente en la descripción.
    """
    return set(self.formulas.keys()) - set(map(lambda c: c.nombre, listaCompuestos))


  def agregarTodosAMedio(self, medio, listaCompuestos):
    """ Que agrega al medio todos los compuestos presentes en la descripción que estén en listaCompuestos. """
    for compuesto in listaCompuestos:
      self.agregarAMedio(medio, compuesto)

  def agregarTodosAMedioConEscala(self, medio, listaCompuestos, escala):
    """ Idem anterior, multiplicando las cantidades a agregar según la escala. """
    intermedio = Medio()
    self.agregarTodosAMedio(intermedio, listaCompuestos)
    intermedio.escalar(escala)
    medio.incorporarMedio(intermedio)
