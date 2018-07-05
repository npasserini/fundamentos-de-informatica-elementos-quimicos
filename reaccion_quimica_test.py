# -*- coding: utf-8 -*-
import unittest
from fixture import *
from reaccion_quimica import ReaccionQuimica

class ReaccionQuimicaTest(unittest.TestCase):
  def setUp(self):
    self.reaccion = ReaccionQuimica([agua, metano], [co2]) # Ponele :P

  def test_sePuedeAplicar(self):
    self.assertTrue(self.reaccion.sePuedeAplicar(medioRaro))
    self.assertFalse(self.reaccion.sePuedeAplicar(otroMedio)) # No tiene metano

  def test_maximoMoles(self):
    self.assertEqual(20, self.reaccion.maximoMoles(medioRaro)) # Los 20 del metano en medioRaro
    self.assertRaises(ValueError, self.reaccion.maximoMoles, otroMedio) # No tiene metano

  def test_aplicar(self):
    medio = createMedioRaro()
    self.reaccion.aplicar(medio, 0.5)
    self.assertEqual(100 - 10, medio.molesDeComponente(agua))
    self.assertEqual(21, medio.molesDeComponente(nh3)) # sin cambios
    self.assertEqual(20 - 10, medio.molesDeComponente(metano))
    self.assertEqual(14 + 10, medio.molesDeComponente(co2))
