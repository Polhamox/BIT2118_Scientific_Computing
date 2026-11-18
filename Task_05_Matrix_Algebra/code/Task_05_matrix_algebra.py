import numpy as np

# PART A: ORIGINAL COMPUTER GRAPHICS EXAMPLE

# Four corners of a square represented as coordinate points
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Rotation angle of 45 degrees
angle = np.deg2rad(45)

# Rotation matrix
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Scaling matrix
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combine rotation and scaling matrices
transformation = rotation @ scale

# Transform the original points
transformed_points = points @ transformation.T

print("PART A: ORIGINAL COMPUTER GRAPHICS RESULTS")
print("Original points:")
print(points)

print("\nRotation matrix:")
print(rotation)

print("\nScaling matrix:")
print(scale)

print("\nCombined transformation matrix:")
print(transformation)

print("\nTransformed points:")
print(transformed_points)

# Calculate determinant
determinant = np.linalg.det(transformation)

print("\nDeterminant:", determinant)


# PART B: CHANGE AN INPUT VALUE

# Change the rotation angle from 45 to 90 degrees
new_angle = np.deg2rad(90)

new_rotation = np.array([
    [np.cos(new_angle), -np.sin(new_angle)],
    [np.sin(new_angle), np.cos(new_angle)]
])

new_transformation = new_rotation @ scale

new_transformed_points = points @ new_transformation.T

print("\nPART B: RESULTS AFTER CHANGING THE ROTATION ANGLE")
print("New rotation angle: 90 degrees")

print("\nNew transformation matrix:")
print(new_transformation)

print("\nNew transformed points:")
print(new_transformed_points)


# PART C: MATRIX ADDITION AND MULTIPLICATION

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("\nPART C: MATRIX OPERATIONS")

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix addition
addition = A + B

# Matrix multiplication
multiplication = A @ B

print("\nMatrix Addition (A + B):")
print(addition)

print("\nMatrix Multiplication (A @ B):")
print(multiplication)


# PART D: MODIFIED REAL-WORLD APPLICATION
# Scaling classroom floor coordinates for a digital floor plan

classroom_points = np.array([
    [0, 0],
    [4, 0],
    [4, 3],
    [0, 3]
])

# Scale the classroom coordinates by a factor of 2
scaling_matrix = np.array([
    [2, 0],
    [0, 2]
])

scaled_classroom = classroom_points @ scaling_matrix.T

print("\nPART D: CLASSROOM FLOOR PLAN APPLICATION")

print("Original classroom coordinates:")
print(classroom_points)

print("\nScaling matrix:")
print(scaling_matrix)

print("\nScaled classroom coordinates:")
print(scaled_classroom)

print("\nINTERPRETATION:")
print("Matrix operations can rotate and resize objects.")
print("Changing the rotation angle changes the position of the points.")
print("Scaling changes the size of the represented object.")
print("These operations are useful in computer graphics and digital floor plans.")