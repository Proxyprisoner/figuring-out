#run in terminal: python "vishal/leet/9.py"
def isPalindrome(x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
x = 121
print(isPalindrome(x))
