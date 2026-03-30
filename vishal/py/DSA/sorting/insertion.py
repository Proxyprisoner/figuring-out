n = input("input the unsorted array: ")
n = n.strip("[]")
n = list(map(int, n.split(",")))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

print("Sorted array:", insertion_sort(n))
