# ==================================================
# TASK 11: NEWTON-RAPHSON AND SECANT METHODS
# ==================================================

# Function: f(x) = x^3 - x - 2

def f(x):
    return x**3 - x - 2


# Derivative of the function
def df(x):
    return 3*x**2 - 1


# ==================================================
# PART A: NEWTON-RAPHSON METHOD
# ==================================================

print("PART A: NEWTON-RAPHSON METHOD")


def newton_raphson(initial_guess, tolerance=1e-6, max_iterations=100):

    x = initial_guess

    for iteration in range(1, max_iterations + 1):

        if df(x) == 0:
            raise ValueError("Derivative is zero. Cannot continue.")

        new_x = x - f(x) / df(x)

        if abs(new_x - x) < tolerance:
            return new_x, iteration

        x = new_x

    return x, max_iterations


root_newton, iterations_newton = newton_raphson(1.5)

print("Function: f(x) = x^3 - x - 2")
print("Initial guess:", 1.5)
print("Approximate root:", root_newton)
print("Function value at root:", f(root_newton))
print("Number of iterations:", iterations_newton)


# ==================================================
# PART B: SECANT METHOD
# ==================================================

print("\nPART B: SECANT METHOD")


def secant(x0, x1, tolerance=1e-6, max_iterations=100):

    for iteration in range(1, max_iterations + 1):

        denominator = f(x1) - f(x0)

        if denominator == 0:
            raise ValueError("Division by zero in secant method.")

        new_x = x1 - f(x1) * (x1 - x0) / denominator

        if abs(new_x - x1) < tolerance:
            return new_x, iteration

        x0 = x1
        x1 = new_x

    return x1, max_iterations


root_secant, iterations_secant = secant(1, 2)

print("Initial guesses:", 1, "and", 2)
print("Approximate root:", root_secant)
print("Function value at root:", f(root_secant))
print("Number of iterations:", iterations_secant)


# ==================================================
# PART C: CHANGING AN INPUT VALUE
# ==================================================

print("\nPART C: CHANGED INITIAL GUESS")

changed_root, changed_iterations = newton_raphson(2.0)

print("New initial guess:", 2.0)
print("Approximate root:", changed_root)
print("Function value at root:", f(changed_root))
print("Number of iterations:", changed_iterations)


# ==================================================
# PART D: REAL-WORLD APPLICATION
# CALCULATING THE SIDE LENGTH OF A CUBE
# ==================================================

print("\nPART D: CUBE VOLUME APPLICATION")

# A cube-shaped storage container must hold 27 cubic metres.
# Volume = side^3
# Therefore: side^3 - 27 = 0

def cube_volume_equation(side):
    return side**3 - 27


def cube_derivative(side):
    return 3 * side**2


# Apply Newton-Raphson to the volume equation
side = 4.0

for iteration in range(1, 101):

    new_side = side - cube_volume_equation(side) / cube_derivative(side)

    if abs(new_side - side) < 1e-6:
        side = new_side
        break

    side = new_side


print("Required volume: 27 cubic metres")
print("Calculated side length:", side, "metres")
print("Verified volume:", side**3, "cubic metres")
print("Number of iterations:", iteration)


print("\nTask 11 completed successfully.")