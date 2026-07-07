#Run in terminal: python "vishal/leet/67.py"
def addBinary(a, b):  
    x = int(a,2)
    y = int(b,2)

    while y:
        carry = (x & y) << 1
        x = x ^ y
        y = carry

    return bin(x)[2:]
num="11"
num2="1"
print(addBinary(num,num2))