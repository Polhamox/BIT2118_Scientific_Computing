import numpy as np
import matplotlib.pyplot as plt
import os


# PART A: JACOBI METHOD

def jacobi_method(A, b, tolerance=1e-8, max_iterations=500):
    n = len(b)
    x = np.zeros(n)
    errors = []

    for iteration in range(max_iterations):
        x_new = np.zeros(n)

        for i in range(n):
            total = 0

            for j in range(n):
                if i != j:
                    total += A[i][j] * x[j]

            x_new[i] = (b[i] - total) / A[i][i]

        error = np.linalg.norm(x_new - x)
        errors.append(error)
        x = x_new

        if error < tolerance:
            break

    return x, iteration + 1, errors


# PART B: GAUSS-SEIDEL METHOD

def gauss_seidel_method(A, b, tolerance=1e-8, max_iterations=500):
    n = len(b)
    x = np.zeros(n)
    errors = []

    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            total = 0

            for j in range(n):
                if i != j:
                    total += A[i][j] * x[j]

            x[i] = (b[i] - total) / A[i][i]

        error = np.linalg.norm(x - x_old)
        errors.append(error)

        if error < tolerance:
            break

    return x, iteration + 1, errors


# ORIGINAL HEAT TRANSFER SYSTEM

A = np.array([
    [2, -1, 0, 0, 0],
    [-1, 2, -1, 0, 0],
    [0, -1, 2, -1, 0],
    [0, 0, -1, 2, -1],
    [0, 0, 0, -1, 2]
], dtype=float)

b = np.array([100, 0, 0, 0, 20], dtype=float)

print("PART A: JACOBI METHOD")

jacobi_solution, jacobi_iterations, jacobi_errors = jacobi_method(A, b)

print("Jacobi solution:")
print(jacobi_solution)
print("Number of iterations:", jacobi_iterations)
print("Final error:", jacobi_errors[-1])


print("\nPART B: GAUSS-SEIDEL METHOD")

gs_solution, gs_iterations, gs_errors = gauss_seidel_method(A, b)

print("Gauss-Seidel solution:")
print(gs_solution)
print("Number of iterations:", gs_iterations)
print("Final error:", gs_errors[-1])


# PART C: COMPARE WITH DIRECT SOLUTION

print("\nPART C: DIRECT SOLUTION COMPARISON")

direct_solution = np.linalg.solve(A, b)

print("Direct solution:")
print(direct_solution)

print("Jacobi difference:", np.linalg.norm(jacobi_solution - direct_solution))
print("Gauss-Seidel difference:", np.linalg.norm(gs_solution - direct_solution))


# PART D: CHANGE AN INPUT VALUE

print("\nPART D: CHANGED BOUNDARY TEMPERATURE")

b_changed = np.array([120, 0, 0, 0, 20], dtype=float)

changed_solution, changed_iterations, changed_errors = jacobi_method(
    A, b_changed
)

print("Changed boundary values:", b_changed)
print("New Jacobi solution:")
print(changed_solution)
print("Number of iterations:", changed_iterations)


# PART E: REAL-WORLD APPLICATION - BUILDING TEMPERATURE

print("\nPART E: BUILDING TEMPERATURE MODEL")

building_b = np.array([80, 0, 0, 0, 10], dtype=float)

building_solution, building_iterations, building_errors = gauss_seidel_method(
    A, building_b
)

print("Building boundary temperatures:", building_b)
print("Estimated internal temperatures:")
print(building_solution)
print("Number of iterations:", building_iterations)


# PART F: CONVERGENCE GRAPH

print("\nPART F: GENERATING CONVERGENCE GRAPH")

os.makedirs("Task_08_Iterative_Linear/documentation", exist_ok=True)

plt.figure(figsize=(9, 6))

plt.semilogy(
    range(1, len(jacobi_errors) + 1),
    jacobi_errors,
    label="Jacobi Method"
)

plt.semilogy(
    range(1, len(gs_errors) + 1),
    gs_errors,
    label="Gauss-Seidel Method"
)

plt.xlabel("Number of Iterations")
plt.ylabel("Error (log scale)")
plt.title("Convergence of Jacobi and Gauss-Seidel Methods")
plt.legend()
plt.grid(True)

plt.tight_layout()

graph_path = (
    "Task_08_Iterative_Linear/documentation/"
    "Task_08_Convergence_Graph.png"
)

plt.savefig(graph_path, dpi=300, bbox_inches="tight")

print("Graph successfully saved to:", graph_path)

plt.show()