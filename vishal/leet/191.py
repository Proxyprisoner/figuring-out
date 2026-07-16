def hammingWeight(n):
    count = 0
    while n != 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count

n = int(input("Enter a decimal number: "))

print("Binary:", bin(n)[2:])
print("Number of 1s:", hammingWeight(n))