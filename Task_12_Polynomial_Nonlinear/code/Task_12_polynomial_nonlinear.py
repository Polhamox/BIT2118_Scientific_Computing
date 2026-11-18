import numpy as np
from scipy.optimize import fsolve

# ==================================================
# PART A: POLYNOMIAL EQUATION SOLVING
# ==================================================

print("PART A: POLYNOMIAL EQUATION")

# Polynomial: x^2 - 5x + 6 = 0

coefficients = [1, -5, 6]

roots = np.roots(coefficients)

print("Polynomial: x^2 - 5x + 6 = 0")
print("Calculated roots:", roots)

for root in roots:
    print(f"Verification for x = {root}:",
          root**2 - 5*root + 6)


# ==================================================
# PART B: CHANGING A POLYNOMIAL COEFFICIENT
# ==================================================

print("\nPART B: CHANGED POLYNOMIAL")

# Change the constant from 6 to 4.
# New polynomial: x^2 - 5x + 4 = 0

changed_coefficients = [1, -5, 4]

changed_roots = np.roots(changed_coefficients)

print("New polynomial: x^2 - 5x + 4 = 0")
print("New roots:", changed_roots)


# ==================================================
# PART C: NONLINEAR EQUATION SOLVING
# ==================================================

print("\nPART C: NONLINEAR EQUATION")

# Nonlinear equation: x^3 - 2x - 5 = 0

def nonlinear_function(x):
    return x**3 - 2*x - 5


initial_guess = 2.0

nonlinear_root = fsolve(
    nonlinear_function,
    initial_guess
)

print("Equation: x^3 - 2x - 5 = 0")
print("Initial guess:", initial_guess)
print("Calculated root:", nonlinear_root[0])
print("Function value at root:",
      nonlinear_function(nonlinear_root[0]))


# ==================================================
# PART D: CHANGING THE INITIAL GUESS
# ==================================================

print("\nPART D: CHANGED INITIAL GUESS")

new_guess = 3.0

new_nonlinear_root = fsolve(
    nonlinear_function,
    new_guess
)

print("New initial guess:", new_guess)
print("Calculated root:", new_nonlinear_root[0])
print("Function value at root:",
      nonlinear_function(new_nonlinear_root[0]))


# ==================================================
# PART E: REAL-WORLD APPLICATION
# RECTANGULAR GARDEN AREA
# ==================================================

print("\nPART E: GARDEN DIMENSION APPLICATION")

# A rectangular garden has an area of 40 square metres.
# Its length is 3 metres greater than its width.
#
# Let width = x
# Length = x + 3
#
# Therefore:
# x(x + 3) = 40
# x^2 + 3x - 40 = 0

def garden_equation(width):
    return width**2 + 3*width - 40


garden_coefficients = [1, 3, -40]

garden_roots = np.roots(garden_coefficients)

# Select the positive root because a width cannot be negative.
garden_width = max(garden_roots)

garden_length = garden_width + 3

calculated_area = garden_width * garden_length

print("Required garden area: 40 square metres")
print("Garden width:", garden_width, "metres")
print("Garden length:", garden_length, "metres")
print("Verified area:", calculated_area, "square metres")


print("\nTask 12 completed successfully.")