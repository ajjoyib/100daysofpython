import random
import statistics

def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

def sort_list(numbers):
    return sorted(numbers)

def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = statistics.stdev(numbers)
    return mean, median, stdev

def main(): 
    list_size = 10

    random_numbers = generate_random_list(list_size)
    print("\n\nOriginal list:", random_numbers)

    sorted_numbers = sort_list(random_numbers)
    print("Sorted list:", sorted_numbers)

    mean, median, stdev = calculate_statistics(sorted_numbers)
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {stdev}\n\n")

if __name__ == "__main__":
    main()
