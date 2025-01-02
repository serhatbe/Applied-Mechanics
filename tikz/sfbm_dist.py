import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
L = 10  # Length of the beam (meters)
w = 5   # Uniformly distributed load (kN/m)

# Reactions at supports (statics: sum of forces and moments)
R_A = w * L / 2
R_B = w * L / 2

# Define x-coordinates along the beam
x = np.linspace(0, L, 1000)

# Shear Force (V)
V = R_A - w * x

# Bending Moment (M)
M = R_A * x - (w * x**2) / 2

# Plotting
plt.figure(figsize=(12, 6))

# Shear Force Diagram (SFD)
plt.subplot(2, 1, 1)
plt.plot(x, V, label='Shear Force', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Shear Force Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.legend()
plt.grid(True)

# Bending Moment Diagram (BMD)
plt.subplot(2, 1, 2)
plt.plot(x, M, label='Bending Moment', color='red')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Bending Moment Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (kNm)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()