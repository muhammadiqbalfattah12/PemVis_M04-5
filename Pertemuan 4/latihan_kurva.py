import numpy as np
import matplotlib.pyplot as plt

# Persamaan untuk kurva (misal: y = x^2)
x = np.linspace(-5, 5, 100)  # Definisi domain
y = x ** 2  # Persamaan kurva

# Plot kurva
plt.plot(x, y, color='blue', label='y = x^2')

# Penyesuaian batas sumbu
plt.xlim(-5, 5)
plt.ylim(0, 25)

# Label sumbu dan judul
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Kurva Quadrat')

# Tampilkan plot
plt.legend()  # Menampilkan legenda
plt.grid(True)  # Menampilkan grid
plt.show()
