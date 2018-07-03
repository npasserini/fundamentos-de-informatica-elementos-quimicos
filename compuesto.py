# -*- coding: utf-8 -*-
from __future__ import division # :P

class Compuesto:
  def __init__(self, nombre):
    self.nombre = nombre
    self.atomos = {}
    self.enlaces = []

  def agregarAtomo(self, elemento, nombre = None):
    if nombre is None:
        nombre = elemento.simbolo() + `self.cantAtomosDe(elemento) + 1`
    self.atomos[nombre] = elemento

  def enlazar(self, atomo1, atomo2):
    self.enlaces.append((atomo1, atomo2))

  def enlazarConVarios(self, atomo1, enlaces):
    for atomo2 in enlaces:
      self.enlazar(atomo1, atomo2)

  def cantAtomos(self):
    return len(self.atomos)

  def atomosDe(self, elemento):
    return [ key
      for key, value in self.atomos.items()
      if value == elemento
    ]

  def incluyeAtomo(self, nombre):
    return self.atomos.has_key(nombre)

  def incluyeElemento(self, elemento):
    return elemento in self.atomos.values()

  def elementosPresentes(self):
    return set(elemento for elemento in self.atomos.values())

  # Sobre enlaces
  def cantEnlaces(self):
    return len(self.enlaces)

  def cantEnlacesAtomo(self, atomo):
    return len([enlace for enlace in self.enlaces if atomo in enlace])

  # Sobre masa
  def masaMolar(self):
    return sum(elemento.pesoAtomico() for elemento in self.atomos.values())

  def proporcionSobreMasa(self, elemento):
    return self.masaMolarElemento(elemento) / self.masaMolar()

  # Auxiliares
  def masaMolarElemento(self, elemento):
    return elemento.pesoAtomico() * self.cantAtomosDe(elemento)

  def cantAtomosDe(self, elemento):
    return len(self.atomosDe(elemento))

  ### Opcionales ###
  ## Formas compactas de crear compuestos
  def agregarAtomos(self, elemento, cuantos):
    for _ in range(cuantos):
      self.agregarAtomo(elemento)

  ## Validación de enlaces
  def enlacesOK(self):
    return self.atomosExisten() and not self.atomosConEnlacesSobrantes()

  def atomosConEnlacesSobrantes(self):
    return filter(self.atomoTieneEnlacesSobrantes, self.atomos.keys())

  def atomosConEnlacesDisponibles(self):
    return filter(self.atomoTieneEnlacesDisponibles, self.atomos.keys())

  # Auxiliares
  def atomoTieneEnlacesSobrantes(self, atomo):
    return self.cantEnlacesAtomo(atomo) > self.atomos[atomo].valencia()

  def atomoTieneEnlacesDisponibles(self, atomo):
    return self.cantEnlacesAtomo(atomo) < self.atomos[atomo].valencia()

  def atomosExisten(self):
    return all(map(self.atomosEnlaceExisten, self.enlaces))

  def atomosEnlaceExisten(self, enlace):
    return all(map(self.atomoExiste, enlace))

  def atomoExiste(self, atomo):
    return atomo in self.atomos.keys()