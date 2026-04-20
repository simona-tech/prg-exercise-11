import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(number_list):
    sorted_numbers = sorted(number_list)
    return sorted_numbers

def main():
    return

if __name__ == "__main__":
    print(selection_sort([564, 456, 0, 15, 478]))