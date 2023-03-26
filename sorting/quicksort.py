import numpy as np
from time import perf_counter

def quicksort(list, low, high):
    if low >= high or low < 0:
        return 
    
    p = partition(list, low, high)
    
    quicksort(list, low, p-1)
    quicksort(list, p+1, high)
    return list
    
    
def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
            
    i += 1
    list[i], list[high] = list[high], list[i]
    return i

num = int(input("Enter the number of random numbers to sort: "))
random_list = np.random.randint(0, 1000, num)
time_start = perf_counter()
quicksort(random_list, 0, len(random_list)-1)
time_end = perf_counter()
print(f"With quicksort it took {time_end-time_start} seconds to sort {num} items.")