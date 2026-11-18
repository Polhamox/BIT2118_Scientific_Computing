
import numpy as np
from scipy.linalg import lu_factor, lu_solve


# ==================================================
# PART A: GAUSSIAN ELIMINATION
# ==================================================

print("PART A: GAUSSIAN ELIMINATION")

# Original system of three linear equations:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
])

b = np.array([8.0, -11.0, -3.0])

print("\nCoefficient matrix:")
print(A)

print("\nConstant values:")
print(b)


# Create an augmented matrix
augmented = np.column_stack((A, b))

print("\nOriginal augmented matrix:")
print(augmented)


# Forward elimination
n = len(b)

for i in range(n):

    # Partial pivoting
    max_row = i + np.argmax(np.abs(augmented[i:, i]))

    augmented[[i, max_row]] = augmented[[max_row, i]]

    for j in range(i + 1, n):

        factor = augmented[j, i] / augmented[i, i]

        augmented[j, i:] = (
            augmented[j, i:] - factor * augmented[i, i:]
        )


print("\nUpper triangular matrix after elimination:")
print(augmented)


# Back substitution
x = np.zeros(n)

for i in range(n - 1, -1, -1):

    x[i] = (
        augmented[i, -1]
        - np.dot(augmented[i, i + 1:n], x[i + 1:n])
    ) / augmented[i, i]


print("\nSolution using Gaussian elimination:")
print(f"x = {x[0]:.2f}")
print(f"y = {x[1]:.2f}")
print(f"z = {x[2]:.2f}")

print("\nVerification:")
print("Calculated values:", A @ x)


# ==================================================
# PART B: CHANGING AN INPUT VALUE
# ==================================================

print("\n\nPART B: CHANGING AN INPUT VALUE")

# Change the first constant from 8 to 9
b_changed = np.array([9.0, -11.0, -3.0])

changed_solution = np.linalg.solve(A, b_changed)

print("\nNew constant values:")
print(b_changed)

print("\nNew solution:")
print(f"x = {changed_solution[0]:.2f}")
print(f"y = {changed_solution[1]:.2f}")
print(f"z = {changed_solution[2]:.2f}")

print("\nVerification:")
print(A @ changed_solution)


# ==================================================
# PART C: LU DECOMPOSITION
# ==================================================

print("\n\nPART C: LU DECOMPOSITION")

# LU decomposition separates A into lower and upper
# triangular matrices, with pivoting handled by SciPy.

lu, piv = lu_factor(A)

print("\nLU factorisation completed.")
print("The coefficient matrix has been factorised.")


# Solve the first measurement system
b1 = np.array([8.0, -11.0, -3.0])

solution1 = lu_solve((lu, piv), b1)

print("\nFirst measurement results:")
print(solution1)

print("Verification:")
print(A @ solution1)


# Solve a second system using the same factorisation
b2 = np.array([9.0, -11.0, -3.0])

solution2 = lu_solve((lu, piv), b2)

print("\nSecond measurement results:")
print(solution2)

print("Verification:")
print(A @ solution2)


# ==================================================
# PART D: MODIFIED REAL-WORLD APPLICATION
# ==================================================

print("\n\nPART D: ENGINEERING SIMULATION")

# An engineering simulation uses the same coefficient
# matrix but receives new measurement values.

# Measurements from two different simulation periods
measurement_1 = np.array([8.0, -11.0, -3.0])
measurement_2 = np.array([10.0, -11.0, -3.0])

# Reuse the existing LU factorisation
result_1 = lu_solve((lu, piv), measurement_1)
result_2 = lu_solve((lu, piv), measurement_2)

print("\nSimulation period 1:")
print("Calculated values:", result_1)

print("\nSimulation period 2:")
print("Calculated values:", result_2)

print("\nConclusion:")
print("LU decomposition allows the same coefficient matrix")
print("to be reused when solving systems with new measurements.")
