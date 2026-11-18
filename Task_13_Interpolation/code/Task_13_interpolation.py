import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# ==================================================
# PART A: ORIGINAL INTERPOLATION
# ==================================================

print("PART A: ORIGINAL INTERPOLATION")

# Recorded temperature readings at different hours.

hours = np.array([0, 2, 4, 6, 8], dtype=float)

temperatures = np.array([10, 15, 20, 18, 25], dtype=float)

print("Recorded hours:", hours)
print("Recorded temperatures:", temperatures)

# Estimate temperature at hour 5.

linear_function = interp1d(hours, temperatures, kind="linear")

linear_result = linear_function(5)

print("\nLinear interpolation at hour 5:", float(linear_result))

# Cubic spline interpolation.

cubic_function = CubicSpline(hours, temperatures)

cubic_result = cubic_function(5)

print("Cubic spline interpolation at hour 5:", float(cubic_result))


# ==================================================
# PART B: CHANGING AN INPUT VALUE
# ==================================================

print("\nPART B: CHANGED INPUT VALUE")

# Change the temperature at hour 6 from 18 to 22.

changed_temperatures = np.array([10, 15, 20, 22, 25], dtype=float)

changed_function = interp1d(
    hours,
    changed_temperatures,
    kind="linear"
)

changed_result = changed_function(5)

print("Changed temperatures:", changed_temperatures)
print("New interpolated temperature at hour 5:", float(changed_result))

print("Original interpolated temperature:", float(linear_result))


# ==================================================
# PART C: REAL-WORLD APPLICATION
# ESTIMATING MISSING RAINFALL DATA
# ==================================================

print("\nPART C: RAINFALL DATA APPLICATION")

# Rainfall measurements recorded over five days.
# Rainfall is measured in millimetres.

days = np.array([1, 2, 3, 4, 5], dtype=float)

rainfall = np.array([12, 18, 24, 30, 36], dtype=float)

# Estimate rainfall for day 2.5.

rainfall_function = interp1d(days, rainfall, kind="linear")

estimated_rainfall = rainfall_function(2.5)

print("Recorded days:", days)
print("Recorded rainfall:", rainfall)
print("Estimated rainfall on day 2.5:", float(estimated_rainfall), "mm")


# ==================================================
# PART D: INTERPOLATION GRAPH
# ==================================================

print("\nPART D: INTERPOLATION GRAPH")

# Generate additional points for smooth curves.

smooth_hours = np.linspace(0, 8, 100)

linear_curve = linear_function(smooth_hours)

cubic_curve = cubic_function(smooth_hours)

plt.figure(figsize=(9, 6))

plt.plot(
    hours,
    temperatures,
    "o",
    label="Original readings"
)

plt.plot(
    smooth_hours,
    linear_curve,
    label="Linear interpolation"
)

plt.plot(
    smooth_hours,
    cubic_curve,
    label="Cubic spline interpolation"
)

plt.scatter(
    5,
    linear_result,
    label="Estimated value at hour 5"
)

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (degrees Celsius)")
plt.title("Temperature Data Interpolation")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Task_13_Interpolation/documentation/Task_13_Interpolation_Graph.png"
)

plt.show()

print("Graph saved successfully.")

print("\nTask 13 completed successfully.")