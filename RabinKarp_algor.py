import time
import matplotlib.pyplot as plt


# Rabin-Karp algorithm implementation
def rabin_karp(text, pattern):
    # Prime number for the hash function
    prime = 101
    m = len(pattern)
    n = len(text)

    # Calculate the hash value of the pattern and the first window of the text
    def hash_value(s, length):
        h = 0
        for i in range(length):
            h += ord(s[i]) * (prime ** (length - i - 1))
        return h

    pattern_hash = hash_value(pattern, m)
    text_hash = hash_value(text, m)

    # List to store the starting indices of the matches
    matches = []

    # Rolling hash algorithm to compare the pattern with substrings in the text
    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            matches.append(i)

        # Update the hash value for the next window of text
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * (prime ** (m - 1))) * prime + ord(text[i + m])

    return matches


# Function to execute the Rabin-Karp algorithm and measure execution time
def benchmark_rabin_karp(input_sizes, pattern, base_text):
    times = []

    for size in input_sizes:
        # Generate the input text by repeating the base text
        text = base_text * (size // len(base_text)) + base_text[:size % len(base_text)]

        # Measure the start time
        start_time = time.time()

        # Execute Rabin-Karp search
        rabin_karp(text, pattern)

        # Measure the end time
        end_time = time.time()

        # Record the execution time
        times.append(end_time - start_time)

    return times


# Benchmark setup
input_sizes = [1000, 5000, 10000, 50000, 100000, 500000]   # Different text sizes
pattern = "test"  # Pattern to search
base_text = "This is a test string used to evaluate the efficiency of the Rabin-Karp string search algorithm."
print(input_sizes)
# Base text

# Execute benchmark
execution_times_rk = benchmark_rabin_karp(input_sizes, pattern, base_text)
print(execution_times_rk)

# Plot the execution time vs. input size
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times_rk, marker='o', linestyle='-', color='r')
plt.title("Rabin-Karp Algorithm: Execution Time vs. Input Size")
plt.xlabel("Input Size (Text Length)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()
