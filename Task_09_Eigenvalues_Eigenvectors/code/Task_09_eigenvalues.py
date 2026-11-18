import numpy as np

# ==================================================
# PART A: CALCULATING EIGENVALUES AND EIGENVECTORS
# ==================================================

print("PART A: ORIGINAL MATRIX")

A = np.array([
    [4, 1],
    [1, 3]
], dtype=float)

print("Original matrix:")
print(A)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# ==================================================
# PART B: VERIFYING THE RESULTS
# ==================================================

print("\nPART B: VERIFICATION")

for i in range(len(eigenvalues)):
    value = eigenvalues[i]
    vector = eigenvectors[:, i]

    left_side = A @ vector
    right_side = value * vector

    print(f"\nEigenvalue {i + 1}: {value:.4f}")
    print("A multiplied by eigenvector:", left_side)
    print("Eigenvalue multiplied by eigenvector:", right_side)
    print("Verified:", np.allclose(left_side, right_side))


# ==================================================
# PART C: CHANGING AN INPUT VALUE
# ==================================================

print("\nPART C: CHANGED MATRIX")

changed_A = np.array([
    [5, 1],
    [1, 3]
], dtype=float)

changed_values, changed_vectors = np.linalg.eig(changed_A)

print("Changed matrix:")
print(changed_A)

print("\nNew eigenvalues:")
print(changed_values)

print("\nOriginal eigenvalues:")
print(eigenvalues)


# ==================================================
# PART D: REAL-WORLD APPLICATION
# SIMPLIFIED WEBSITE PAGE-RANKING MODEL
# ==================================================

print("\nPART D: WEBSITE RANKING MODEL")

# Transition probabilities between three websites.
# Each column represents the probability of moving
# from one website to another.

P = np.array([
    [0.7, 0.1, 0.2],
    [0.2, 0.7, 0.1],
    [0.1, 0.2, 0.7]
])

print("Website transition matrix:")
print(P)

# Calculate eigenvalues and eigenvectors
page_values, page_vectors = np.linalg.eig(P)

# Find the eigenvector corresponding to eigenvalue 1
index = np.argmin(np.abs(page_values - 1))

ranking_vector = np.real(page_vectors[:, index])

# Normalize the values so they add up to 1
ranking_vector = ranking_vector / np.sum(ranking_vector)

print("\nWebsite ranking scores:")

websites = ["Website A", "Website B", "Website C"]

for website, score in zip(websites, ranking_vector):
    print(f"{website}: {score:.4f} ({score * 100:.2f}%)")

print("\nTotal ranking score:", np.sum(ranking_vector))

print("\nTask 9 completed successfully.")