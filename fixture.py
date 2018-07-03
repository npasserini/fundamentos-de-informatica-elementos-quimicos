import elemento
import tabla_periodica

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