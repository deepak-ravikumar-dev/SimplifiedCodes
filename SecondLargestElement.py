# Find the second largest element in a list entered by the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort(reverse=True)  # Sort in descending order

if len(unique_numbers) >= 2:
    print("The second largest number is:", unique_numbers[1])
else:
    print("There is no second largest number.")
