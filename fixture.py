# -*- coding: utf-8 -*-
from elemento import Elemento
from tabla_periodica import TablaPeriodica
from compuesto import Compuesto
from medio import Medio

oxigeno = Elemento("O", 8, 8, 4)
hidrogeno = Elemento("H", 1, 0, 1)
carbono = Elemento("C", 6, 6, 4)
nitrogeno = Elemento("N", 7, 7, 3)

tabla = TablaPeriodica([
  oxigeno,
  hidrogeno,
  carbono,
  nitrogeno
])

tablaVacia = TablaPeriodica()

nh3 = Compuesto('NH3')
nh3.agregarAtomo(nitrogeno)
nh3.agregarAtomos(hidrogeno, 3)
nh3.enlazarConVarios("N1", ["H1", "H2", "H3"])

agua = Compuesto("Agua")
agua.agregarAtomo(oxigeno)
agua.agregarAtomos(hidrogeno, 2)
agua.enlazarConVarios("O1", ["H1", "H2"])

metano = Compuesto("Metano")
metano.agregarAtomo(carbono)
metano.agregarAtomos(hidrogeno, 4)
metano.enlazarConVarios("C1", ["H1", "H2", "H3", "H4"])

co2 = Compuesto("CO2")
co2.agregarAtomo(carbono)
co2.agregarAtomos(oxigeno, 2)
co2.enlazarConVarios("C1", ["O1", "O2"])

# El higrógeno tiene un enlace sobrante
sobranol = Compuesto('sobranol')
sobranol.agregarAtomo(oxigeno)
sobranol.agregarAtomo(hidrogeno)
sobranol.enlazarConVarios("O1", ["H1", "H1"])

# El oxígeno tiene un enlace disponible
disponiblol = Compuesto('disponiblol')
disponiblol.agregarAtomo(oxigeno)
disponiblol.agregarAtomo(hidrogeno)
disponiblol.enlazar("O1", "H1")

# El oxígeno tiene un enlace disponible
inexistenciol = Compuesto('inexistenciol')
inexistenciol.enlazar("O1", "H1")

# Elementos inconexos
inconexiol = Compuesto('inconexiol')
inconexiol.agregarAtomo(oxigeno)
inconexiol.agregarAtomo(hidrogeno)

medioRaro = Medio()
medioRaro.agregarComponente(agua, 100)
medioRaro.agregarComponente(nh3, 6)
medioRaro.agregarComponente(metano, 20)
medioRaro.agregarComponente(co2, 14)
medioRaro.agregarComponente(nh3, 15)