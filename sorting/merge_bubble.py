import random
from time import perf_counter


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
    return list

def merge_sort(list):
    if len(list) <= 1:
        return list
    
    left = []
    right = []
    for i in range(len(list)):
        if i < len(list)/2:
            left.append(list[i])
        else:
            right.append(list[i])
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    
    while len(left) != 0:
        result.append(left[0])
        left.remove(left[0])
    while len(right) != 0:
        result.append(right[0])
        right.remove(right[0])
    return result
    
num = int(input("Enter the number of random numbers to sort: "))
  
random_list = [random.randint(0, 1000) for x in range(0, num)]
time_start = perf_counter()
bubble_sort(random_list)
time_end = perf_counter()
print(f"With bubble sort it took {time_end-time_start} seconds to sort {num} items.")

random_list = [random.randint(0, 1000) for x in range(0, num)]
time_start = perf_counter()
merge_sort(random_list)
time_end = perf_counter()
print(f"With merge sort it took {time_end-time_start} seconds to sort {num} items.")
