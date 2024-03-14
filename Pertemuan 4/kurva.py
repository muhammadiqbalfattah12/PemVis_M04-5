import numpy as np
import matplotlib.pyplot as plt

# Persamaan untuk kurva parabolik (y = ax^2 + bx + c)
a = 1
b = 0
c = 0

# Persamaan kurva
x = np.linspace(-5, 5, 100)  # Definisi domain
y = a * x**2 + b * x + c  # Persamaan kurva parabolik

# Plot kurva
plt.plot(x, y, color='blue', label='y = x^2')

# Penyesuaian batas sumbu
plt.xlim(-5, 5)
plt.ylim(0, 10)

# Label sumbu dan judul
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Kurva Parabolik')

# Tampilkan plot
plt.legend()  # Menampilkan legenda
plt.grid(True)  # Menampilkan grid
plt.show()
