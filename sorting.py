import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def my_selection_sort(number_list):
    sorted_numbers = sorted(number_list)
    return sorted_numbers

def selection_sort(values_original):
    values = values_original.copy()
    for min_index in range(len(values)):
        print(values)
        min_value = values[min_index]
        min_ind = min_index
        for i in range(min_index, len(values)):
            if values[i] < min_value:
                min_ind = i
                min_value = values[i]
        values[min_ind], values[min_index] = values[min_index], values[min_ind]
    return values

def main():
    val_ori = random_numbers(20)
    return selection_sort(val_ori)

if __name__ == "__main__":
    print(main())