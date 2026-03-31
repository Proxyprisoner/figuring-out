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

# Test
arr = [5, 3, 8, 4, 2]
bubble_sort(arr)

print("\nFinal Sorted Array:", arr)