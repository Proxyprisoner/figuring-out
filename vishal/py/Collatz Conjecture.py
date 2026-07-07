#Run in terminal: python "vishal/py/Collatz Conjecture.py"
# Collatz Conjecture (Recursive)

def collatz(n, steps=0):
    if n == 1:
        print(1)
        return steps

    print(n, end=" → ")

    if n % 2 == 0:
        return collatz(n // 2, steps + 1)
    else:
        return collatz(3 * n + 1, steps + 1)


num = int(input("Enter a number: "))

if num > 0:
    total = collatz(num)
    print("Total steps:", total)
else:
    print("Enter a positive number.")