# Create and access a nested dictionary with user input
name = input("Enter your name: ")
age = input("Enter your age: ")
subject_scores = {
    "math": int(input("Enter Math score: ")),
    "science": int(input("Enter Science score: ")),
    "english": int(input("Enter English score: "))
}
student = {
    "name": name,
    "age": age,
    "subjects": subject_scores
}
print("Math score:", student["subjects"]["math"])
