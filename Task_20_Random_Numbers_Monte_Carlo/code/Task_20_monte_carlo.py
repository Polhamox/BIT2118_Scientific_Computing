import numpy as np
import matplotlib.pyplot as plt


# PART A: GENERATING RANDOM NUMBERS
print("PART A: GENERATING RANDOM NUMBERS")

np.random.seed(42)

random_numbers = np.random.random(10)

print("Generated random numbers:")
print(random_numbers)

print("Mean:", round(np.mean(random_numbers), 4))
print("Minimum:", round(np.min(random_numbers), 4))
print("Maximum:", round(np.max(random_numbers), 4))


# PART B: MONTE CARLO ESTIMATION OF PI
print("\nPART B: MONTE CARLO ESTIMATION OF PI")

number_of_points = 10000

x = np.random.uniform(-1, 1, number_of_points)
y = np.random.uniform(-1, 1, number_of_points)

# Check which points fall inside the unit circle
inside_circle = x**2 + y**2 <= 1

points_inside = np.sum(inside_circle)

# Estimate pi using the ratio of points
pi_estimate = 4 * points_inside / number_of_points

print("Total random points:", number_of_points)
print("Points inside circle:", points_inside)
print("Estimated value of pi:", round(pi_estimate, 6))
print("Actual value of pi:", round(np.pi, 6))
print("Absolute error:", round(abs(pi_estimate - np.pi), 6))


# PART C: CHANGE THE NUMBER OF RANDOM POINTS
print("\nPART C: CHANGED NUMBER OF RANDOM POINTS")

new_number_of_points = 100000

new_x = np.random.uniform(-1, 1, new_number_of_points)
new_y = np.random.uniform(-1, 1, new_number_of_points)

new_inside_circle = new_x**2 + new_y**2 <= 1

new_points_inside = np.sum(new_inside_circle)

new_pi_estimate = 4 * new_points_inside / new_number_of_points

print("New total random points:", new_number_of_points)
print("New points inside circle:", new_points_inside)
print("New estimated value of pi:", round(new_pi_estimate, 6))
print("Actual value of pi:", round(np.pi, 6))
print("New absolute error:", round(abs(new_pi_estimate - np.pi), 6))


# PART D: REAL-WORLD APPLICATION
print("\nPART D: MONTE CARLO PROJECT COST ESTIMATION")

# Simulate project costs with random variations.
# Minimum cost = 80000
# Maximum cost = 120000

np.random.seed(10)

simulations = 10000

project_costs = np.random.uniform(
    80000, 120000, simulations
)

average_cost = np.mean(project_costs)
minimum_cost = np.min(project_costs)
maximum_cost = np.max(project_costs)

probability_above_100000 = np.mean(
    project_costs > 100000
) * 100

print("Number of simulations:", simulations)
print("Average estimated project cost:",
      round(average_cost, 2))
print("Minimum simulated cost:", round(minimum_cost, 2))
print("Maximum simulated cost:", round(maximum_cost, 2))
print("Probability of cost exceeding 100000:",
      round(probability_above_100000, 2), "%")


# PART E: GRAPH
print("\nPART E: MONTE CARLO GRAPH")

plt.figure(figsize=(9, 5))

plt.scatter(
    x[~inside_circle],
    y[~inside_circle],
    s=5,
    label="Outside circle"
)

plt.scatter(
    x[inside_circle],
    y[inside_circle],
    s=5,
    label="Inside circle"
)

plt.xlabel("X coordinates")
plt.ylabel("Y coordinates")
plt.title("Monte Carlo Estimation of Pi")
plt.axis("equal")
plt.legend()
plt.grid(True)

plt.savefig(
    "Task_20_Random_Numbers_Monte_Carlo/documentation/Task_20_Monte_Carlo_Graph.png"
)

plt.show()