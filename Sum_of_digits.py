# Find the sum of digits of a number entered by the user
num = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in num)
print(f"The sum of the digits of {num} is {sum_of_digits}.")
