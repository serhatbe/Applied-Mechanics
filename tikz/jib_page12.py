import math

# Given data
W = 37.5  # Weight in kN
theta_jib = 48  # Jib angle from x-axis in degrees
theta_tie = 192  # Tie angle from x-axis in degrees

# Trigonometric values
cos_theta_jib = math.cos(math.radians(theta_jib))
sin_theta_jib = math.sin(math.radians(theta_jib))
cos_theta_tie = math.cos(math.radians(theta_tie))
sin_theta_tie = math.sin(math.radians(theta_tie))

# Horizontal equilibrium: T * cos(theta_tie) + J * cos(theta_jib) = 0
# Solve for T in terms of J:
# T = J * cos(theta_jib) / -cos(theta_tie)
T_over_J = cos_theta_jib / -cos_theta_tie

# Vertical equilibrium: T * sin(theta_tie) + J * sin(theta_jib) = W
# Substitute T = T_over_J * J:
# (T_over_J * J) * sin(theta_tie) + J * sin(theta_jib) = W
# J * (T_over_J * sin(theta_tie) + sin(theta_jib)) = W
# Solve for J:
J = W / (T_over_J * sin_theta_tie + sin_theta_jib)

# Calculate T:
T = T_over_J * J

# Results
print(f"Force in the jib (J): {J:.2f} kN")
print(f"Force in the tie (T): {T:.2f} kN")