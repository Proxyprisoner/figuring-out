# Kaprekar's Constant Visualizer
# This program demonstrates the process of reaching Kaprekar's constant (6174)
# from any 4-digit number (with at least two different digits) using the Kaprekar routine.
# The constant is 6174. Any 4-digit number (with at least two different
# digits) will reach 6174 within 7 steps using this process.

def kaprekar_routine(number):
    step = 1

    while number != 6174:
        # Step 1: Convert number to a 4-digit string (pad with zeros if needed)
        digits = str(number).zfill(4)

        # Step 2: Arrange digits in descending and ascending order
        descending = "".join(sorted(digits, reverse=True))
        ascending = "".join(sorted(digits))

        # Step 3: Subtract smaller from bigger
        big = int(descending)
        small = int(ascending)
        result = big - small

        print(f"Step {step}: {big} - {small} = {result}")

        number = result
        step += 1

    print(f"\nReached Kaprekar's Constant 6174 in {step - 1} steps!")


# ---- Main Program ----
print("Kaprekar's Constant Finder")
user_number = int(input("Enter a 4-digit number (not all same digits): "))

# Basic check: must be 4 digits and not all same digit
if user_number < 1000 or user_number > 9999:
    print("Please enter a valid 4-digit number.")
elif len(set(str(user_number).zfill(4))) == 1:
    print("All digits are the same. Please try a different number.")
else:
    kaprekar_routine(user_number)
