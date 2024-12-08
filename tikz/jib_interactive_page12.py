import math

# Prompt user for inputs
W = float(input("Enter the weight (W) in kN: "))
theta_jib = float(input("Enter the angle of the jib from the positive x-axis (in degrees): "))
theta_tie = float(input("Enter the angle of the tie from the positive x-axis (in degrees): "))

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
# J * (T_over_J * sin(theta_tie) + sin_theta_jib) = W
# Solve for J:
J = W / (T_over_J * sin_theta_tie + sin_theta_jib)

# Calculate T:
T = T_over_J * J

# Results
print(f"\nResults:")
print(f"Force in the jib (J): {J:.4f} kN")
print(f"Force in the tie (T): {T:.4f} kN")