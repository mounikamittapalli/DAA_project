import time
import matplotlib.pyplot as plt


# KMP algorithm implementation
def KMP_search(text, pattern):
    # Step 1: Preprocess the pattern to create the LPS (Longest Prefix Suffix) array
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m  # Initialize LPS array with 0s
        length = 0  # Length of the previous longest prefix suffix
        i = 1  # Start from the second character in the pattern

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # Use the previous longest prefix suffix
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # Step 2: Perform the pattern search using the LPS array
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern
    matches = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # Found a match
            matches.append(i - j)
            j = lps[j - 1]  # Use the LPS array to skip unnecessary comparisons

        elif i < n and pattern[j] != text[i]:  # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]  # Use the LPS array to shift the pattern
            else:
                i += 1

    return matches


# Function to execute the KMP algorithm and measure execution time
def benchmark_kmp(input_sizes, pattern, base_text):
    times = []

    for size in input_sizes:
        # Generate the input text by repeating the base text
        text = base_text * (size // len(base_text)) + base_text[:size % len(base_text)]

        # Measure the start time
        start_time = time.time()

        # Execute KMP search
        KMP_search(text, pattern)

        # Measure the end time
        end_time = time.time()

        # Record the execution time
        times.append(end_time - start_time)

    return times


# Benchmark setup
input_sizes = [1000, 5000, 10000, 50000, 100000,500000]  # Different text sizes
pattern = "search"  # Pattern to search
base_text = "searching for the right phrase to match and testing for repeated words like search"  # Base text
print(input_sizes)

# Execute benchmark
execution_times = benchmark_kmp(input_sizes, pattern, base_text)
print(execution_times)

# Plot the execution time vs. input size
plt.figure(figsize=(10, 4))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b')
plt.title("KMP Algorithm: Execution Time vs. Input Size")
plt.xlabel("Input Size (Text Length)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.show()
