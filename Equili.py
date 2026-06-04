import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
PEV = 2818       # Punto de Equilibrio en Volumen
PEI = 56364      # Punto de Equilibrio en Ingresos
P = 20           # Precio de venta
CV = 26500       # Costos Variables Totales
Cvu = 9          # Costo Variable Unitario
CF = 31000       # Costos Fijos
# Rango de unidades para el gráfico
unidades = np.arange(0, 5000, 100)
# Calcular el Ingreso Total (IT), Costo Variable Total (CVT) y Costo Total (CT)
ingreso_total = unidades * P
costo_variable_total = unidades * Cvu
costo_total = CF + costo_variable_total
# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(unidades, ingreso_total, label="Ingresos Totales (IT)", color="blue", linestyle="--", linewidth=2)
plt.plot(unidades, costo_total, label="Costos Totales (CT)", color="red", linestyle="-", linewidth=2)
plt.axvline(x=PEV, color="green", linestyle=":", linewidth=2, label=f"PEV = {PEV} unidades")
plt.axhline(y=PEI, color="purple", linestyle=":", linewidth=2, label=f"PEI = S/ {PEI}")
# Etiquetas y leyenda
plt.title("Gráfico de Punto de Equilibrio")
plt.xlabel("Unidades Vendidas")
plt.ylabel("Monto en S/")
plt.legend(loc="best")
plt.grid()
# Mostrar el gráfico
plt.show()
