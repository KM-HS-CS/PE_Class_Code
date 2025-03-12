# Program to calculate and print the area of a rectangle

# Define variables for rectangle dimensions
length = 10
width = 0

# Syntax Error 1: Missing colon after 'if' statement
if width > 0
    # Logical Error 1: Incorrect condition, should be 'width > 0'
    print("Calculating area for a rectangle with positive width")
    area = length * width
    print("Area:", area)
else:
    print("Width should be greater than zero")

# Logical Error 2: Incorrect string concatenation, should be "The area is: " + str(area)
print("The area is: " area)

# Syntax Error 2: Unexpected colon after 'else' statement
else:
    print("Width is not valid")

# Runtime Error 1: Division by zero
result = length / 0

# Syntax Error 3: Unmatched parentheses
print("Result of division:", result))

# Logical Error 3: Incorrect condition, should be 'result == 0'
if result = 0:
    print("Result is zero")
else:
    print("Result is not zero")

# Syntax Error 4: Unmatched quotes
print("This is a mismatched quote')

# Logical Error 4: Incorrect condition, should be 'result > 0'
if result < 0:
    print("Result is negative")
else:
    print("Result is zero or positive")


