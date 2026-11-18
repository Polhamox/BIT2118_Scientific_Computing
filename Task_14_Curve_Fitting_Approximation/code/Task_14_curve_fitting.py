import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART A: ORIGINAL CURVE FITTING
# ==========================================

print("PART A: ORIGINAL CURVE FITTING")

# Sample data representing monthly sales
months = np.array([1, 2, 3, 4, 5, 6], dtype=float)
sales = np.array([20, 25, 32, 40, 50, 62], dtype=float)

# Fit a second-degree polynomial
coefficients = np.polyfit(months, sales, 2)
polynomial = np.poly1d(coefficients)

# Estimate sales using the fitted curve
predicted_sales = polynomial(months)

print("Original sales:", sales)
print("Polynomial equation:")
print(polynomial)

# Calculate R-squared
ss_res = np.sum((sales - predicted_sales) ** 2)
ss_tot = np.sum((sales - np.mean(sales)) ** 2)

r_squared = 1 - (ss_res / ss_tot)

print("R-squared:", round(r_squared, 4))


# ==========================================
# PART B: CHANGE ONE INPUT VALUE
# ==========================================

print("\nPART B: CHANGED INPUT VALUE")

# Change sales for month 4 from 40 to 48
changed_sales = sales.copy()
changed_sales[3] = 48

changed_coefficients = np.polyfit(months, changed_sales, 2)
changed_polynomial = np.poly1d(changed_coefficients)

changed_predictions = changed_polynomial(months)

print("Changed sales:", changed_sales)
print("New polynomial equation:")
print(changed_polynomial)

print("Original prediction for month 4:", round(polynomial(4), 2))
print("New prediction for month 4:", round(changed_polynomial(4), 2))


# ==========================================
# PART C: MODIFIED REAL-WORLD APPLICATION
# ==========================================

print("\nPART C: REAL-WORLD APPLICATION")

# Monthly electricity consumption in a small business
months_business = np.array([1, 2, 3, 4, 5, 6], dtype=float)

electricity_units = np.array([120, 135, 155, 180, 210, 245], dtype=float)

# Fit a quadratic curve
business_coefficients = np.polyfit(
    months_business, electricity_units, 2
)

business_polynomial = np.poly1d(business_coefficients)

# Predict consumption for month 7
month_to_predict = 7
predicted_consumption = business_polynomial(month_to_predict)

print("Recorded electricity consumption:", electricity_units)
print(
    "Predicted consumption for month 7:",
    round(predicted_consumption, 2),
    "units"
)


# ==========================================
# PART D: CURVE FITTING GRAPH
# ==========================================

print("\nPART D: CURVE FITTING GRAPH")

# Generate smooth x-values for plotting
smooth_months = np.linspace(1, 7, 100)

plt.figure(figsize=(10, 6))

# Original data and fitted curve
plt.scatter(months, sales, label="Original sales data")
plt.plot(
    smooth_months,
    polynomial(smooth_months),
    label="Original fitted curve"
)

# Modified data and fitted curve
plt.scatter(
    months,
    changed_sales,
    marker="x",
    label="Changed sales data"
)

plt.plot(
    smooth_months,
    changed_polynomial(smooth_months),
    linestyle="--",
    label="Changed fitted curve"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Polynomial Curve Fitting and Approximation")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_14_Curve_Fitting_Approximation/documentation/"
    "Task_14_Curve_Fitting_Graph.png"
)

plt.show()

print("Graph saved successfully.")