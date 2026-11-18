import numpy as np

# ============================================================
# TASK 2: NUMPY ARRAYS AND NUMERICAL COMPUTATION
# ============================================================

# PART A: Original example - hourly weather station readings
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Convert every Celsius reading to Fahrenheit using NumPy
temperatures_f = 1.8 * temperatures_c + 32

print("PART A: ORIGINAL WEATHER STATION RESULTS")
print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))

# PART B: Change one input value and compare the result.
# The 13th reading is changed from 29.4 C to 34.4 C.
changed_temperatures_c = temperatures_c.copy()
changed_temperatures_c[12] = 34.4

changed_mean = np.mean(changed_temperatures_c)
changed_min = np.min(changed_temperatures_c)
changed_max = np.max(changed_temperatures_c)

print("\nPART B: RESULTS AFTER CHANGING ONE INPUT")
print(f"New daily mean temperature: {changed_mean:.2f} C")
print(f"New minimum temperature: {changed_min:.2f} C")
print(f"New maximum temperature: {changed_max:.2f} C")
print(f"Change in daily mean: {changed_mean - mean_temp:.2f} C")
print(f"Change in maximum: {changed_max - max_temp:.2f} C")

# PART C: Modified related real-world case - greenhouse monitoring.
# A greenhouse records temperatures during 8 monitoring periods.
greenhouse_c = np.array([21.0, 22.5, 24.0, 26.5, 28.0, 27.0, 25.0, 23.5])

greenhouse_mean = np.mean(greenhouse_c)
greenhouse_min = np.min(greenhouse_c)
greenhouse_max = np.max(greenhouse_c)
greenhouse_f = 1.8 * greenhouse_c + 32

print("\nPART C: GREENHOUSE TEMPERATURE MONITORING")
print(f"Average greenhouse temperature: {greenhouse_mean:.2f} C")
print(f"Lowest greenhouse temperature: {greenhouse_min:.2f} C")
print(f"Highest greenhouse temperature: {greenhouse_max:.2f} C")
print("Temperatures in Fahrenheit:", np.round(greenhouse_f, 2))

if greenhouse_max > 30:
    print("Interpretation: The greenhouse may be getting too hot and needs ventilation.")
else:
    print("Interpretation: The recorded greenhouse temperatures are within the selected 30 C limit.")
