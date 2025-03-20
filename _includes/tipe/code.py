import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 750, 750)  # Temps en jours
R, r = 1.5, 0.3  # Rayons en UA (exemple pour Mars)
omega1 = 2 * np.pi / 687  # Période du déférent (Mars : 687 jours)
omega2 = 2 * np.pi / 50   # Période fictive de l’épicycle

x = R * np.cos(omega1 * t) + r * np.cos(omega2 * t)
y = R * np.sin(omega1 * t) + r * np.sin(omega2 * t)

plt.plot(x, y)
plt.title("Trajectoire épicycloïdale de Mars")
plt.xlabel("x (UA)")
plt.ylabel("y (UA)")
plt.grid()
plt.show()