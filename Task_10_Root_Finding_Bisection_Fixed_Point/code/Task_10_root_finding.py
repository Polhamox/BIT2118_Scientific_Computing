# ==================================================
# TASK 10: ROOT FINDING METHODS
# BISECTION AND FIXED-POINT METHODS
# ==================================================

# General bisection function

def bisection(func, a, b, tolerance=1e-6, max_iterations=100):

    if func(a) * func(b) >= 0:
        raise ValueError("The interval must contain a sign change.")

    for iteration in range(1, max_iterations + 1):

        midpoint = (a + b) / 2

        if abs(func(midpoint)) < tolerance or (b - a) / 2 < tolerance:
            return midpoint, iteration

        if func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return midpoint, max_iterations


# ==================================================
# PART A: BISECTION METHOD
# ==================================================

print("PART A: BISECTION METHOD")

def f(x):
    return x**3 - x - 2


root, iterations = bisection(f, 1, 2)

print("Function: f(x) = x^3 - x - 2")
print("Initial interval: [1, 2]")
print("Approximate root:", root)
print("Function value at root:", f(root))
print("Number of iterations:", iterations)


# ==================================================
# PART B: CHANGING THE INPUT INTERVAL
# ==================================================

print("\nPART B: CHANGED INPUT INTERVAL")

new_root, new_iterations = bisection(f, 1.5, 2)

print("New interval: [1.5, 2]")
print("Approximate root:", new_root)
print("Function value at root:", f(new_root))
print("Number of iterations:", new_iterations)


# ==================================================
# PART C: FIXED-POINT METHOD
# ==================================================

print("\nPART C: FIXED-POINT METHOD")

def g(x):
    return (x + 2)**(1/3)


def fixed_point(initial_guess, tolerance=1e-6, max_iterations=100):

    x = initial_guess

    for iteration in range(1, max_iterations + 1):

        new_x = g(x)

        if abs(new_x - x) < tolerance:
            return new_x, iteration

        x = new_x

    return x, max_iterations


fixed_root, fixed_iterations = fixed_point(1.5)

print("Iteration formula: x = (x + 2)^(1/3)")
print("Initial guess:", 1.5)
print("Approximate root:", fixed_root)
print("Function value at root:", f(fixed_root))
print("Number of iterations:", fixed_iterations)


# ==================================================
# PART D: WATER TANK APPLICATION
# ==================================================

print("\nPART D: WATER TANK APPLICATION")

# A cube-shaped tank must hold 1000 litres.
# 1000 litres = 1 cubic metre.
# Volume of a cube = side^3.

def volume_equation(side):
    return side**3 - 1


tank_side, tank_iterations = bisection(volume_equation, 0, 2)

print("Required tank volume: 1 cubic metre")
print("Calculated side length:", tank_side, "metres")
print("Verified volume:", tank_side**3, "cubic metres")
print("Number of iterations:", tank_iterations)


print("\nTask 10 completed successfully.")