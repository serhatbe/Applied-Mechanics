import numpy as np
import matplotlib.pyplot as plt

# Beam parameters
L = 8  # Length between supports (meters)
a = 2  # Overhang length on each side (meters)
w = 4  # Uniformly distributed load (kN/m)

# Total beam length including overhangs
total_length = L + 2 * a

# Reactions at supports
R_A = w * total_length * (total_length / 2 - a) / L
R_B = w * total_length - R_A

# Define x-coordinates along the beam
x = np.linspace(0, total_length, 1000)

# Shear Force (V)
V = np.piecewise(x, 
                 [x < a,  # Left overhang
                  (x >= a) & (x <= a + L),  # Main span
                  x > a + L],  # Right overhang
                 [lambda x: -w * x,
                  lambda x: R_A - w * (x - a),
                  lambda x: R_A - w * L - w * (x - (a + L))])

# Bending Moment (M)
M = np.piecewise(x, 
                 [x < a,  # Left overhang
                  (x >= a) & (x <= a + L),  # Main span
                  x > a + L],  # Right overhang
                 [lambda x: -w * x**2 / 2,
                  lambda x: R_A * (x - a) - w * (x - a)**2 / 2,
                  lambda x: R_A * (x - a) - w * L * (x - (a + L)) - w * (x - (a + L))**2 / 2])

# Plotting
plt.figure(figsize=(12, 9))

# Plot the beam and the distributed load
plt.subplot(3, 1, 1)
beam_x = np.linspace(0, total_length, 100)
beam_y = np.zeros_like(beam_x)  # Beam lies along the x-axis
load_y = w/4 * np.ones_like(beam_x)  # Represent the UDL on the positive side

# Beam line
plt.plot(beam_x, beam_y, color='black', linewidth=4, label='Beam')

# UDL shading
plt.fill_between(beam_x, beam_y, load_y, color='blue', alpha=0.3, label='UDL')

# Supports as triangles
support_x = [a, a + L]
support_y = [0, 0]
for sx, sy in zip(support_x, support_y):
    triangle = plt.Polygon([[sx - 0.1, sy], [sx + 0.1, sy], [sx, sy - 0.2]],
                           color='red', label='Support')
    plt.gca().add_patch(triangle)

# Add labels and grid
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Beam with Uniformly Distributed Load (UDL)')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Load (kN/m)')
plt.ylim(-1, w * 1.5)  # Adjust vertical scale for better appearance
plt.legend(loc='upper left')
plt.grid(True)

# Shear Force Diagram (SFD)
plt.subplot(3, 1, 2)
plt.plot(x, V, label='Shear Force', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Shear Force Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.legend()
plt.grid(True)

# Bending Moment Diagram (BMD)
plt.subplot(3, 1, 3)
plt.plot(x, M, label='Bending Moment', color='red')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Bending Moment Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (kNm)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()