#run in terminal: python "vishal/py/deficient numbers.py"
def is_deficient(n):
    if n == 1:
        return True

    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1

    return s < n

# Example
for i in range(1, 21):
    if is_deficient(i):
        print(i, end=" ")