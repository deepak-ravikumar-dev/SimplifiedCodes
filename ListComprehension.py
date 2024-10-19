# Create a list of squares of even numbers entered by the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
squares_of_even = [num ** 2 for num in numbers if num % 2 == 0]
print("Squares of even numbers:", squares_of_even)
