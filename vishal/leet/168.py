# Run in terminal: python "vishal/leet/168.py"
def convertToTitle(columnNumber):
    res = ""

    while columnNumber > 0:
        columnNumber -= 1
        res = chr((columnNumber % 26) + ord("A")) + res
        columnNumber //= 26

    return res


columnNumber = 28
print(convertToTitle(columnNumber))  # Output: AB
