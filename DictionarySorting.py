# Sort a dictionary by its values based on user input
scores = {}
for _ in range(3):
    name = input("Enter name: ")
    score = int(input(f"Enter {name}'s score: "))
    scores[name] = score
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print("Sorted dictionary by values:", sorted_scores)
