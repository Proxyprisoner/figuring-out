# Run in terminal: python "vishal/leet/744.py"
def nextGreatestLetter(letters, target):
        low, high = 0, len(letters) - 1
        ans = letters[0]   # default for wrap-around

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                ans = letters[mid]   
                high = mid - 1       
            else:
                low = mid + 1

        return ans
letter=["c", "f", "j"]
target="a"  
print(nextGreatestLetter(letter, target))  # Output: "c"