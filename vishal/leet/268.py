#run in terminal: python "vishal/leet/268.py"
def missingNumber(nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
numb=[3,0,1]
print(missingNumber(numb))