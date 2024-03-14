import numpy as np
import matplotlib.pyplot as plt

# Koordinat pusat dan radius lingkaran
centers = [(1, 2), (3, 4), (5, 3), (2, 5), (4, 1)]
radii = [0.5, 0.8, 1.0, 0.7, 0.4]

# Membuat figur dan sumbu
fig, ax = plt.subplots()

# Plot lingkaran
for center, radius in zip(centers, radii):
    circle = plt.Circle(center, radius, color='blue', fill=False)
    ax.add_artist(circle)

# Penyesuaian batas sumbu
plt.xlim(0, 6)
plt.ylim(0, 6)

# Label sumbu dan judul
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Lingkaran')

# Tampilkan plot
plt.grid(True)
plt.show()
