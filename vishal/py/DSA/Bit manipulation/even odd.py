"""
for all even numbers, the last bit is 0 and for odd numbers, 
the last bit is 1. So we can check if a number is even or odd 
by performing a bitwise AND operation with 1.1is represent as 0001 in binary. 
If the result is 0, the number is even; 
if the result is 1, the number is odd.
"""

a=input("Enter a number: ")
print("Binary representation of", a, "is:", bin(int(a)))
if int(a) & 1 == 0:
    print(a, "is even")       
else:    
    print(a, "is odd")