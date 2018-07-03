import unittest
from fixture import *

class TablaPeriodicaTest(unittest.TestCase):
  def test_elementos(self):
    self.assertEqual(4, len(tabla.elementos()))
    self.assertEqual(0, len(tablaVacia.elementos()))

  def test_elementoS(self):
    self.assertEqual(6, tabla.elementoS('C').numeroAtomico())
    self.assertEqual(None, tabla.elementoS('XXX'))
    self.assertEqual(None, tablaVacia.elementoS('C'))

  def test_elementoN(self):
    self.assertEqual(14, tabla.elementoN(7).pesoAtomico())
    self.assertEqual(None, tabla.elementoN(123))
    self.assertEqual(None, tablaVacia.elementoN(7))

  def test_agregarElemento(self):
    tabla.agregarElemento(oxigeno)
    self.assertEqual(4, len(tabla.elementos()))
