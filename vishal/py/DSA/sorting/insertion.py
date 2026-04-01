n = input("Input the unsorted array: ")
n = n.strip("[]")
n = list(map(int, n.split(",")))

def insertion_sort(arr):
    print("Initial array:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nStep {i}: insert {key} into sorted left side {arr[:i]}")

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"  shift: {arr} (j={j})")

        arr[j + 1] = key
        print(f"  placed {key} ->", arr)

    return arr

sorted_arr = insertion_sort(n)
print("\nSorted array:", sorted_arr)
