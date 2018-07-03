# -*- coding: utf-8 -*-
class TablaPeriodica:
  def __init__(self, elementos = []):
    self._elementos = elementos

  def agregarElemento(self, elemento):
    """Agrega un elemento a la tabla."""
    if (self.elementoS(elemento.simbolo()) is None):
      self._elementos.append(elemento)

  def elementos(self):
    """Devuelve la lista con los elementos agregados."""
    return self._elementos

  def elementoS(self, simbolo):
    """
      Devuelve el elemento de la tabla que tenga el símbolo indicado,
      o None si no hay ningún elemento con tal símbolo.
    """
    return next((elem for elem in self._elementos if elem.simbolo() == simbolo), None)

  def elementoN(self, numero):
    """Análogo a elementoS, buscando por número atómico en lugar de por símbolo."""
    return next((elem for elem in self._elementos if elem.numeroAtomico() == numero), None)
