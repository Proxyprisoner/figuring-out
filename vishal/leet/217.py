#Run in terminal: python "vishal/leet/217.py"
def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
def containsDuplicate2(self, nums):
        
        temp = set(nums)
        if len(temp) != len(nums):
            return True 
        return False       
    
def containsDuplicate3(self, nums):
        dup=[]
        org=[]
        seen=[]
        for i in nums:
            if i not in dup:
                dup.append(i)
            else:
                seen.append(i)
        if seen:
            return True
        else:
            return False
arr=[1,2,3,4,5,6,7,8,9,10]
print(containsDuplicate(arr))   
print(containsDuplicate2(arr))
print(containsDuplicate3(arr))   