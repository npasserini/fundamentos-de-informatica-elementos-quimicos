# -*- coding: utf-8 -*-
import unittest
from fixture import *
from medio import Medio

class MedioTest(unittest.TestCase):
  def test_agregarComponente(self):
    medio = Medio()
    medio.agregarComponente(agua, 160)
    self.assertEqual(160, medio.molesDeComponente(agua))
    self.assertEqual(0, medio.molesDeComponente(nh3))

    medio.agregarComponente(agua, 160)
    medio.agregarComponente(nh3, 6)
    self.assertEqual(320, medio.molesDeComponente(agua))
    self.assertEqual(6, medio.molesDeComponente(nh3))

    self.assertEqual(100, medioRaro.molesDeComponente(agua))
    self.assertEqual(21, medioRaro.molesDeComponente(nh3))
    self.assertEqual(20, medioRaro.molesDeComponente(metano))
    self.assertEqual(14, medioRaro.molesDeComponente(co2))


  def test_masaTotal(self):
    """masa total	3093 gramos"""
    self.assertEqual(3093, medioRaro.masaTotal())

  def test_elementosPresentes(self):
    """ Elementos presentes	hidrógeno, oxígeno, nitrógeno y carbono. """
    self.assertItemsEqual([hidrogeno, oxigeno, nitrogeno, carbono], medioRaro.elementosPresentes())

  def test_compuestosPresentes(self):
    """ Compuestos presentes	agua, amoníaco, metano y dióxido de carbono. """
    self.assertItemsEqual([agua, nh3, metano, co2], medioRaro.compuestosPresentes())

  def test_cantMolesElemento(self):
    """ Cantidad de moles por elemento	oxígeno: 128; hidrógeno: 343. """
    self.assertEqual(128, medioRaro.cantMolesElemento(oxigeno))
    self.assertEqual(343, medioRaro.cantMolesElemento(hidrogeno))

  def test_masaDeCompuesto(self):
    """ Masa por compuesto	agua: 1800 gramos; amoníaco: 357 gramos. """
    self.assertEqual(1800, medioRaro.masaDeCompuesto(agua))
    self.assertEqual(357, medioRaro.masaDeCompuesto(nh3))

  def test_masaDeElemento(self):
    """ Masa por elemento	oxígeno: 2048 gramos; carbono: 408 gramos. """
    self.assertEqual(2048, medioRaro.masaDeElemento(oxigeno))
    self.assertEqual(408, medioRaro.masaDeElemento(carbono))

  def test_proporcionCompuestoSobreMasa(self):
    """ Proporción de un compuesto sobre masa	agua: 0.5819. """
    self.assertAlmostEqual(0.5819, medioRaro.proporcionCompuestoSobreMasa(agua), 3)

  def test_proporcionElementoSobreMasa(self):
    """ Proprción de un elemento sobre masa	oxígeno: 0.6621; hidrógeno: 0.1108. """
    self.assertAlmostEqual(0.6621, medioRaro.proporcionElementoSobreMasa(oxigeno), 3)
    self.assertAlmostEqual(0.1108, medioRaro.proporcionElementoSobreMasa(hidrogeno), 3)

  ### Opcionales ###
  def test_escalar(self):
    """ medioRaro.escalar(3) pasa la cantidad de agua de 100 moles a 300, la de amoníaco de 21 moles a 63, etc.; """
    medio = createMedioRaro()
    medio.escalar(3)
    self.assertEqual(300, medio.molesDeComponente(agua))
    self.assertEqual(63, medio.molesDeComponente(nh3))

    """ mientras que medioRaro.escalar(0.5) deja al medio con 50 moles de agua, 10.5 de amoníaco, etc. """
    medio = createMedioRaro()
    medio.escalar(0.5)
    self.assertEqual(50, medio.molesDeComponente(agua))
    self.assertEqual(10.5, medio.molesDeComponente(nh3))

  def test_incorporarMedio(self):
    medio = Medio()
    medio.incorporarMedio(medioRaro)
    self.assertEqual(100, medio.molesDeComponente(agua))
    self.assertEqual(21, medio.molesDeComponente(nh3))
    self.assertEqual(20, medio.molesDeComponente(metano))
    self.assertEqual(14, medio.molesDeComponente(co2))

    medio.incorporarMedio(otroMedio)
    self.assertEqual(125, medio.molesDeComponente(agua)) # 100 + 25
    self.assertEqual(31, medio.molesDeComponente(nh3)) # 21 + 10
    self.assertEqual(20, medio.molesDeComponente(metano)) # sin cambios
    self.assertEqual(14, medio.molesDeComponente(co2)) # sin cambios

  def test_masMedio(self):
    medio = medioRaro.masMedio(otroMedio)
    self.assertEqual(125, medio.molesDeComponente(agua)) # 100 + 25
    self.assertEqual(31, medio.molesDeComponente(nh3)) # 21 + 10
    self.assertEqual(20, medio.molesDeComponente(metano)) # sin cambios
    self.assertEqual(14, medio.molesDeComponente(co2)) # sin cambios
