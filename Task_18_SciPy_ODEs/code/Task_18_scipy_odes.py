import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# PART A: ORIGINAL DIFFERENTIAL EQUATION
print("PART A: SOLVING ODE USING SCIPY")

# Differential equation: dy/dt = -0.5y
def decay_model(t, y):
    return -0.5 * y


initial_value = [100]
time_interval = (0, 5)

solution = solve_ivp(
    decay_model,
    time_interval,
    initial_value,
    t_eval=np.linspace(0, 5, 51)
)

# Exact solution
exact_values = 100 * np.exp(-0.5 * solution.t)

print("Initial value:", initial_value[0])
print("Time interval:", time_interval)
print("Final SciPy solution:", round(solution.y[0][-1], 4))
print("Final exact value:", round(exact_values[-1], 4))
print("Absolute error:", round(
    abs(solution.y[0][-1] - exact_values[-1]), 6
))


# PART B: CHANGE THE INITIAL VALUE
print("\nPART B: CHANGED INITIAL VALUE")

new_initial_value = [150]

new_solution = solve_ivp(
    decay_model,
    time_interval,
    new_initial_value,
    t_eval=np.linspace(0, 5, 51)
)

new_exact_value = 150 * np.exp(-0.5 * new_solution.t[-1])

print("New initial value:", new_initial_value[0])
print("New final SciPy solution:",
      round(new_solution.y[0][-1], 4))
print("New exact value:", round(new_exact_value, 4))


# PART C: REAL-WORLD APPLICATION
print("\nPART C: MEDICINE CONCENTRATION MODEL")

# Medicine concentration decreases at a rate of 0.2 per hour.
def medicine_model(t, concentration):
    return -0.2 * concentration


medicine_solution = solve_ivp(
    medicine_model,
    (0, 5),
    [500],
    t_eval=np.linspace(0, 5, 51)
)

medicine_exact = 500 * np.exp(-0.2 * medicine_solution.t[-1])

print("Initial medicine concentration: 500 mg")
print("Time period: 5 hours")
print("Final estimated concentration:",
      round(medicine_solution.y[0][-1], 4), "mg")
print("Exact concentration:",
      round(medicine_exact, 4), "mg")


# PART D: GRAPH
print("\nPART D: SCIPY ODE GRAPH")

plt.figure(figsize=(9, 5))

plt.plot(
    solution.t,
    solution.y[0],
    label="SciPy numerical solution"
)

plt.plot(
    solution.t,
    exact_values,
    linestyle="--",
    label="Exact solution"
)

plt.xlabel("Time")
plt.ylabel("Value of y")
plt.title("Numerical Solution of an ODE Using SciPy")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_18_SciPy_ODEs/documentation/Task_18_SciPy_ODE_Graph.png"
)

plt.show()