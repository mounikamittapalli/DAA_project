# compare_algorithms.py

import matplotlib.pyplot as plt
from KnuthMorrisPratt_algo import benchmark_kmp
from RabinKarp_algor import benchmark_rabin_karp

# Benchmark setup
input_sizes = [1000, 5000, 10000, 50000, 100000, 500000]  # Different text sizes
pattern_kmp = "search"  # Pattern for KMP
pattern_rk = "test"  # Pattern for Rabin-Karp
base_text_kmp = "searching for the right phrase to match and testing for repeated words like search"  # Base text for KMP
base_text_rk = "This is a test string used to evaluate the efficiency of the Rabin-Karp string search algorithm."  # Base text for Rabin-Karp

# Execute benchmark for KMP
execution_times_kmp = benchmark_kmp(input_sizes, pattern_kmp, base_text_kmp)
print(f"KMP Execution Times: {execution_times_kmp}")

# Execute benchmark for Rabin-Karp
execution_times_rk = benchmark_rabin_karp(input_sizes, pattern_rk, base_text_rk)
print(f"Rabin-Karp Execution Times: {execution_times_rk}")

# Plot the execution time vs. input size for KMP and Rabin-Karp
plt.figure(figsize=(10, 6))

# Plotting KMP results
plt.plot(input_sizes, execution_times_kmp, marker='o', linestyle='-', color='b', label='KMP Algorithm')

# Plotting Rabin-Karp results
plt.plot(input_sizes, execution_times_rk, marker='x', linestyle='-', color='r', label='Rabin-Karp Algorithm')

# Adding titles and labels
plt.title("KMP vs Rabin-Karp: Execution Time vs. Input Size", fontsize=14)
plt.xlabel("Input Size (Text Length)", fontsize=12)
plt.ylabel("Execution Time (seconds)", fontsize=12)
plt.legend()
plt.grid(True)

# Display the graph
plt.show()

