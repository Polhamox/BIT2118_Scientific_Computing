import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART A: ORIGINAL NUMERICAL DIFFERENTIATION
# ==========================================

print("PART A: ORIGINAL NUMERICAL DIFFERENTIATION")

# Function: f(x) = x^2
def f(x):
    return x**2

# Point at which the derivative is calculated
x = 3.0

# Small step size
h = 0.01

# Forward difference
forward_difference = (f(x + h) - f(x)) / h

# Backward difference
backward_difference = (f(x) - f(x - h)) / h

# Central difference
central_difference = (f(x + h) - f(x - h)) / (2 * h)

# Exact derivative: f'(x) = 2x
exact_derivative = 2 * x

print("Function: f(x) = x^2")
print("Point x:", x)
print("Step size:", h)
print("Forward difference:", round(forward_difference, 6))
print("Backward difference:", round(backward_difference, 6))
print("Central difference:", round(central_difference, 6))
print("Exact derivative:", exact_derivative)


# ==========================================
# PART B: CHANGE THE STEP SIZE
# ==========================================

print("\nPART B: CHANGED STEP SIZE")

# Change step size from 0.01 to 0.1
new_h = 0.1

new_central_difference = (
    f(x + new_h) - f(x - new_h)
) / (2 * new_h)

print("Original step size:", h)
print("New step size:", new_h)
print("Original central difference:", round(central_difference, 6))
print("New central difference:", round(new_central_difference, 6))
print("Exact derivative:", exact_derivative)


# ==========================================
# PART C: REAL-WORLD APPLICATION
# ==========================================

print("\nPART C: REAL-WORLD APPLICATION")

# Distance travelled by a vehicle:
# s(t) = 5t^2 + 10t
def distance(t):
    return 5 * t**2 + 10 * t

# Calculate speed at 4 seconds
time = 4.0
time_step = 0.01

# Central difference estimates instantaneous speed
speed = (
    distance(time + time_step) -
    distance(time - time_step)
) / (2 * time_step)

# Exact speed: s'(t) = 10t + 10
exact_speed = 10 * time + 10

print("Distance function: s(t) = 5t^2 + 10t")
print("Time:", time, "seconds")
print("Estimated speed:", round(speed, 4), "m/s")
print("Exact speed:", exact_speed, "m/s")


# ==========================================
# PART D: NUMERICAL DIFFERENTIATION GRAPH
# ==========================================

print("\nPART D: NUMERICAL DIFFERENTIATION GRAPH")

# Generate points for the function
x_values = np.linspace(0, 6, 100)
y_values = f(x_values)

# Tangent line at x = 3
tangent_line = exact_derivative * (x_values - x) + f(x)

plt.figure(figsize=(10, 6))

plt.plot(x_values, y_values, label="f(x) = x^2")
plt.plot(
    x_values,
    tangent_line,
    linestyle="--",
    label="Tangent at x = 3"
)

plt.scatter(
    [x],
    [f(x)],
    label="Point of differentiation"
)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical Differentiation of f(x) = x^2")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_15_Numerical_Differentiation/documentation/"
    "Task_15_Differentiation_Graph.png"
)

plt.show()

print("Graph saved successfully.")