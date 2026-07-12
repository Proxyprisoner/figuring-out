#run in terminal: python "vishal/leet/9.py"
def isPalindrome(x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
x= int(input("Enter a number: "))
print(isPalindrome(x))