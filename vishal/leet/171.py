# Run in terminal: python "vishal/leet/171.py"
def titleToNumber(columnTitle):
    res = 0
    for ch in columnTitle:
        res = res * 26 + (ord(ch) - ord('A') + 1)
    return res


columnTitle = "AB"
print(titleToNumber(columnTitle))  # Output: 28
