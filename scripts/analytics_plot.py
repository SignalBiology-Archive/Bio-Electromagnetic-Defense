import matplotlib.pyplot as plt
import numpy as np

# Time in minutes
time = np.arange(0, 60, 1)

# Potential energy in the hydrogel (Relative Units)
no_mitigation = np.exp(-0.01 * time) # Slow decay
shunting_only = np.exp(-0.1 * time)  # Faster decay
chelation_shunting = np.exp(-0.5 * time) # Rapid collapse

plt.figure(figsize=(10,6))
plt.plot(time, no_mitigation, label='No Mitigation (Slow Leak)', color='red')
plt.plot(time, shunting_only, label='Galvanic Shunting Only', color='blue')
plt.plot(time, chelation_shunting, label='Chelation + Shunting (Targeted)', color='green', linewidth=3)

plt.title('Hydrogel Electromechanical Decay Curves')
plt.xlabel('Time (Minutes)')
plt.ylabel('Piezoelectric Potential (Energy Density)')
plt.legend()
plt.grid(True)
plt.show()
