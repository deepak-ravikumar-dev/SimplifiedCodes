# Check if a number entered by the user is an Armstrong number
num = int(input("Enter a number to check if it's an Armstrong number: "))
sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))

if num == sum_of_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
