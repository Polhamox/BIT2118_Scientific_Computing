import numpy as np
import timeit

# =====================================================
# PART A: ORIGINAL NETWORK MONITORING PROBLEM
# =====================================================

# Generate one million network latency readings
rng = np.random.default_rng(42)

latency_ms = rng.uniform(5, 250, 1_000_000)


# Method 1: Using an ordinary Python loop
def loop_version(data):
    squared = []

    for value in data:
        seconds = value / 1000.0
        squared.append(seconds ** 2)

    return squared


# Method 2: Using NumPy vectorization
def vectorized_version(data):
    seconds = data / 1000.0
    return seconds ** 2


# Measure execution time
loop_time = timeit.timeit(
    lambda: loop_version(latency_ms),
    number=1
)

vector_time = timeit.timeit(
    lambda: vectorized_version(latency_ms),
    number=3
) / 3

result = vectorized_version(latency_ms)


print("PART A: ORIGINAL NETWORK MONITORING RESULTS")

print("Number of latency readings:", len(latency_ms))
print("First five squared latency values:", result[:5])

print(f"Loop execution time: {loop_time:.4f} seconds")
print(f"Vectorized execution time: {vector_time:.4f} seconds")

print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")


# =====================================================
# PART B: CHANGE ONE INPUT
# =====================================================

# Reduce measurements from 1 million to 500,000

changed_rng = np.random.default_rng(42)

changed_latency_ms = changed_rng.uniform(5, 250, 500_000)

changed_result = vectorized_version(changed_latency_ms)


print("\nPART B: RESULTS AFTER CHANGING THE INPUT")

print("New number of readings:", len(changed_latency_ms))
print("First five squared latency values:", changed_result[:5])

print("The program now processes half as many measurements.")


# =====================================================
# PART C: MATHEMATICAL FUNCTIONS
# =====================================================

# Demonstrate the identity:
# sin²(x) + cos²(x) = 1

x = np.array([0, np.pi / 2, np.pi])

sine_values = np.sin(x)
cosine_values = np.cos(x)

identity_result = sine_values**2 + cosine_values**2


print("\nPART C: MATHEMATICAL FUNCTIONS")

print("Input values:", x)
print("Sine values:", sine_values)
print("Cosine values:", cosine_values)
print("sin²(x) + cos²(x):", identity_result)


# =====================================================
# PART D: MODIFIED REAL-WORLD APPLICATION
# AUDIO SIGNAL PROCESSING
# =====================================================

audio_signal = np.array([
    -0.9, -0.6, -0.2, 0.0, 0.3, 0.7, 0.95
])

# Reduce signal amplitude by half
normalized_signal = audio_signal * 0.5

# Square all signal values
squared_signal = normalized_signal ** 2


print("\nPART D: AUDIO SIGNAL PROCESSING")

print("Original audio signal:", audio_signal)
print("Scaled audio signal:", normalized_signal)
print("Squared signal values:", squared_signal)

print("\nINTERPRETATION:")

print("NumPy processed all audio samples using vectorized operations.")
print("This avoids writing a separate loop for every sample.")