# Separate even and odd numbers from a list entered by the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
