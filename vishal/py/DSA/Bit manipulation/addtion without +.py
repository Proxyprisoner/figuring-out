a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
i = 1

while b != 0:
    print("Step :", i, "\n")
    carry = a & b
    print("carry:", carry)

    a = a ^ b
    print("sum without carry:", a)

    b = carry << 1
    print("shifted carry:", b)
    print()
    i += 1

print("sum is:", a)
