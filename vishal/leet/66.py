#run in terminal: python "vishal/leet/66.py"
def plusOne(digits):
        num = 0

        for digit in digits:
            num = num * 10 + digit

        num += 1

        digits = list(map(int, str(num)))

        return digits
digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]