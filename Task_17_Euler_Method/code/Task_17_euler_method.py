import numpy as np
import matplotlib.pyplot as plt


# Euler's Method function
def euler_method(function, initial_value, start_time, end_time, step_size):
    times = np.arange(start_time, end_time + step_size, step_size)
    values = np.zeros(len(times))

    values[0] = initial_value

    for i in range(len(times) - 1):
        values[i + 1] = values[i] + step_size * function(
            times[i], values[i]
        )

    return times, values


# PART A: ORIGINAL DIFFERENTIAL EQUATION
print("PART A: ORIGINAL EULER METHOD")

# Differential equation: dy/dt = -0.5y
def decay_function(t, y):
    return -0.5 * y


initial_value = 100
step_size = 0.1

times, numerical_values = euler_method(
    decay_function, initial_value, 0, 5, step_size
)

# Exact solution: y = 100e^(-0.5t)
exact_values = 100 * np.exp(-0.5 * times)

print("Initial value:", initial_value)
print("Step size:", step_size)
print("Final Euler approximation:", round(numerical_values[-1], 4))
print("Final exact value:", round(exact_values[-1], 4))
print("Absolute error:", round(
    abs(numerical_values[-1] - exact_values[-1]), 4
))


# PART B: CHANGE THE STEP SIZE
print("\nPART B: CHANGED STEP SIZE")

new_step_size = 0.5

new_times, new_values = euler_method(
    decay_function, initial_value, 0, 5, new_step_size
)

new_exact_values = 100 * np.exp(-0.5 * new_times)

print("New step size:", new_step_size)
print("New Euler approximation:", round(new_values[-1], 4))
print("Exact value:", round(new_exact_values[-1], 4))
print("New absolute error:", round(
    abs(new_values[-1] - new_exact_values[-1]), 4
))


# PART C: REAL-WORLD APPLICATION
print("\nPART C: MEDICINE CONCENTRATION DECAY")

# A medicine starts at 500 mg and loses 20% of its
# concentration per hour according to the decay model.
def medicine_decay(t, concentration):
    return -0.2 * concentration


medicine_times, medicine_values = euler_method(
    medicine_decay, 500, 0, 5, 0.5
)

medicine_exact = 500 * np.exp(-0.2 * medicine_times)

print("Initial medicine concentration: 500 mg")
print("Time period: 5 hours")
print("Step size: 0.5 hours")
print("Estimated concentration after 5 hours:",
      round(medicine_values[-1], 4), "mg")
print("Exact concentration after 5 hours:",
      round(medicine_exact[-1], 4), "mg")


# PART D: GRAPH
print("\nPART D: EULER METHOD GRAPH")

plt.figure(figsize=(9, 5))

plt.plot(
    times, numerical_values,
    marker="o", label="Euler approximation"
)

plt.plot(
    times, exact_values,
    linestyle="--", label="Exact solution"
)

plt.xlabel("Time")
plt.ylabel("Value of y")
plt.title("Euler Method: Numerical and Exact Solutions")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_17_Euler_Method/documentation/Task_17_Euler_Graph.png"
)

plt.show()