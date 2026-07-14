#run in terminal: python "vishal/leet/35.py"
def searchInsert(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

# Example usage:
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Output: 2