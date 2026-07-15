def create_palindrome(num):
    for i in range(50):
        if num == int(str(num)[::-1]):
            return num
        num = num + int(str(num)[::-1])
    return "Possible Lychrel number"

def Lychamp_numbers(num):
    return create_palindrome(num)

num = int(input("Enter a number: "))
result = Lychamp_numbers(num)
print("The palindrome is:", result)