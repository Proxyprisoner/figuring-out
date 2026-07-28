def is_narcissistic(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

user_num = int(input("Enter a positive number: "))

if is_narcissistic(user_num):
    print(f"{user_num} is a Narcissistic number.")
else:
    print(f"{user_num} is NOT a Narcissistic number.")

print(f"\nNarcissistic numbers from 1 to {user_num}:")
for i in range(1, user_num + 1):
    if is_narcissistic(i):
        print(i, end=" ")