#Run in terminal: python "vishal/leet/136.py"
def singleNumber(nums):
        result = 0

        for num in nums:
            result ^= num

        return result
arr=[4, 1, 2, 1, 2]
print(singleNumber(arr))