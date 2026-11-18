import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, minimize_scalar


# PART A: ORIGINAL NUMERICAL OPTIMIZATION
print("PART A: ORIGINAL NUMERICAL OPTIMIZATION")

# Function to minimize: f(x) = (x - 3)^2 + 4
def objective_function(x):
    return (x[0] - 3) ** 2 + 4


initial_guess = [0]

result = minimize(objective_function, initial_guess)

print("Initial guess:", initial_guess[0])
print("Optimal value of x:", round(result.x[0], 4))
print("Minimum function value:", round(result.fun, 4))
print("Optimization successful:", result.success)


# PART B: CHANGE AN INPUT PARAMETER
print("\nPART B: CHANGED INITIAL GUESS")

new_initial_guess = [10]

new_result = minimize(objective_function, new_initial_guess)

print("New initial guess:", new_initial_guess[0])
print("New optimal value of x:", round(new_result.x[0], 4))
print("New minimum function value:", round(new_result.fun, 4))


# PART C: REAL-WORLD APPLICATION
print("\nPART C: BUSINESS COST MINIMIZATION")

# A business estimates its daily production cost.
# Cost(x) = 2x^2 - 40x + 500
# x represents the number of production batches.
def production_cost(x):
    return 2 * x ** 2 - 40 * x + 500


business_result = minimize_scalar(
    production_cost,
    bounds=(0, 20),
    method="bounded"
)

print("Production batches:", round(business_result.x, 4))
print("Minimum production cost:",
      round(business_result.fun, 4))
print("Optimization successful:", business_result.success)


# PART D: GRAPH
print("\nPART D: OPTIMIZATION GRAPH")

x_values = np.linspace(-2, 8, 200)
y_values = (x_values - 3) ** 2 + 4

plt.figure(figsize=(9, 5))

plt.plot(x_values, y_values, label="Objective function")

plt.scatter(
    result.x[0],
    result.fun,
    marker="o",
    label="Minimum point"
)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical Optimization Using SciPy")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_19_Numerical_Optimization/documentation/Task_19_Optimization_Graph.png"
)

plt.show()