# Calculate the Least Common Multiple (LCM) of two numbers entered by the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}.")
