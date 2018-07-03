# -*- coding: utf-8 -*-
import elemento
import tabla_periodica
import compuesto

oxigeno = elemento.Elemento("O", 8, 8, 4)
hidrogeno = elemento.Elemento("H", 1, 0, 1)
carbono = elemento.Elemento("C", 6, 6, 4)
nitrogeno = elemento.Elemento("N", 7, 7, 3)

tabla = tabla_periodica.TablaPeriodica([
  oxigeno,
  hidrogeno,
  carbono,
  nitrogeno
])

tablaVacia = tabla_periodica.TablaPeriodica()

nh3 = compuesto.Compuesto('NH3')
nh3.agregarAtomo(tabla.elementoS("N"))
nh3.agregarAtomos(tabla.elementoS("H"), 3)
nh3.enlazarConVarios("N1", ["H1", "H2", "H3"])

# El higrógeno tiene un enlace sobrante
sobranol = compuesto.Compuesto('sobranol')
sobranol.agregarAtomo(oxigeno)
sobranol.agregarAtomo(hidrogeno)
sobranol.enlazarConVarios("O1", ["H1", "H1"])

# El oxígeno tiene un enlace disponible
disponiblol = compuesto.Compuesto('disponiblol')
disponiblol.agregarAtomo(oxigeno)
disponiblol.agregarAtomo(hidrogeno)
disponiblol.enlazar("O1", "H1")

# El oxígeno tiene un enlace disponible
inexistenciol = compuesto.Compuesto('inexistenciol')
inexistenciol.enlazar("O!", "H1")
