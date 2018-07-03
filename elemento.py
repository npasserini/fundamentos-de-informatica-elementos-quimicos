class Elemento:
  def __init__(self, miSimbolo, protones, neutrones, miValencia):
    self.miSimbolo = miSimbolo
    self.protones = protones
    self.neutrones = neutrones
    self.miValencia = miValencia

  def cantProtones(self):
    return self.protones

  def cantNeutrones(self):
    return self.neutrones

  def cantElectrones(self):
    return self.protones

  def numeroAtomico(self):
    return self.cantProtones()

  def pesoAtomico(self):
    return self.cantProtones() + self.cantNeutrones()

  def valencia(self):
    return self.miValencia

  def simbolo(self):
    return self.miSimbolo