import numpy as np
from time import perf_counter


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
    return list

num = int(input("Enter the number of random numbers to sort: "))
random_list = np.random.randint(0, 1000, num)
time_start = perf_counter()
bubble_sort(random_list)
time_end = perf_counter()
print(f"With bubble sort it took {time_end-time_start} seconds to sort {num} items.")