#run in terminal: python "vishal/leet/1394.py"
def findLucky(arr):
    from collections import Counter
    freq = Counter(arr)
    lucky = -1
    for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)


    return lucky
    
def findLucky(arr):
        count = {}

        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        lucky = -1

        for num in count:
            if num == count[num] and num > lucky:
                lucky = num

        return lucky
arr=[2,2,3,4]
arr2=[2,3,4]
print(findLucky(arr))   
print(findLucky(arr2))