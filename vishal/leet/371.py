# Run in terminal: python "vishal/leet/371.py"
def getSum(a, b):
        while b:
            carry=(a&b)<<1
            a=(a^b)& 0xffffffff
            b=carry& 0xffffffff
        return a if a <=  0x7fffffff else ~(a ^  0xffffffff)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
print(getSum(a,b))