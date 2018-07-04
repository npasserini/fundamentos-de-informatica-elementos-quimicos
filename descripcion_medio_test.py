# -*- coding: utf-8 -*-
import unittest
from fixture import *
from descripcion_medio import DescripcionMedio

class MedioTest(unittest.TestCase):
  def setUp(self):
    self.miDescripcion = DescripcionMedio("[H2O][CO2][H2O][CH4]")

  def test_apareceCompuesto(self):
    self.assertTrue(self.miDescripcion.apareceCompuesto(agua))
    self.assertTrue(self.miDescripcion.apareceCompuesto(co2))
    self.assertFalse(self.miDescripcion.apareceCompuesto(nh3))

  def test_molesCompuesto(self):
    self.assertEqual(2, self.miDescripcion.molesCompuesto(agua))
    self.assertEqual(1, self.miDescripcion.molesCompuesto(co2))
    self.assertEqual(0, self.miDescripcion.molesCompuesto(nh3))

  def test_quienesAparecen(self):
    self.assertItemsEqual([agua, metano], self.miDescripcion.quienesAparecen([agua, nh3, metano]))

  def test_agregarAMedio(self):
    # El agua en medioRaro aumenta en dos moles, pasando de 100 a 102
    medio = createMedioRaro()
    self.miDescripcion.agregarAMedio(medio, agua)
    self.assertEqual(102, medio.molesDeComponente(agua))

    # El metano en medio aumenta en un mol, pasando de 20 a 21
    medio = createMedioRaro()
    self.miDescripcion.agregarAMedio(medio, metano)
    self.assertEqual(21, medio.molesDeComponente(metano))

    # No se produce ningún efecto, porque miDescripcion no incluye ningún mol de amoníaco
    medio = createMedioRaro()
    self.miDescripcion.agregarAMedio(medio, nh3)
    self.assertEqual(21, medio.molesDeComponente(nh3))