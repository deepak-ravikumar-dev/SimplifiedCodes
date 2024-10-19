# Generate the Fibonacci sequence up to a certain number
n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
