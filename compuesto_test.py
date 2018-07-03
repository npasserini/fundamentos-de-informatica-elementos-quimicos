import unittest
from fixture import *

class CompuestoTest(unittest.TestCase):
  def test_cantAtomos(self):
    self.assertEqual(4, nh3.cantAtomos())

  def test_atomosDe(self):
    self.assertItemsEqual(
      ["H1", "H2", "H3"],
      nh3.atomosDe(tabla.elementoS('H'))
    )

  def test_incluyeAtomo(self):
    self.assertTrue(nh3.incluyeAtomo("N1"))
    self.assertFalse(nh3.incluyeAtomo("N4"))

  def test_incluyeElemento(self):
    self.assertTrue(nh3.incluyeElemento(tabla.elementoS('N')))
    self.assertFalse(nh3.incluyeElemento(tabla.elementoS('O')))

  def test_elementosPresentes(self):
    self.assertItemsEqual(
      ["N","H"],
      [elem.simbolo() for elem in nh3.elementosPresentes()]
    )

  def test_cantEnlaces(self):
    self.assertEqual(3, nh3.cantEnlaces())

  def test_cantEnlacesAtomo(self):
    self.assertEqual(1, nh3.cantEnlacesAtomo("H2"))

  def test_masaMolar(self):
    self.assertEqual(17, nh3.masaMolar())

  def test_cantAtomosDe(self):
    self.assertEqual(3, nh3.cantAtomosDe(hidrogeno))
    self.assertEqual(1, nh3.cantAtomosDe(nitrogeno))

  def test_masaMolarElemento(self):
    self.assertEqual(3, nh3.masaMolarElemento(hidrogeno))
    self.assertEqual(14, nh3.masaMolarElemento(nitrogeno))

  def test_proporcionSobreMasa(self):
    self.assertAlmostEqual(0.8235, nh3.proporcionSobreMasa(nitrogeno), 4)
