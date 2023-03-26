from time import perf_counter

def collatz(number):
    highest, steps = 0, 0
    while number != 1:
        if number > highest: highest = number
        if number % 2 == 0:
            steps += 1
            number = number / 2
        else:
            steps += 1
            number = 3 * number + 1
    return steps, highest
if __name__ == "__main__":
    num_to_check = int(input("Enter a number to check: "))
    
    time_start = perf_counter()
    steps, highest = collatz(num_to_check)
    time_end = perf_counter()
    
    print(f"The number of steps for {num_to_check} is {steps}")
    print(f"Highest number achieved: {round(highest, 0)}")
    print(f"The time elapsed in seconds: {time_end - time_start}")