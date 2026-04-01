def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        print(f"\nPass {i+1}:")

        for j in range(n - i - 1):
            print(f"  Compare {arr[j]} and {arr[j+1]}", end=" ")

            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("→ swap", arr)
            else:
                print("→ no swap", arr)

        print("Result after pass:", arr)

n = input("Input the unsorted array: ")
n = n.strip("[]")
n = list(map(int, n.split(",")))
bubble_sort(n)