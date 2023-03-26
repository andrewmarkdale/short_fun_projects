from time import perf_counter

def collatz(number, steps=0):
    if number == 1:
        return steps
    elif number % 2 == 0:
        steps += 1
        return collatz(number/2, steps)
    else:
        steps += 1
        return collatz(number * 3 + 1, steps)
        
num_to_check = int(input("Please enter a number to check: "))
time_start = perf_counter()
print(f"The number of steps for {num_to_check} is {collatz(num_to_check)}")
time_end = perf_counter()

print(f"The time elapsed in seconds: {time_end-time_start}")