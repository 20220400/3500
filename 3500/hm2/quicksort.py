import random
import time
import sys

# Set recursion limit to 1 million 
sys.setrecursionlimit(10**6)

# Quicksort function with last element as pivot
def quicksort_last_pivot(arr, low, high):
    if low < high:
        # Choose the last element as pivot
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        # Recursively sort elements before and after partition
        quicksort_last_pivot(arr, low, pi - 1)
        quicksort_last_pivot(arr, pi + 1, high)

# Quicksort function with random element as pivot
def quicksort_random_pivot(arr, low, high):
    if low < high:
        # Choose a random element as pivot
        rand_pivot_idx = random.randint(low, high)
        arr[high], arr[rand_pivot_idx] = arr[rand_pivot_idx], arr[high]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        # Recursively sort elements before and after partition
        quicksort_random_pivot(arr, low, pi - 1)
        quicksort_random_pivot(arr, pi + 1, high)

# Test Quicksort
def test_quicksort(arr):
    arr_copy = arr.copy()

    # Measure time taken for Quicksort with last element as pivot
    start_time = time.time()
    quicksort_last_pivot(arr_copy, 0, len(arr_copy) - 1)
    last_pivot_time = time.time() - start_time

    arr_copy = arr.copy()

    # Measure time taken for Quicksort with random element as pivot
    start_time = time.time()
    quicksort_random_pivot(arr_copy, 0, len(arr_copy) - 1)
    random_pivot_time = time.time() - start_time

    return last_pivot_time, random_pivot_time

# Test on different input types and sizes
input_sizes = [100, 500, 1000, 1500, 2000]
input_types = {
    'Sorted list': lambda n: list(range(n)),
    'Reverse sorted list': lambda n: list(range(n, 0, -1)),
    'Random list': lambda n: random.sample(range(n), n)
}

print("Input size\tInput type\tLast pivot time (seconds)\tRandom pivot time (seconds)")

for input_size in input_sizes:
    for input_type, input_generator in input_types.items():
        arr = input_generator(input_size)
        last_pivot_time, random_pivot_time = test_quicksort(arr)
        # Print results in TSV format
        print(f"{input_size}\t{input_type}\t{last_pivot_time:.6f}\t{random_pivot_time:.6f}")
