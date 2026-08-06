# Run in terminal: python "vishal/leet/1154.py"
def dayOfYear(date):
    year, month, day = map(int, date.split('-'))
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days[1] = 29
    total = sum(days[:month-1]) + day

    return total


date = "2019-01-09"
print(dayOfYear(date))  # Output: 9
