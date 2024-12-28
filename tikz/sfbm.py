import matplotlib.pyplot as plt
import numpy as np

# Beam parameters
L = 10  # Length of the beam (meters)
P = 20  # Point load (kN)
a = 4   # Distance from left support (meters)

# Reactions
R_A = P * (L - a) / L
R_B = P * a / L

# Shear Force and Bending Moment
x = np.linspace(0, L, 1000)
V = np.piecewise(x, [x < a, x >= a],
                 [lambda x: R_A, lambda x: R_A - P])
M = np.piecewise(x, [x < a, x >= a],
                 [lambda x: R_A * x,
                  lambda x: R_A * x - P * (x - a)])

# Plotting
plt.figure(figsize=(12, 6))

# Shear Force Diagram
plt.subplot(2, 1, 1)
plt.plot(x, V, label='Shear Force', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Shear Force Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.legend()
plt.grid(True)

# Bending Moment Diagram
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