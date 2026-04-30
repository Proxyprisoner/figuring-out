def karatsuba(x, y, space=""):
    print(space + f"{x}X{y}")

    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y))) // 2
    a, b = x // 10**m, x % 10**m
    c, d = y // 10**m, y % 10**m

    ac = karatsuba(a, c, space + "  ")
    bd = karatsuba(b, d, space + "  ")
    abcd = karatsuba(a + b, c + d, space + "  ")

    return ac * 10**(2*m) + (abcd - ac - bd) * 10**m + bd


# Run
result = karatsuba(1234, 5678)
print("Final Answer:", result)