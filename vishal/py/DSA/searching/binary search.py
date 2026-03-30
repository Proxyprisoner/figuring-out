n = input("input the sorted array: ")
n = n.strip("[]")
n = list(map(int, n.split(",")))
target = int(input("input the target: "))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
result = binary_search(n, target)
if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found in the array.")    

