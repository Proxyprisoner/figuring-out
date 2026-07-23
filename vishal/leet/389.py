#run in terminal: python "vishal/leet/389.py"
def findTheDifference(s,t):
        res = 0
        
        # XOR all characters in s and t
        for char in s + t:
            res ^= ord(char)
        
        # Convert the XOR result back to character
        return chr(res)
s="abcd"
t="abcde"   
print(findTheDifference(s,t))