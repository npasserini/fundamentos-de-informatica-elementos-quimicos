import elemento
import tabla_periodica
import compuesto

oxigeno = elemento.Elemento("O", 8, 8, 4)
hidrogeno = elemento.Elemento("H", 1, 0, 1)
carbono = elemento.Elemento("C", 6, 6, 4)
nitrogeno = elemento.Elemento("N", 7, 7, 1)

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
nh3.enlazarConVarios("N1", ["H2", "H3", "H4"])