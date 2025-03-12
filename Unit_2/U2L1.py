# Get user input
age = int(input("Enter your age: "))

# Conditional statements
if age < 0:
    print("Invalid age, please enter a positive number.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 21:
    print("You are an adult but not allowed to drink.")
else:
    print("You are a legal adult.")

# Check if the age is even or odd
if age % 2 == 0:
    print("Your age is an even number.")
else:
    print("Your age is an odd number.")

# Nested conditional statement
if age > 65:
    print("You are eligible for senior discounts.")
elif age > 60:
    print("Consider planning for retirement.")

# Logical operators
hasLicense = input("Do you have a driver's license? (yes/no): ").lower() == 'yes'
ownsCar = input("Do you own a car? (yes/no): ").lower() == 'yes'

if hasLicense and ownsCar:
    print("You can drive your own car.")
elif hasLicense:
    print("Consider getting a car.")

# Ternary conditional expression
canVote = "You can vote." if age >= 18 else "You cannot vote yet."
print(canVote)

