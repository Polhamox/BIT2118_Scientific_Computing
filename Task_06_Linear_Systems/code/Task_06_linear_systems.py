import numpy as np

# PART A: ORIGINAL EXAMPLE
# Solve two simultaneous equations:
# 2x + 3y = 8
# 4x + y = 6

A = np.array([
    [2, 3],
    [4, 1]
])

b = np.array([8, 6])

solution = np.linalg.solve(A, b)

print("PART A: ORIGINAL LINEAR EQUATIONS")
print("Coefficient matrix:")
print(A)

print("\nConstant values:")
print(b)

print("\nSolution:")
print("x =", solution[0])
print("y =", solution[1])

print("\nVerification:")
print("A @ solution =", A @ solution)


# PART B: CHANGE AN INPUT VALUE
# Change the first equation from 2x + 3y = 8
# to 2x + 3y = 10

new_b = np.array([10, 6])

new_solution = np.linalg.solve(A, new_b)

print("\nPART B: RESULTS AFTER CHANGING AN INPUT")
print("New constant values:", new_b)

print("New solution:")
print("x =", new_solution[0])
print("y =", new_solution[1])

print("Verification:", A @ new_solution)


# PART C: MODIFIED REAL-WORLD APPLICATION
# Determine the number of two types of servers
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total CPU usage = 20 units
# Total memory usage = 72 GB

server_matrix = np.array([
    [4, 2],
    [8, 12]
])

resource_totals = np.array([20, 72])

server_solution = np.linalg.solve(
    server_matrix,
    resource_totals
)

print("\nPART C: SERVER RESOURCE ALLOCATION")

print("Resource coefficient matrix:")
print(server_matrix)

print("\nTotal resources:")
print(resource_totals)

print("\nCalculated number of servers:")
print("Type A servers:", server_solution[0])
print("Type B servers:", server_solution[1])

print("\nVerification:")
print("Calculated resource usage:", server_matrix @ server_solution)

print("\nResidual:")
print(resource_totals - server_matrix @ server_solution)

print("\nINTERPRETATION:")
print("Linear equations can be used to determine unknown quantities.")
print("Changing an input value changes the calculated solution.")
print("The server example demonstrates how equations can help")
print("allocate and analyse computing resources.")