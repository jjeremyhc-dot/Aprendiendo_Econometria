import matplotlib.pyplot as plt
import numpy as np

 #datos#
P= 25
ymax= 500
xmax= 10
x= np.array([0,xmax])
y= 500-(2*P)
plt.figure(figsize=(8,9))
plt.plot(x, y, color= 'green', label=f'Demanda: {ymax}-2{P}P', linewidth=2)
plt.xlabel("Cantidad")
plt.ylabel("Precio")
plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()
