import matplotlib.pyplot as plt
import numpy as np

# Tentukan wilayah (domain)
x = np.linspace(-12, 12, 1000)

# Persamaan untuk lingkaran kepala Mickey Mouse
head_top = 5 + np.sqrt(25 - (x - 5) ** 2)
head_bottom = 5 - np.sqrt(25 - (x - 5) ** 2)

# Persamaan untuk telinga Mickey Mouse
ear_right_top = 9 + np.sqrt(4 - (x - 9) ** 2)
ear_right_bottom = 9 - np.sqrt(4 - (x - 9) ** 2)
ear_left_top = 9 + np.sqrt(4 - (x - 1) ** 2)
ear_left_bottom = 9 - np.sqrt(4 - (x - 1) ** 2)

# Plot kepala Mickey Mouse
plt.fill_between(x, head_bottom, head_top, color='black')

# Plot telinga Mickey Mouse
plt.fill_between(x, ear_right_bottom, ear_right_top, color='red')
plt.fill_between(x, ear_left_bottom, ear_left_top, color='magenta')

# Tampilkan plot
plt.axis('equal')
plt.grid()
plt.show()
