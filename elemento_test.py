import unittest
from fixture import *

class ElementoTest(unittest.TestCase):
  def test_oxigeno(self):
    self.assertEqual(8, oxigeno.cantProtones())
    self.assertEqual(8, oxigeno.cantNeutrones())
    self.assertEqual(8, oxigeno.cantElectrones())
    self.assertEqual(8, oxigeno.numeroAtomico())
    self.assertEqual(16, oxigeno.pesoAtomico())
    self.assertEqual(4, oxigeno.valencia())
    self.assertEqual("O", oxigeno.simbolo())

  def test_hidrogeno(self):
    self.assertEqual(1, hidrogeno.cantProtones())
    self.assertEqual(0, hidrogeno.cantNeutrones())
    self.assertEqual(1, hidrogeno.cantElectrones())
    self.assertEqual(1, hidrogeno.numeroAtomico())
    self.assertEqual(1, hidrogeno.pesoAtomico())
    self.assertEqual(1, hidrogeno.valencia())
    self.assertEqual("H", hidrogeno.simbolo())
