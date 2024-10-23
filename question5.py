
age = int(input("Enter your age: "))


if age < 18:
    category = "Minor"
elif 18 <= age <= 65:
    category = "Adult"
else:
    category = "Senior"


print(f"You are a {category}.")
