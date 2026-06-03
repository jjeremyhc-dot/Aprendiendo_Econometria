import numpy as np
import matplotlib.pyplot as plt

# 1. Definir la función de demanda
def cantidad_demandada(P, a, b):
    """
    Función de demanda lineal: Q = a - b*P
    a: Intercepto (Cantidad si el precio es 0)
    b: Pendiente (Cambio en Q por cada cambio en P)
    """
    return a - b * P

# 2. Definir la función de elasticidad
def elasticidad_precio_demanda(P, Q, b):
    """
    Calcula la elasticidad precio de la demanda (puntual) para una demanda lineal.
    Ed = (dQ/dP) * (P/Q). Para Q = a - bP, dQ/dP = -b.
    """
    # El valor de la elasticidad es negativo, por convención se usa el valor absoluto.
    return abs(-b * (P / Q))

# --- Parámetros de ejemplo ---
a = 100  # Intercepto
b = 2    # Pendiente (negativa implícita)
# -----------------------------

# 3. Calcular y mostrar la elasticidad en un punto específico
precio_ejemplo = 20
cantidad_ejemplo = cantidad_demandada(precio_ejemplo, a, b)
epd_ejemplo = elasticidad_precio_demanda(precio_ejemplo, cantidad_ejemplo, b)

print(f"--- Punto de Cálculo ---")
print(f"Precio (P): {precio_ejemplo}")
print(f"Cantidad (Q): {cantidad_ejemplo}")
print(f"Elasticidad Precio de la Demanda (EPD): {epd_ejemplo:.2f}")

if epd_ejemplo > 1:
    print("**Demanda Elástica** (un cambio en el precio causa un cambio porcentual mayor en la cantidad)")
elif epd_ejemplo < 1:
    print("**Demanda Inelástica** (un cambio en el precio causa un cambio porcentual menor en la cantidad)")
else:
    print("**Elasticidad Unitaria** (el cambio porcentual es el mismo)")

# Rango de precios para la gráfica (desde 0 hasta el precio máximo donde Q=0)
precio_max = a / b
P_values = np.linspace(0.1, precio_max - 0.1, 50) # Evitamos P=0 y Q=0
# Calcular las cantidades y elasticidades para cada precio
Q_values = cantidad_demandada(P_values, a, b)
EPD_values = elasticidad_precio_demanda(P_values, Q_values, b)

# Definir los puntos clave de la elasticidad
P_unitario = (a / b) / 2 # Precio donde la elasticidad es unitaria
Q_unitario = cantidad_demandada(P_unitario, a, b)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Gráfica 1: Curva de Demanda (P vs. Q) ---
ax1.plot(Q_values, P_values, label=f'Demanda Q = {a} - {b}P', color='blue')
ax1.set_title('Curva de Demanda y Regiones de Elasticidad', fontsize=14)
ax1.set_xlabel('Cantidad (Q)')
ax1.set_ylabel('Precio (P)')
ax1.grid(True, linestyle='--', alpha=0.6)

# Marcar el punto de Elasticidad Unitaria
ax1.scatter(Q_unitario, P_unitario, color='black', zorder=5)
ax1.annotate('EPD = 1 (Unitaria)', (Q_unitario, P_unitario), textcoords="offset points", xytext=(-5,10), ha='right')

# Resaltar regiones
# Región Elástica (P > P_unitario)
ax1.fill_between(Q_values[P_values > P_unitario], P_unitario, P_values[P_values > P_unitario], color='red', alpha=0.1, label='Elástica (|Ed| > 1)')
# Región Inelástica (P < P_unitario)
ax1.fill_between(Q_values[P_values < P_unitario], P_values[P_values < P_unitario], P_unitario, color='green', alpha=0.1, label='Inelástica (|Ed| < 1)')

ax1.legend()
ax1.invert_yaxis() # Por convención, a veces se invierte el eje Y para que Q crezca hacia la derecha

# --- Gráfica 2: Elasticidad vs. Precio (P) ---
ax2.plot(P_values, EPD_values, label='Elasticidad |Ed|', color='red')
ax2.axhline(1, color='black', linestyle='--', label='|Ed| = 1 (Unitaria)')
ax2.set_title('Elasticidad Precio de la Demanda vs. Precio', fontsize=14)
ax2.set_xlabel('Precio (P)')
ax2.set_ylabel('|Ed| (Valor Absoluto de la Elasticidad)')
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()
ax2.set_ylim(0, max(EPD_values) * 1.1)

plt.tight_layout()
plt.show()
