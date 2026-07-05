def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result
arr=[4, 1, 2, 1, 2]
print(singleNumber(arr))