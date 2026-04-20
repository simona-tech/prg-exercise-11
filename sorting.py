import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values_original):
    values = values_original.copy()
    for min_index in range(len(values)):
        min_value = values[min_index]
        min_ind = min_index
        for i in range(min_index, len(values)):
            if values[i] < min_value:
                min_ind = i
                min_value = values[i]
        values[min_ind], values[min_index] = values[min_index], values[min_ind]
    return values

def bubble_sort(values_original):
    values = values_original.copy()
    plt.ion()
    plt.show()
    for x in range(len(values)-1):
        for i in range(len(values)-1-x):
            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if values[i] > values[i+1]:
                values[i], values[i+1] = values[i+1], values[i]
    plt.ioff()
    plt.show()
    return values

def main():
    val_ori = random_numbers(20)
    return selection_sort(val_ori)

if __name__ == "__main__":
    print(bubble_sort(random_numbers(20)))