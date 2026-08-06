#run in terminal: python "vishal/leet/26.py"
def removeDuplicates(nums):
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k
nums = [1, 1, 2]
print(removeDuplicates(nums))  # Output: 2
