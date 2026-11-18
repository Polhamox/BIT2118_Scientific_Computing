import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid, simpson, quad

# ==========================================
# PART A: ORIGINAL NUMERICAL INTEGRATION
# ==========================================

print("PART A: ORIGINAL NUMERICAL INTEGRATION")

# Function: f(x) = x^2
def f(x):
    return x**2

# Integration limits
a = 0
b = 4

# Number of intervals
n = 100

# Generate equally spaced points
x = np.linspace(a, b, n + 1)
y = f(x)

# Trapezoidal rule
trapezoidal_result = trapezoid(y, x=x)

# Simpson's rule
simpson_result = simpson(y, x=x)

# Exact integration using SciPy quad
exact_result, error = quad(f, a, b)

print("Function: f(x) = x^2")
print("Lower limit:", a)
print("Upper limit:", b)
print("Number of intervals:", n)
print("Trapezoidal result:", round(trapezoidal_result, 6))
print("Simpson's result:", round(simpson_result, 6))
print("Exact result:", round(exact_result, 6))


# ==========================================
# PART B: CHANGE NUMBER OF INTERVALS
# ==========================================

print("\nPART B: CHANGED NUMBER OF INTERVALS")

# Change intervals from 100 to 10
new_n = 10

new_x = np.linspace(a, b, new_n + 1)
new_y = f(new_x)

new_trapezoidal = trapezoid(new_y, x=new_x)
new_simpson = simpson(new_y, x=new_x)

print("Original number of intervals:", n)
print("New number of intervals:", new_n)
print("Original trapezoidal result:", round(trapezoidal_result, 6))
print("New trapezoidal result:", round(new_trapezoidal, 6))
print("Original Simpson's result:", round(simpson_result, 6))
print("New Simpson's result:", round(new_simpson, 6))


# ==========================================
# PART C: REAL-WORLD APPLICATION
# ==========================================

print("\nPART C: REAL-WORLD APPLICATION")

# Water flowing into a tank at a changing rate
# Flow rate: Q(t) = 2t + 5 litres per minute

def flow_rate(t):
    return 2 * t + 5

# Time interval: 0 to 10 minutes
start_time = 0
end_time = 10

# Sample flow rates
time_values = np.linspace(start_time, end_time, 101)
flow_values = flow_rate(time_values)

# Calculate total water using trapezoidal integration
total_water = trapezoid(flow_values, x=time_values)

# Exact total water
exact_water = 150

print("Flow rate function: Q(t) = 2t + 5")
print("Start time:", start_time, "minutes")
print("End time:", end_time, "minutes")
print("Estimated total water:", round(total_water, 4), "litres")
print("Exact total water:", exact_water, "litres")


# ==========================================
# PART D: NUMERICAL INTEGRATION GRAPH
# ==========================================

print("\nPART D: NUMERICAL INTEGRATION GRAPH")

# Generate smooth curve
smooth_x = np.linspace(a, b, 200)
smooth_y = f(smooth_x)

plt.figure(figsize=(10, 6))

plt.plot(smooth_x, smooth_y, label="f(x) = x^2")

# Shade the area under the curve
plt.fill_between(
    smooth_x,
    smooth_y,
    alpha=0.3,
    label="Area under the curve"
)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical Integration of f(x) = x^2")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_16_Numerical_Integration/documentation/"
    "Task_16_Integration_Graph.png"
)

plt.show()

print("Graph saved successfully.")