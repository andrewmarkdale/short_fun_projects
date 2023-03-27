import numpy as np
from time import perf_counter

def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        i += 1
    return arr

#def insertion_sort_fast(arr):
    

num = int(input("Enter the number of random numbers to sort: "))
random_list = np.random.randint(0, 1000, num)
time_start = perf_counter()
insertion_sort(random_list)
time_end = perf_counter()
print(f"With insertion sort it took {time_end-time_start} seconds to sort {num} items.")
        