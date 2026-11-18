import numpy as np

# PART A: FLOATING-POINT COMPARISON
calculated = 0.1 + 0.2
expected = 0.3

print("PART A: FLOATING-POINT COMPARISON")
print("0.1 + 0.2 =", calculated)
print("Expected value:", expected)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))


# PART B: ABSOLUTE AND RELATIVE ERROR
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nPART B: ABSOLUTE AND RELATIVE ERROR")
print(f"True value: {true_value:.8f}")
print(f"Approximate value: {approx_value:.8f}")
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")


# PART C: CHANGE THE APPROXIMATE VALUE
new_approx_value = 1.4142

new_absolute_error = abs(true_value - new_approx_value)
new_relative_error = new_absolute_error / abs(true_value)

print("\nPART C: RESULTS AFTER CHANGING THE INPUT")
print("New approximate value:", new_approx_value)
print(f"New absolute error: {new_absolute_error:.8f}")
print(f"New relative error: {new_relative_error:.8%}")
print(f"Reduction in absolute error: {absolute_error - new_absolute_error:.8f}")


# PART D: NUMERICAL STABILITY
print("\nPART D: NUMERICAL STABILITY")

for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)

    print(f"x = {x:.0e}")
    print(f"Direct formula: {direct:.12f}")
    print(f"Stable formula: {stable:.12f}")


# PART E: MODIFIED REAL-WORLD APPLICATION
# Banking interest calculation

initial_balance = 1000.00
monthly_interest_rate = 0.015
months = 12

balance = initial_balance

for month in range(months):
    balance = balance * (1 + monthly_interest_rate)

print("\nPART E: BANKING APPLICATION")
print("Initial balance:", initial_balance)
print("Monthly interest rate:", monthly_interest_rate * 100, "%")
print("Number of months:", months)
print(f"Final balance: {balance:.2f}")

amount1 = 0.1 + 0.2
amount2 = 0.3

print("\nBanking precision check:")
print("Calculated amount:", amount1)
print("Expected amount:", amount2)
print("Exact equality:", amount1 == amount2)
print("Tolerance-based equality:", np.isclose(amount1, amount2))


print("\nINTERPRETATION:")
print("Floating-point numbers can introduce small calculation errors.")
print("Tolerance-based comparisons help identify approximately equal values.")
print("More accurate approximations reduce numerical errors.")